import pytest
from unittest.mock import MagicMock, patch
import haydee_outfit_gen.main as main

@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "generate"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.ModBuilder")
@patch("haydee_outfit_gen.main.ImageProcessor")
@patch("haydee_outfit_gen.main.Settings")
@patch("haydee_outfit_gen.main.GeminiModClient")
@patch("haydee_outfit_gen.main.tempfile.TemporaryDirectory")
def test_main_success_flow(
    mock_tmp_dir, 
    mock_gemini_client_class,
    mock_settings_class,
    mock_image_processor, 
    mock_mod_builder_class, 
    mock_parse_args, 
    mock_config
):
    """Test the successful end-to-end run of the CLI application."""
    mock_args = MagicMock()
    mock_args.command = "generate"
    mock_args.name = "TestMod"
    mock_args.style = "Test Style"
    mock_args.author = None
    mock_parse_args.return_value = mock_args
    
    mock_path = MagicMock()
    mock_path.exists.return_value = True
    
    mock_settings_instance = MagicMock()
    mock_settings_instance.base_texture_path = mock_path
    mock_settings_class.return_value = mock_settings_instance
    
    # Setup ModBuilder mock
    mock_builder_instance = MagicMock()
    mock_builder_instance.mod_dir = mock_config.outfits_dir / "TestMod"
    mock_mod_builder_class.return_value = mock_builder_instance
    
    # Setup temp directory mock
    mock_tmp_context = MagicMock()
    mock_tmp_context.__enter__.return_value = "/tmp/fake_dir"
    mock_tmp_dir.return_value = mock_tmp_context
    
    # Setup Gemini client mock
    mock_gemini_instance = MagicMock()
    mock_gemini_client_class.return_value = mock_gemini_instance
    
    # Run main
    main.main()
    
    # Verifications
    mock_builder_instance.prepare_directory.assert_called_once()
    mock_image_processor.dds_to_png.assert_called_once()
    mock_gemini_instance.generate_texture.assert_called_once()
    mock_image_processor.img_to_dds.assert_called_once()
    mock_builder_instance.generate_mtl_file.assert_called_once()
    mock_builder_instance.generate_outfit_file.assert_called_once()
    
@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "--name", "OldStyle", "--style", "cool"])
@patch("haydee_outfit_gen.main.ModBuilder")
@patch("haydee_outfit_gen.main.ImageProcessor")
@patch("haydee_outfit_gen.main.Settings")
@patch("haydee_outfit_gen.main.GeminiModClient")
@patch("haydee_outfit_gen.main.tempfile.TemporaryDirectory")
def test_main_backward_compatibility(
    mock_tmp_dir, 
    mock_gemini_client_class,
    mock_settings_class,
    mock_image_processor, 
    mock_mod_builder_class, 
    mock_config
):
    """Test that running without a subcommand defaults to 'generate'."""
    mock_path = MagicMock()
    mock_path.exists.return_value = True
    
    mock_settings_instance = MagicMock()
    mock_settings_instance.base_texture_path = mock_path
    mock_settings_class.return_value = mock_settings_instance
    
    # Setup ModBuilder mock
    mock_builder_instance = MagicMock()
    mock_builder_instance.mod_dir = mock_config.outfits_dir / "OldStyle"
    mock_mod_builder_class.return_value = mock_builder_instance
    
    # Setup temp directory mock
    mock_tmp_context = MagicMock()
    mock_tmp_context.__enter__.return_value = "/tmp/fake_dir"
    mock_tmp_dir.return_value = mock_tmp_context
    
    # Setup Gemini client mock
    mock_gemini_instance = MagicMock()
    mock_gemini_client_class.return_value = mock_gemini_instance
    
    # Run main
    main.main()
    
    # Verifications
    mock_builder_instance.prepare_directory.assert_called_once()
    mock_image_processor.dds_to_png.assert_called_once()
    mock_gemini_instance.generate_texture.assert_called_once()
    mock_image_processor.img_to_dds.assert_called_once()

@patch("haydee_outfit_gen.main.Settings")
@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "generate"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.ModBuilder")
def test_main_base_texture_not_found(mock_mod_builder_class, mock_parse_args, mock_settings_class, mock_config, caplog):
    """Test that main exits and logs an error when the base texture is missing."""
    import logging
    
    mock_args = MagicMock()
    mock_args.command = "generate"
    mock_args.name = "TestMod"
    mock_args.style = "Test Style"
    mock_args.author = None
    mock_parse_args.return_value = mock_args

    mock_path = MagicMock()
    mock_path.exists.return_value = False

    mock_settings_instance = MagicMock()
    mock_settings_instance.base_texture_path = mock_path
    mock_settings_class.return_value = mock_settings_instance

    # main script uses exit(1) on failure
    with pytest.raises(SystemExit) as excinfo:
       with caplog.at_level(logging.ERROR):
           main.main()
           
    assert excinfo.value.code == 1
    assert "Base texture not found" in caplog.text

@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "generate"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.ModBuilder")
def test_main_general_exception(mock_mod_builder_class, mock_parse_args, mock_config, caplog):
    """Test that unexpected exceptions are caught and logged."""
    import logging
    
    mock_args = MagicMock()
    mock_args.command = "generate"
    mock_args.name = "TestMod"
    mock_args.style = "Test Style"
    mock_args.author = None
    mock_parse_args.return_value = mock_args
    
    mock_mod_builder_class.side_effect = Exception("A wild unexpected error appeared!")
    
    with pytest.raises(SystemExit) as excinfo:
       with caplog.at_level(logging.ERROR):
           main.main()
           
    assert excinfo.value.code == 1
    assert "An error occurred" in caplog.text
    assert "A wild unexpected error appeared!" in caplog.text

@patch("haydee_outfit_gen.main.Settings")
@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "group"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.MultiModBuilder")
def test_main_group_success_flow(
    mock_multimod_builder_class, 
    mock_parse_args,
    mock_settings_class,
    mock_config
):
    """Test the successful end-to-end run of the group CLI command."""
    mock_settings_instance = MagicMock()
    mock_settings_class.return_value = mock_settings_instance
    mock_args = MagicMock()
    mock_args.command = "group"
    mock_args.name = "Rainbow"
    mock_args.mods = ["red", "blue"]
    mock_args.slot_category = "color"
    mock_args.author = "Artem"
    mock_args.delete_sources = True
    mock_parse_args.return_value = mock_args
    
    mock_builder_instance = MagicMock()
    mock_multimod_builder_class.return_value = mock_builder_instance
    
    main.main()
    
    # Verifications
    mock_multimod_builder_class.assert_called_once_with(
        multimod_name="Rainbow",
        source_mods=["red", "blue"],
        outfits_dir=mock_settings_instance.outfits_dir,
        slot_category="color",
        author="Artem"
    )
    mock_builder_instance.validate_sources.assert_called_once()
    mock_builder_instance.prepare_directory.assert_called_once()
    mock_builder_instance.migrate_assets_and_generate_mtls.assert_called_once()
    mock_builder_instance.generate_outfit_file.assert_called_once()
    mock_builder_instance.cleanup_sources.assert_called_once()
