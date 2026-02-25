import logging
from pathlib import Path
from google import genai
from google.genai import types
from .config import settings

logger = logging.getLogger(__name__)

class GeminiModClient:
    """Handles communication with the Gemini API for texture generation."""

    def __init__(self):
        self.client = genai.Client(api_key=settings.gemini_api_key)

    def generate_texture(self, base_image_path: Path, style: str, output_path: Path) -> None:
        """
        Sends the base texture and prompt to Gemini to generate a new texture.
        """
        logger.info(f"Requesting Gemini to generate texture in style: '{style}'...")

        res_text = "4096x4096 (4K)" if settings.image_resolution == "4K" else "2048x2048 (2K)"

        # Enhanced prompt tailored to the character's cybernetic/biomechanical nature
        prompt = f"""
        Attached is a UV map texture for the 3D character model 'Haydee'. 
        The character is a biomechanical humanoid with distinct segmented armor plates, synthetic skin, and specific anatomical proportions.

        I need you to completely transform the visual theme of this texture into: {style}.

        CRITICAL INSTRUCTIONS:
        1. Exact Mapping: Maintain the exact UV layout, seams, alignment, and proportions of the original image so it maps perfectly back onto the 3D model.
        2. Transparency/Background: Keep the blank and transparent spaces exactly where they are in the original file. Do not fill empty UV space.
        3. Application: Apply the '{style}' aesthetic purely to the textured areas (armor panels, skin, details).
        4. Quality: Ensure high-fidelity texturing with sharp details, respecting the shadows and highlights of the original topology.
        5. Resolution: Please generate the output image in exactly {res_text} resolution.
        
        Output ONLY the generated texture image.
        """
        
        try:
            from PIL import Image
            
            contents = [
                prompt,
                Image.open(base_image_path)
            ]
            
            result = self.client.models.generate_content(
                model='gemini-3-pro-image-preview',
                contents=contents,
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE'],
                    image_config=types.ImageConfig(
                        image_size=settings.image_resolution
                    )
                )
            )

            # Save the generated image
            saved = False
            # Check for standard text/multimodal response structure
            if hasattr(result, 'candidates') and result.candidates:
                for candidate in result.candidates:
                    if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                        for part in candidate.content.parts:
                            if hasattr(part, 'image') and part.image:
                                 with open(output_path, "wb") as f:
                                    f.write(part.image.image_bytes)
                                 saved = True
                                 break
                            elif hasattr(part, 'inline_data') and part.inline_data:
                                 with open(output_path, "wb") as f:
                                    f.write(part.inline_data.data)
                                 saved = True
                                 break
            
            # Alternative fallback for direct parts
            if not saved and hasattr(result, 'parts') and result.parts:
                for part in result.parts:
                    if hasattr(part, 'image') and part.image:
                         with open(output_path, "wb") as f:
                            f.write(part.image.image_bytes)
                         saved = True
                         break
                    elif hasattr(part, 'inline_data') and part.inline_data:
                         with open(output_path, "wb") as f:
                            f.write(part.inline_data.data)
                         saved = True
                         break
            if not saved:
                raise RuntimeError("No image was returned from Gemini API.")
                
            try:
                with Image.open(output_path) as gen_img:
                    width, height = gen_img.size
                    logger.info(f"Generated image resolution from Gemini API: {width}x{height}")
            except Exception as e:
                logger.warning(f"Could not determine generated image resolution: {e}")
                
            logger.info(f"Gemini successfully generated the new texture: {output_path}")

        except Exception as e:
            logger.error(f"Failed to generate texture via Gemini API: {e}")
            raise
