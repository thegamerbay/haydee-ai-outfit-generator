import pytest
from pathlib import Path
from haydee_outfit_gen.mod_builder import ModBuilder, MultiModBuilder

def test_mod_builder_init_valid(mock_config, mocker):
    """Test initialization with a valid mod name."""
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = ModBuilder("TestOutfit")
    assert builder.mod_name == "TestOutfit"
    # Convert to string to avoid WindowsPath vs PosixPath or absolute differences
    assert str(builder.mod_dir) == str(mock_config.outfits_dir / "TestOutfit")

def test_mod_builder_init_invalid(mock_config):
    """Test that restricted names are rejected."""
    with pytest.raises(ValueError, match="Mod name cannot be 'Haydee'"):
        ModBuilder("Haydee")
    with pytest.raises(ValueError, match="Mod name cannot be 'Haydee'"):
        ModBuilder("haydee")
    with pytest.raises(ValueError, match="Mod name cannot be 'Haydee'"):
        ModBuilder("  HAYDEE  ")

def test_prepare_directory(mock_config, mocker):
    """Test that prepare_directory creates the necessary folder."""
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = ModBuilder("Cyberpunk")
    
    assert not builder.mod_dir.exists()
    builder.prepare_directory()
    assert builder.mod_dir.exists()
    assert builder.mod_dir.is_dir()

def test_prepare_directory_overwrites(mock_config, mocker):
    """Test that existing directories are overwritten cleanly."""
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = ModBuilder("OverwrittenMod")
    builder.prepare_directory()
    
    # Create a dummy file in the directory
    dummy_file = builder.mod_dir / "stray_file.txt"
    dummy_file.write_text("should be deleted")
    
    # Call prepare_directory again
    builder.prepare_directory()
    
    # Check that directory exists but the stray file is gone
    assert builder.mod_dir.exists()
    assert not dummy_file.exists()

def test_generate_mtl_file(mock_config, mocker):
    """Test that the .mtl file is generated with correct content."""
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = ModBuilder("Synthwave")
    builder.prepare_directory()
    builder.generate_mtl_file()
    
    mtl_file = builder.mod_dir / "Suit.mtl"
    assert mtl_file.exists()
    
    content = mtl_file.read_text(encoding="utf-8")
    assert "HD_DATA_TXT 300" in content
    assert 'diffuseMap "Outfits\\Synthwave\\Suit_D.dds"' in content

def test_generate_outfit_file(mock_config, mocker):
    """Test that the .outfit file is generated with correct content."""
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = ModBuilder("Retro")
    builder.prepare_directory()
    builder.generate_outfit_file()
    
    outfit_file = mock_config.outfits_dir / "Retro.outfit"
    assert outfit_file.exists() or (mock_config.haydee_path / "Outfits" / "Retro.outfit").exists()
    
    content = outfit_file.read_text(encoding="utf-8")
    assert "HD_DATA_TXT 300" in content
    assert 'name			"Retro";' in content
    assert 'material	"Outfits\\Retro\\Suit.mtl";' in content

# --- MultiModBuilder Tests ---

def test_multimod_builder_init_valid(mock_config, mocker):
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = MultiModBuilder("Rainbow", ["red", "blue"], "color", "Artem")
    assert builder.multimod_name == "Rainbow"
    assert builder.source_mods == ["red", "blue"]
    assert builder.slot_category == "color"
    assert builder.author == "Artem"
    assert str(builder.mod_dir) == str(mock_config.outfits_dir / "Rainbow")

def test_multimod_builder_init_invalid(mock_config):
    with pytest.raises(ValueError, match="Multi-mod name cannot be 'Haydee'"):
        MultiModBuilder("Haydee", ["red", "blue"])

def test_multimod_validate_sources_success(mock_config, mocker):
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    
    # Create valid source structure
    mod_dir = mock_config.outfits_dir / "red"
    mod_dir.mkdir(parents=True)
    (mod_dir / "Suit_D.dds").write_text("dummy dds data")
    
    builder = MultiModBuilder("Rainbow", ["red"])
    # Should not raise any exception
    builder.validate_sources()

def test_multimod_validate_sources_system_protections(mock_config, mocker):
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = MultiModBuilder("Rainbow", ["Haydee"])
    with pytest.raises(ValueError, match="Cannot group the system 'Haydee' mod"):
        builder.validate_sources()

def test_multimod_validate_sources_missing_mod(mock_config, mocker):
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = MultiModBuilder("Rainbow", ["nonexistent"])
    with pytest.raises(FileNotFoundError, match="Source mod 'nonexistent' not found in"):
        builder.validate_sources()

def test_multimod_validate_sources_missing_texture(mock_config, mocker):
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    mod_dir = mock_config.outfits_dir / "red"
    mod_dir.mkdir(parents=True)
    
    builder = MultiModBuilder("Rainbow", ["red"])
    with pytest.raises(FileNotFoundError, match="Texture file not found in source mod"):
        builder.validate_sources()

def test_multimod_prepare_directory(mock_config, mocker):
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = MultiModBuilder("Rainbow", ["red", "blue"])
    assert not builder.mod_dir.exists()
    builder.prepare_directory()
    assert builder.mod_dir.exists()
    assert builder.mod_dir.is_dir()

def test_multimod_migrate_assets_and_generate_mtls(mock_config, mocker):
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    
    # Create valid source structure
    mod_dir = mock_config.outfits_dir / "red"
    mod_dir.mkdir(parents=True)
    (mod_dir / "Suit_D.dds").write_text("dds binary data")
    
    builder = MultiModBuilder("Rainbow", ["red"])
    builder.prepare_directory()
    builder.migrate_assets_and_generate_mtls()
    
    migrated_dds = builder.mod_dir / "red_d.dds"
    assert migrated_dds.exists()
    assert migrated_dds.read_text() == "dds binary data"
    
    mtl_file = builder.mod_dir / "red.mtl"
    assert mtl_file.exists()
    mtl_content = mtl_file.read_text(encoding="utf-8")
    assert 'diffuseMap "Outfits\\Rainbow\\red_d.dds"' in mtl_content

def test_multimod_generate_outfit_file(mock_config, mocker):
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    builder = MultiModBuilder("Rainbow", ["red", "blue"], "color", "Artem")
    builder.prepare_directory()
    builder.generate_outfit_file()
    
    outfit_file = mock_config.outfits_dir / "Rainbow.outfit"
    assert outfit_file.exists()
    content = outfit_file.read_text(encoding="utf-8")
    assert 'name			"Rainbow";' in content
    assert 'slot		"mod by" "Artem";' in content
    assert 'slot		"color" "red";' in content
    assert 'slot		"color" "blue";' in content
    assert 'material	"Outfits\\Rainbow\\red.mtl";' in content

def test_multimod_cleanup_sources(mock_config, mocker):
    mocker.patch('haydee_outfit_gen.mod_builder.settings', mock_config)
    
    # Create dummy source mod dir and outfit
    mod_dir = mock_config.outfits_dir / "red"
    mod_dir.mkdir(parents=True)
    (mock_config.outfits_dir / "red.outfit").write_text("dummy config")
    
    assert mod_dir.exists()
    assert (mock_config.outfits_dir / "red.outfit").exists()
    
    builder = MultiModBuilder("Rainbow", ["red"])
    builder.cleanup_sources()
    
    assert not mod_dir.exists()
    assert not (mock_config.outfits_dir / "red.outfit").exists()

