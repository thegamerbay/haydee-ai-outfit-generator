import logging
from pathlib import Path
from google import genai
from google.genai import types

logger = logging.getLogger(__name__)

class GeminiModClient:
    """Handles communication with the Gemini API for texture generation."""

    def __init__(self, api_key: str, image_resolution: str = "4K", model_name: str = "gemini-3.1-flash-image-preview"):
        self.api_key = api_key
        self.image_resolution = image_resolution
        self.model_name = model_name
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
        1. Anatomy Warning (Head/Face): The character is a FACELESS robot. The round area on the mid-right is the helmet/head. ABSOLUTELY DO NOT generate human faces, eyes, noses, mouths, teeth, or hair. This area MUST remain a blank synthetic panel.
        2. Anatomy Warning (Legs): The two large vertical sections filling the bottom half of the image are the character's LEGS and THIGHS, absolutely NOT a torso. DO NOT generate abdominal muscles, chests, or torso armor on these lower sections. Treat them strictly as leg/thigh surfaces.
        3. Anatomy Warning (Torso Continuity): The two shapes in the top-left area are the front torso (left) and back torso (right). It is CRITICAL that the materials on the outer edges of these two shapes match perfectly so they stitch together without seams in 3D. If the bottom sides of the front torso are bare skin, the bottom sides of the back torso MUST also be bare skin. If one side has armor or fabric wrapping around, the other must seamlessly continue that same armor/fabric. Do NOT mix materials on the side seams.
        4. Anatomy Warning (Collar/Back Overlay & Spinal Radiator): The irregular shape on the middle-right (below the head) rests directly on top of the back torso (top-middle shape). It is CRITICAL that they blend seamlessly as a single continuous surface design. Specifically, any lines, vents, or patterns on the lower-left edge of this middle-right piece (the radiator) MUST be oriented strictly VERTICAL (straight up and down) so they perfectly align with the spine on the back torso, never at an angle.
        5. Exact Mapping: Maintain the exact UV layout, seams, alignment, and proportions of the original image so it maps perfectly back onto the 3D model.
        6. Transparency/Background: Keep the blank and transparent spaces exactly where they are in the original file. Do not fill empty UV space.
        7. Application: Apply the '{style}' aesthetic purely to the textured areas (armor panels, skin, details).
        8. Quality: Ensure high-fidelity texturing with sharp details, respecting the shadows and highlights of the original topology.
        9. Resolution: Please generate the output image in exactly {res_text} resolution.
        
        Output ONLY the generated texture image.
        """
        
        try:
            from PIL import Image
            
            contents = [
                prompt,
                Image.open(base_image_path)
            ]
            
            result = self.client.models.generate_content(
                model=self.model_name,
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

    def generate_material_mask(self, diffuse_image_path: Path, output_path: Path) -> None:
        """
        Generates a grayscale material mask based on the generated Suit_D.
        """
        logger.info("Requesting Gemini to generate a material mask...")

        prompt = """
        This is a diffuse UV texture for a 3D character. I need you to create a simple, flat GRAYSCALE material mask based exactly on this image.
        Follow these strict coloring rules:
        - Metallic, highly glossy armor, or shiny latex MUST be solid WHITE.
        - Bare skin MUST be solid MID-GRAY.
        - Matte fabrics, cloth, or dull surfaces MUST be solid BLACK.
        
        Do not add ANY lighting, shadows, or 3D shading. Keep it entirely flat.
        Maintain the exact same UV layout, borders, and transparent background as the provided image.
        Output ONLY the grayscale image.
        """
        
        try:
            from PIL import Image
            contents = [prompt, Image.open(diffuse_image_path)]
            
            result = self.client.models.generate_content(
                model=self.model_name,
                contents=contents,
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE'],
                    image_config=types.ImageConfig(
                        aspect_ratio="1:1",
                        image_size=self.image_resolution
                    )
                )
            )
            
            # Saving logic is similar to the generate_texture method
            saved = False
            if hasattr(result, 'candidates') and result.candidates:
                for candidate in result.candidates:
                    if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                        for part in candidate.content.parts:
                            if hasattr(part, 'image') and part.image:
                                with open(output_path, "wb") as f:
                                    f.write(part.image.image_bytes)
                                return
                            elif hasattr(part, 'inline_data') and part.inline_data:
                                with open(output_path, "wb") as f:
                                    f.write(part.inline_data.data)
                                return
            
            # Alternative fallback for direct parts
            if not saved and hasattr(result, 'parts') and result.parts:
                for part in result.parts:
                    if hasattr(part, 'image') and part.image:
                         with open(output_path, "wb") as f:
                            f.write(part.image.image_bytes)
                         return
                    elif hasattr(part, 'inline_data') and part.inline_data:
                         with open(output_path, "wb") as f:
                            f.write(part.inline_data.data)
                         return
                        
            raise RuntimeError("No mask image was returned from Gemini API.")
        except Exception as e:
            logger.error(f"Failed to generate material mask: {e}")
            raise
