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
        """Generates a flat, neutral normal map (128, 128, 128, 128) for DXT5nm format."""
        logger.info("Generating a neutral normal map (Suit_N.dds)...")
        
        target_size = 4096 if resolution == "4K" else 2048
        
        # In DXT5nm format, a flat normal is a semi-transparent gray (Alpha = 128)
        neutral_color = (128, 128, 128, 128)
        neutral_img = Image.new("RGBA", (target_size, target_size), neutral_color)
        
        # Save as DDS
        neutral_img.save(dds_path, format="DDS", pixel_format="DXT5")
        
        logger.info(f"Successfully created neutral normal map: {dds_path}")

    @staticmethod
    def create_custom_normal_map(normal_path: Path, dds_path: Path, resolution: str = "4K") -> None:
        """Converts a standard RGB normal map from AI into Haydee's DXT5nm format."""
        logger.info("Packing AI normal map into DXT5nm format...")
        
        with Image.open(normal_path) as img:
            # Ensure we are working in RGB mode
            img = img.convert("RGB")
            
            # Split standard blue normal map into channels: R (X-axis), G (Y-axis), B (Z-axis)
            r, g, b = img.split()
            
            # Create a neutral channel "dummy" filled with 128 (gray)
            neutral = Image.new("L", img.size, 128)
            
            # Pack into DXT5nm format for Haydee:
            # R = 128 (muted)
            # G = G (keep Y-axis)
            # B = 128 (muted)
            # Alpha = R (move X-axis into the alpha channel)
            suit_n = Image.merge("RGBA", (neutral, g, neutral, r))
            
            target_size = 4096 if resolution == "4K" else 2048
            suit_n_resized = suit_n.resize((target_size, target_size), Image.Resampling.LANCZOS)
            suit_n_resized.save(dds_path, format="DDS", pixel_format="DXT5")
            
        logger.info(f"Successfully created custom normal map: {dds_path}")
