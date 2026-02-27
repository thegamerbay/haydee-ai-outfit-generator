import logging
from pathlib import Path
from google import genai
from google.genai import types

logger = logging.getLogger(__name__)

class GeminiModClient:
    """Handles communication with the Gemini API for texture generation."""

    def __init__(self, api_key: str, image_resolution: str = "4K"):
        self.api_key = api_key
        self.image_resolution = image_resolution
        self.client = genai.Client(api_key=self.api_key)

    def generate_texture(self, base_image_path: Path, style: str, output_path: Path) -> None:
        """
        Sends the base texture and prompt to Gemini to generate a new texture.
        """
        logger.info(f"Requesting Gemini to generate texture in style: '{style}'...")

        res_text = "4096x4096 (4K)" if self.image_resolution == "4K" else "2048x2048 (2K)"

        # Enhanced prompt tailored to the character's cybernetic/biomechanical nature
        prompt = f"""
        Attached is a UV map texture for the 3D character model 'Haydee'. 
        The character is a biomechanical humanoid with distinct segmented armor plates, synthetic skin, and specific anatomical proportions.

        I need you to completely transform the visual theme of this texture into: {style}.

        CRITICAL INSTRUCTIONS:
        1. Anatomy Warning (Legs): The two large vertical sections filling the bottom half of the image are the character's LEGS and THIGHS, absolutely NOT a torso. DO NOT generate abdominal muscles, chests, or torso armor on these lower sections. Treat them strictly as leg/thigh surfaces.
        2. Anatomy Warning (Head/Face): The character is a FACELESS robot. The round area on the mid-right is the helmet/head. ABSOLUTELY DO NOT generate human faces, eyes, noses, mouths, teeth, or hair. This area MUST remain a blank synthetic panel.
        3. Anatomy Warning (Torso Continuity): The two shapes in the top-left area are the front torso (left) and back torso (right). It is CRITICAL that the materials on the outer edges of these two shapes match perfectly so they stitch together without seams in 3D. If the bottom sides of the front torso are bare skin, the bottom sides of the back torso MUST also be bare skin. If one side has armor or fabric wrapping around, the other must seamlessly continue that same armor/fabric. Do NOT mix materials on the side seams.
        4. Exact Mapping: Maintain the exact UV layout, seams, alignment, and proportions of the original image so it maps perfectly back onto the 3D model.
        5. Transparency/Background: Keep the blank and transparent spaces exactly where they are in the original file. Do not fill empty UV space.
        6. Application: Apply the '{style}' aesthetic purely to the textured areas (armor panels, skin, details).
        7. Quality: Ensure high-fidelity texturing with sharp details, respecting the shadows and highlights of the original topology.
        8. Resolution: Please generate the output image in exactly {res_text} resolution.
        
        Output ONLY the generated texture image.
        """
        
        try:
            from PIL import Image
            
            contents = [
                prompt,
                Image.open(base_image_path)
            ]
            
            result = self.client.models.generate_content(
                model='gemini-3.1-flash-image-preview',
                contents=contents,
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE'],
                    image_config=types.ImageConfig(
                        aspect_ratio="1:1",
                        image_size=self.image_resolution
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
                    
                    expected_res = 4096 if self.image_resolution == "4K" else 2048
                    if width != expected_res or height != expected_res:
                        raise ValueError(f"Generated image resolution ({width}x{height}) does not match expected {self.image_resolution} ({expected_res}x{expected_res}).")
            except ValueError:
                raise
            except Exception as e:
                logger.warning(f"Could not determine generated image resolution: {e}")
                
            logger.info(f"Gemini successfully generated the new texture: {output_path}")

        except Exception as e:
            logger.error(f"Failed to generate texture via Gemini API: {e}")
            raise
