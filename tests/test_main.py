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
    mock_args.skip_d = False
    mock_args.skip_s = False
    mock_args.skip_n = False
    mock_args.max_retries = 3
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
    mock_gemini_instance.generate_material_mask.assert_called_once()
    mock_image_processor.img_to_dds.assert_called_once()
    mock_image_processor.create_specular_map.assert_called_once()
    mock_gemini_instance.generate_normal_map.assert_called_once()
    mock_image_processor.create_custom_normal_map.assert_called_once()
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
    mock_gemini_instance.generate_material_mask.assert_called_once()
    mock_image_processor.img_to_dds.assert_called_once()
    mock_image_processor.create_specular_map.assert_called_once()
    mock_gemini_instance.generate_normal_map.assert_called_once()
    mock_image_processor.create_custom_normal_map.assert_called_once()

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
    mock_args.skip_d = False
    mock_args.skip_s = False
    mock_args.skip_n = False
    mock_args.max_retries = 3
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
    mock_args.skip_d = False
    mock_args.skip_s = False
    mock_args.skip_n = False
    mock_args.max_retries = 3
    mock_parse_args.return_value = mock_args
    
    mock_mod_builder_class.side_effect = Exception("A wild unexpected error appeared!")
    
    with pytest.raises(SystemExit) as excinfo:
       with caplog.at_level(logging.ERROR):
           main.main()
           
    assert excinfo.value.code == 1
    assert "An error occurred" in caplog.text
    assert "A wild unexpected error appeared!" in caplog.text

