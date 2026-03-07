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

    @staticmethod
    def create_specular_map(mask_path: Path, dds_path: Path, resolution: str = "4K") -> None:
        """Converts the AI grayscale mask into a technical Suit_S texture (R=Roughness, G=Specular)."""
        logger.info("Packing material mask into Specular/Roughness channels...")
        
        with Image.open(mask_path) as mask_img:
            # Convert to grayscale just in case
            mask_l = mask_img.convert("L")
            
            # R-channel (Roughness)
            # If mask is white (glossy) -> roughness is low (e.g., 50)
            # If mask is black (matte) -> roughness is high (e.g., 250)
            def map_roughness(val):
                return int(250 - (val / 255.0) * 200)

            # G-channel (Specular)
            # If mask is white -> specular is strong (255)
            # If mask is black -> specular is weak (20)
            def map_specular(val):
                return int(20 + (val / 255.0) * 235)

            # Apply math to pixels
            r_channel = mask_l.point(map_roughness)
            g_channel = mask_l.point(map_specular)
            
            # B-channel (Metallic) is usually black for Haydee unless a custom shader is used
            b_channel = Image.new("L", mask_l.size, 0)
            
            # Pack the separated masks into a new RGB texture
            suit_s = Image.merge("RGB", (r_channel, g_channel, b_channel))
            
            # Resize and save to DDS
            target_size = 4096 if resolution == "4K" else 2048
            suit_s_resized = suit_s.resize((target_size, target_size), Image.Resampling.LANCZOS)
            suit_s_resized.save(dds_path, format="DDS", pixel_format="DXT5")
            
        logger.info(f"Successfully created specular map: {dds_path}")

    @staticmethod
    def create_neutral_normal_map(dds_path: Path, resolution: str = "4K") -> None:
        """Generates a flat, neutral normal map (128, 128, 255) to remove baked geometry details."""
        logger.info("Generating a neutral normal map (Suit_N.dds)...")
        
        target_size = 4096 if resolution == "4K" else 2048
        
        # Neutral normal map color: R=128, G=128, B=255
        neutral_color = (128, 128, 255)
        neutral_img = Image.new("RGB", (target_size, target_size), neutral_color)
        
        # Save as DDS
        neutral_img.save(dds_path, format="DDS", pixel_format="DXT5")
        
        logger.info(f"Successfully created neutral normal map: {dds_path}")
