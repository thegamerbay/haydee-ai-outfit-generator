import pytest
import os
from pydantic_settings import BaseSettings
from pydantic import ValidationError

def test_settings_initialization(mock_config):
    """Test that settings load correctly from the environment."""
    assert mock_config.gemini_api_key == "fake_test_key_123"
    assert mock_config.model_name == "gemini-3.1-flash-image-preview"
    assert mock_config.validator_model == "gemini-3.1-pro-preview"
    assert "fake_haydee_path" in str(mock_config.haydee_path) or "pytest" in str(mock_config.haydee_path)

def test_settings_property_outfits_dir(mock_config):
    """Test the computed outfits_dir property."""
    expected_path = mock_config.haydee_path / "Outfits"
    assert mock_config.outfits_dir == expected_path

def test_settings_property_base_texture_path(mock_config):
    """Test the computed base_texture_path property."""
    expected_path = mock_config.haydee_path / "Outfits" / "Haydee" / "Suit_D.dds"
    assert mock_config.base_texture_path == expected_path

def test_settings_missing_api_key(monkeypatch):
    """Test that missing required settings raise ValidationError."""
    import os
    import haydee_outfit_gen.config
    
    # Force pure environment variables for this test
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    
    with pytest.raises(ValidationError) as excinfo:
        haydee_outfit_gen.config.Settings(_env_file=None)
        
    assert "gemini_api_key" in str(excinfo.value)

def test_settings_missing_haydee_path(monkeypatch):
    """Test that missing required settings raise ValidationError."""
    import os
    import haydee_outfit_gen.config
    
    monkeypatch.delenv("HAYDEE_PATH", raising=False)
    monkeypatch.setenv("GEMINI_API_KEY", "fake_test_key")
    
    with pytest.raises(ValidationError) as excinfo:
        haydee_outfit_gen.config.Settings(_env_file=None)
        
    assert "haydee_path" in str(excinfo.value)
