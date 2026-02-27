import pytest
from pathlib import Path
from PIL import Image
from haydee_outfit_gen.image_processor import ImageProcessor

def test_dds_to_png(mocker, tmp_path):
    """Test that dds format conversion properties are set accurately."""
    mock_image_open = mocker.patch('haydee_outfit_gen.image_processor.Image.open')
    mock_img_context = mock_image_open.return_value.__enter__.return_value
    
    dds_path = tmp_path / "input.dds"
    png_path = tmp_path / "output.png"
    
    ImageProcessor.dds_to_png(dds_path, png_path)
    
    # Verify the Image class was initialized correctly
    mock_image_open.assert_called_once_with(dds_path)
    
    # Verify format and save were called on instance
    mock_img_context.save.assert_called_once_with(png_path, format="PNG")

@pytest.mark.parametrize("resolution, expected_size", [
    ("4K", 4096),
    ("2K", 2048)
])
def test_img_to_dds(mocker, tmp_path, resolution, expected_size):
    """Test that image conversion to dds executes required transformations."""
    mock_image_open = mocker.patch('haydee_outfit_gen.image_processor.Image.open')
    mock_img_context = mock_image_open.return_value.__enter__.return_value
    mock_resized = mocker.MagicMock()
    mock_img_context.resize.return_value = mock_resized
    
    img_path = tmp_path / "input.jpg"
    dds_path = tmp_path / "output.dds"
    
    ImageProcessor.img_to_dds(img_path, dds_path, resolution=resolution)
    
    # Verify the Image class was initialized correctly
    mock_image_open.assert_called_once_with(img_path)
    
    # Verify the required transformations
    mock_img_context.resize.assert_called_once_with((expected_size, expected_size), Image.Resampling.LANCZOS)
    mock_resized.save.assert_called_once_with(dds_path, format="DDS", pixel_format="DXT5")