@patch("haydee_outfit_gen.main.ImageProcessor")
@patch("haydee_outfit_gen.main.Settings")
@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "group"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.MultiModBuilder")
def test_main_group_success_flow(
    mock_multimod_builder_class, 
    mock_parse_args,
    mock_settings_class,
    mock_image_processor_class,
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
    mock_image_processor_class.create_neutral_normal_map.assert_called_once()
    mock_builder_instance.generate_outfit_file.assert_called_once()
    mock_builder_instance.cleanup_sources.assert_called_once()


    
@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "generate"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.ModBuilder")
@patch("haydee_outfit_gen.main.ImageProcessor")
@patch("haydee_outfit_gen.main.Settings")
@patch("haydee_outfit_gen.main.GeminiModClient")
@patch("haydee_outfit_gen.main.tempfile.TemporaryDirectory")
def test_main_skip_all_except_d(
    mock_tmp_dir, 
    mock_gemini_client_class,
    mock_settings_class,
    mock_image_processor, 
    mock_mod_builder_class, 
    mock_parse_args, 
    mock_config
):
    """Test skipping Suit_S and Suit_N generates only Suit_D."""
    mock_args = MagicMock()
    mock_args.command = "generate"
    mock_args.name = "TestMod"
    mock_args.style = "Test Style"
    mock_args.author = None
    mock_args.skip_d = False
    mock_args.skip_s = True
    mock_args.skip_n = True
    mock_args.max_retries = 3
    mock_parse_args.return_value = mock_args

    mock_path = MagicMock()
    mock_path.exists.return_value = True

    mock_settings_instance = MagicMock()
    mock_settings_instance.base_texture_path = mock_path
    mock_settings_class.return_value = mock_settings_instance

    mock_builder_instance = MagicMock()
    mock_builder_instance.mod_dir = mock_config.outfits_dir / "TestMod"
    mock_mod_builder_class.return_value = mock_builder_instance

    mock_tmp_context = MagicMock()
    mock_tmp_context.__enter__.return_value = "/tmp/fake_dir"
    mock_tmp_dir.return_value = mock_tmp_context

    mock_gemini_instance = MagicMock()
    mock_gemini_client_class.return_value = mock_gemini_instance

    main.main()

    # Verifications
    mock_builder_instance.prepare_directory.assert_called_once_with(clear_dir=True)
    mock_image_processor.dds_to_png.assert_called_once()
    mock_gemini_instance.generate_texture.assert_called_once()
    mock_image_processor.img_to_dds.assert_called_once()
    
    # These should NOT be called
    mock_gemini_instance.generate_material_mask.assert_not_called()
    mock_image_processor.create_specular_map.assert_not_called()
    mock_gemini_instance.generate_normal_map.assert_not_called()
    mock_image_processor.create_custom_normal_map.assert_not_called()
    
    mock_builder_instance.generate_mtl_file.assert_called_once()


@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "generate"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.ModBuilder")
@patch("haydee_outfit_gen.main.ImageProcessor")
@patch("haydee_outfit_gen.main.Settings")
@patch("haydee_outfit_gen.main.GeminiModClient")
@patch("haydee_outfit_gen.main.tempfile.TemporaryDirectory")
def test_main_skip_d_without_style(
    mock_tmp_dir, 
    mock_gemini_client_class,
    mock_settings_class,
    mock_image_processor, 
    mock_mod_builder_class, 
    mock_parse_args, 
    mock_config
):
    """Test skipping Suit_D without style and successfully generating S and N using existing D."""
    mock_args = MagicMock()
    mock_args.command = "generate"
    mock_args.name = "TestMod"
    mock_args.style = None
    mock_args.author = None
    mock_args.skip_d = True
    mock_args.skip_s = False
    mock_args.skip_n = False
    mock_args.max_retries = 3
    mock_parse_args.return_value = mock_args

    mock_path = MagicMock()
    mock_path.exists.return_value = True
    mock_settings_instance = MagicMock()
    mock_settings_instance.base_texture_path = mock_path
    mock_settings_class.return_value = mock_settings_instance

    mock_builder_instance = MagicMock()
    mock_builder_instance.mod_dir = mock_config.outfits_dir / "TestMod"
    mock_mod_builder_class.return_value = mock_builder_instance

    mock_tmp_context = MagicMock()
    mock_tmp_context.__enter__.return_value = "/tmp/fake_dir"
    mock_tmp_dir.return_value = mock_tmp_context

    mock_gemini_instance = MagicMock()
    mock_gemini_client_class.return_value = mock_gemini_instance

    # Mock that Suit_D.dds DOES exist in mod dir
    with patch("haydee_outfit_gen.main.Path.exists", return_value=True):
        main.main()

    # Verify style wasn't needed and image processing called for S and N
    mock_gemini_instance.generate_texture.assert_not_called()
    mock_image_processor.dds_to_png.assert_called_once() # Should be called to convert existing Suit_D
    mock_gemini_instance.generate_material_mask.assert_called_once()
    mock_gemini_instance.generate_normal_map.assert_called_once()


@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "generate"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.ModBuilder")
@patch("haydee_outfit_gen.main.Settings")
def test_main_skip_d_missing_existing(
    mock_settings_class,
    mock_mod_builder_class, 
    mock_parse_args, 
    mock_config,
    caplog
):
    """Test skipping Suit_D when it does not exist locally should fail."""
    import logging
    
    mock_args = MagicMock()
    mock_args.command = "generate"
    mock_args.name = "TestMod"
    mock_args.style = None
    mock_args.author = None
    mock_args.skip_d = True
    mock_args.skip_s = False
    mock_args.skip_n = False
    mock_args.max_retries = 3
    mock_parse_args.return_value = mock_args

    mock_settings_instance = MagicMock()
    mock_settings_class.return_value = mock_settings_instance

    mock_builder_instance = MagicMock()
    mock_builder_instance.mod_dir = mock_config.outfits_dir / "TestMod"
    mock_mod_builder_class.return_value = mock_builder_instance

    # Mock that Suit_D.dds does NOT exist in mod dir
    with patch("haydee_outfit_gen.main.Path.exists", return_value=False):
        with pytest.raises(SystemExit) as excinfo:
            with caplog.at_level(logging.ERROR):
                main.main()
                
    assert "Cannot generate Suit_S or Suit_N because Suit_D generation was skipped and Suit_D.dds does not exist" in caplog.text

@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "generate"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.ModBuilder")
@patch("haydee_outfit_gen.main.ImageProcessor")
@patch("haydee_outfit_gen.main.Settings")
@patch("haydee_outfit_gen.main.GeminiModClient")
@patch("haydee_outfit_gen.main.tempfile.TemporaryDirectory")
def test_main_retry_success_second_attempt(
    mock_tmp_dir, 
    mock_gemini_client_class,
    mock_settings_class,
    mock_image_processor, 
    mock_mod_builder_class, 
    mock_parse_args, 
    mock_config,
    caplog
):
    """Test that generation retries successfully on the second attempt after initially failing validation."""
    mock_args = MagicMock()
    mock_args.command = "generate"
    mock_args.name = "TestMod"
    mock_args.style = "Test Style"
    mock_args.author = None
    mock_args.skip_d = False
    mock_args.skip_s = True
    mock_args.skip_n = True
    mock_args.max_retries = 3
    mock_parse_args.return_value = mock_args
    
    mock_path = MagicMock()
    mock_path.exists.return_value = True
    mock_settings_instance = MagicMock()
    mock_settings_instance.base_texture_path = mock_path
    mock_settings_class.return_value = mock_settings_instance
    
    mock_builder_instance = MagicMock()
    mock_builder_instance.mod_dir = mock_config.outfits_dir / "TestMod"
    mock_mod_builder_class.return_value = mock_builder_instance
    
    mock_tmp_context = MagicMock()
    mock_tmp_context.__enter__.return_value = "/tmp/fake_dir"
    mock_tmp_dir.return_value = mock_tmp_context
    
    # Setup Gemini client mock
    mock_gemini_instance = MagicMock()
    mock_gemini_client_class.return_value = mock_gemini_instance
    
    from haydee_outfit_gen.gemini_client import ValidationResult
    invalid_result = ValidationResult(is_face_valid=False, is_torso_seams_valid=True, is_legs_valid=True, feedback="Bad anatomy.")
    valid_result = ValidationResult(is_face_valid=True, is_torso_seams_valid=True, is_legs_valid=True, feedback="Looks good.")
    
    # First call returns invalid, second call returns valid
    mock_gemini_instance.validate_texture.side_effect = [invalid_result, valid_result]
    
    import logging
    with caplog.at_level(logging.INFO):
        main.main()
    
    # Verify generate_texture was called exactly 2 times
    assert mock_gemini_instance.generate_texture.call_count == 2
    # The first time feedback was None, the second time it was "Bad anatomy."
    calls = mock_gemini_instance.generate_texture.call_args_list
    assert calls[0].kwargs.get("previous_feedback") is None
    assert calls[1].kwargs.get("previous_feedback") == "Bad anatomy."
    
    assert "Texture validation failed: Bad anatomy." in caplog.text
    assert "Texture passed QA validation!" in caplog.text

@patch("haydee_outfit_gen.main.sys.argv", ["haydee-gen", "generate"])
@patch("haydee_outfit_gen.main.argparse.ArgumentParser.parse_args")
@patch("haydee_outfit_gen.main.ModBuilder")
@patch("haydee_outfit_gen.main.ImageProcessor")
@patch("haydee_outfit_gen.main.Settings")
@patch("haydee_outfit_gen.main.GeminiModClient")
@patch("haydee_outfit_gen.main.tempfile.TemporaryDirectory")
def test_main_retry_failure_max_retries(
    mock_tmp_dir, 
    mock_gemini_client_class,
    mock_settings_class,
    mock_image_processor, 
    mock_mod_builder_class, 
    mock_parse_args, 
    mock_config,
    caplog
):
    """Test that generation attempts hit the max_retries limit and proceeds with a warning."""
    mock_args = MagicMock()
    mock_args.command = "generate"
    mock_args.name = "TestMod"
    mock_args.style = "Test Style"
    mock_args.author = None
    mock_args.skip_d = False
    mock_args.skip_s = True
    mock_args.skip_n = True
    mock_args.max_retries = 3
    mock_parse_args.return_value = mock_args
    
    mock_path = MagicMock()
    mock_path.exists.return_value = True
    mock_settings_instance = MagicMock()
    mock_settings_instance.base_texture_path = mock_path
    mock_settings_class.return_value = mock_settings_instance
    
    mock_builder_instance = MagicMock()
    mock_builder_instance.mod_dir = mock_config.outfits_dir / "TestMod"
    mock_mod_builder_class.return_value = mock_builder_instance
    
    mock_tmp_context = MagicMock()
    mock_tmp_context.__enter__.return_value = "/tmp/fake_dir"
    mock_tmp_dir.return_value = mock_tmp_context
    
    mock_gemini_instance = MagicMock()
    mock_gemini_client_class.return_value = mock_gemini_instance
    
    from haydee_outfit_gen.gemini_client import ValidationResult
    invalid_result = ValidationResult(is_face_valid=False, is_torso_seams_valid=True, is_legs_valid=True, feedback="Persistent bad anatomy.")
    
    # Always returns invalid
    mock_gemini_instance.validate_texture.return_value = invalid_result
    
    import logging
    with caplog.at_level(logging.INFO):
        main.main()
    
    # Verify generate_texture was called exactly max_retries (3) times
    assert mock_gemini_instance.generate_texture.call_count == 3
    
    assert "Texture validation failed: Persistent bad anatomy." in caplog.text
    assert "Max retries (3) reached. Proceeding with the last generated texture" in caplog.text
