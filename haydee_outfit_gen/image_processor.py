import logging
from pathlib import Path
from PIL import Image

logger = logging.getLogger(__name__)

class ImageProcessor:
    """Handles image conversions between DDS and standard formats."""

    @staticmethod
    def dds_to_png(dds_path: Path, png_path: Path) -> None:
        """Converts a DDS texture to PNG format for API processing."""
        logger.info(f"Converting {dds_path.name} to PNG...")
        with Image.open(dds_path) as img:
            img.save(png_path, format="PNG")
        logger.info(f"Successfully saved to {png_path}")

    @staticmethod
    def img_to_dds(img_path: Path, dds_path: Path, resolution: str = "4K") -> None:
        """Converts a generated image (PNG/JPG) back to DDS format."""
        logger.info(f"Converting {img_path.name} to DDS...")
        with Image.open(img_path) as img:
            target_size = 4096 if resolution == "4K" else 2048
            
            # Resize with a high-quality anti-aliasing filter
            img_resized = img.resize((target_size, target_size), Image.Resampling.LANCZOS)
            
            # Save directly to DDS with DXT5 compression
            img_resized.save(dds_path, format="DDS", pixel_format="DXT5")
            
        logger.info(f"Successfully saved to {dds_path}")
