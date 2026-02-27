import pytest
import os
import sys
from unittest.mock import MagicMock
from pathlib import Path


# Set default environment variables for testing before config is imported
os.environ["GEMINI_API_KEY"] = "fake_test_key_123"
os.environ["HAYDEE_PATH"] = str(Path("/tmp/fake_haydee_path"))

@pytest.fixture
def mock_haydee_path(tmp_path):
    """Provides a temporary mock Haydee installation directory."""
    haydee_dir = tmp_path / "Haydee"
    outfits_dir = haydee_dir / "Outfits"
    base_outfit_dir = outfits_dir / "Haydee"
    
    base_outfit_dir.mkdir(parents=True)
    
    # Create a dummy base texture
    suit_d = base_outfit_dir / "Suit_D.dds"
    suit_d.write_text("dummy dds data")
    
    # Update environment variable to point to tmp_path
    os.environ["HAYDEE_PATH"] = str(haydee_dir)
    return haydee_dir

@pytest.fixture
def mock_config(mock_haydee_path):
    """Returns a Settings instance with the mocked Haydee path."""
    import haydee_outfit_gen.config
    
    settings = haydee_outfit_gen.config.Settings()
    yield settings
