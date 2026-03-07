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

def test_create_specular_map(mocker, tmp_path):
    """Test that material mask is correctly packed into a specular map."""
    mock_image_open = mocker.patch('haydee_outfit_gen.image_processor.Image.open')
    mock_img_context = mock_image_open.return_value.__enter__.return_value
    
    # Mock convert to L
    mock_l = mocker.MagicMock()
    mock_img_context.convert.return_value = mock_l
    mock_l.size = (4096, 4096)
    
    # Mock point (applying map functions)
    mock_channel = mocker.MagicMock()
    mock_l.point.return_value = mock_channel
    
    # Mock Image.new for B-channel
    mock_image_new = mocker.patch('haydee_outfit_gen.image_processor.Image.new')
    mock_b_channel = mocker.MagicMock()
    mock_image_new.return_value = mock_b_channel
    
    # Mock Image.merge for RGB packing
    mock_image_merge = mocker.patch('haydee_outfit_gen.image_processor.Image.merge')
    mock_merged = mocker.MagicMock()
    mock_image_merge.return_value = mock_merged
    
    # Mock resize
    mock_resized = mocker.MagicMock()
    mock_merged.resize.return_value = mock_resized
    
    mask_path = tmp_path / "mask.png"
    dds_path = tmp_path / "output_s.dds"
    
    ImageProcessor.create_specular_map(mask_path, dds_path, resolution="4K")
    
    # Verify open was called
    mock_image_open.assert_called_once_with(mask_path)
    
    # Verify channel extractions and merge
    assert mock_l.point.call_count == 2
    mock_image_new.assert_called_once_with("L", (4096, 4096), 0)
    mock_image_merge.assert_called_once_with("RGB", (mock_channel, mock_channel, mock_b_channel))
    
    # Verify save
    mock_merged.resize.assert_called_once_with((4096, 4096), Image.Resampling.LANCZOS)
    mock_resized.save.assert_called_once_with(dds_path, format="DDS", pixel_format="DXT5")

def test_create_neutral_normal_map(mocker, tmp_path):
    """Test that the neutral normal map is correctly generated and saved."""
    mock_image_new = mocker.patch('haydee_outfit_gen.image_processor.Image.new')
    mock_neutral_img = mocker.MagicMock()
    mock_image_new.return_value = mock_neutral_img
    
    dds_path = tmp_path / "Suit_N.dds"
    
    ImageProcessor.create_neutral_normal_map(dds_path, resolution="4K")
    
    mock_image_new.assert_called_once_with("RGB", (4096, 4096), (128, 128, 255))
    mock_neutral_img.save.assert_called_once_with(dds_path, format="DDS", pixel_format="DXT5")
