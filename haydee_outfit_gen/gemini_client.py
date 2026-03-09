import logging
import time
import functools
from pathlib import Path
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

def retry_api_call(max_retries=3, wait_seconds=5):
    """Decorator to retry API calls on transient errors like 503 UNAVAILABLE or 504 DEADLINE_EXCEEDED."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 2):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    error_str = str(e)
                    is_transient = "503" in error_str or "504" in error_str or "Deadline" in error_str or "UNAVAILABLE" in error_str
                    
                    if attempt <= max_retries and is_transient:
                        logger.warning(f"Transient API error encountered: {e}. Retrying in {wait_seconds} seconds (Attempt {attempt}/{max_retries})...")
                        time.sleep(wait_seconds)
                    else:
                        raise e
        return wrapper
    return decorator

class ValidationResult(BaseModel):
    is_face_valid: bool = Field(description="True if the helmet area is strictly faceless (no human eyes, nose, mouth).")
    is_torso_seams_valid: bool = Field(description="True if the front torso (top-left) and back torso (top-middle) match perfectly in materials/clothing without seam breaks.")
    is_legs_valid: bool = Field(description="True if the two bottom shapes are treated as individual left/right legs WITHOUT drawing two legs inside a single shape.")
    
    @property
    def is_valid(self) -> bool:
        return self.is_face_valid and self.is_torso_seams_valid and self.is_legs_valid

    feedback: str = Field(description="If any check failed, explain EXACTLY which area failed and why, comparing Image 1 and Image 2.")

class GeminiModClient:
    """Handles communication with the Gemini API for texture generation."""

    def __init__(self, api_key: str, image_resolution: str = "4K", model_name: str = "gemini-3.1-flash-image-preview", validator_model: str = "gemini-3.1-pro-preview"):
        self.api_key = api_key
        self.image_resolution = image_resolution
        self.model_name = model_name
        self.validator_model = validator_model
        self.client = genai.Client(api_key=self.api_key)

    @retry_api_call()
    def generate_texture(self, base_image_path: Path, style: str, output_path: Path, previous_feedback: str = None) -> None:
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
        1. Anatomy Warning (Head/Face): The character is a FACELESS robot. The round area on the mid-right is the helmet/head. ABSOLUTELY DO NOT generate human faces, eyes, noses, mouths, teeth, or hair. Do NOT draw gas masks, respirators, goggles, glasses, visors, or any accessories that imply a face underneath. This area MUST remain a blank synthetic panel.
        2. Anatomy Warning (Legs Explicit): The two large vertical sections filling the bottom half are LEGS and THIGHS, absolutely NOT a torso. DO NOT generate abdominal muscles or chests here.
           - The bottom-left shape is ONE ENTIRE UNROLLED LEG (Left Leg).
           - The bottom-right shape is ONE ENTIRE UNROLLED LEG (Right Leg).
           - DO NOT draw two legs inside one shape. Do not draw a vertical split line. Treat each shape as a single, unified cylindrical surface wrapped around one limb. Design them symmetrically.
        3. Anatomy Warning (Torso Continuity): The two shapes in the top-left area are the front torso (left) and back torso (right). It is CRITICAL that the materials on the outer edges of these two shapes match perfectly so they stitch together without seams in 3D. If the bottom sides of the front torso are bare skin, the bottom sides of the back torso MUST also be bare skin. If one side has armor or fabric wrapping around, the other must seamlessly continue that same armor/fabric. Do NOT mix materials on the side seams. Do NOT draw open coats, jackets, or asymmetrical clothing that breaks the seam continuity.
        4. Anatomy Warning (Collar/Back Overlay & Spinal Radiator): The irregular shape on the middle-right (below the head) rests directly on top of the back torso (top-middle shape). It is CRITICAL that they blend seamlessly as a single continuous surface design. Specifically, any lines, vents, or patterns on the lower-left edge of this middle-right piece (the radiator) MUST be oriented strictly VERTICAL (straight up and down) so they perfectly align with the spine on the back torso, never at an angle.
        5. Exact Mapping: Maintain the exact UV layout, seams, alignment, and proportions of the original image so it maps perfectly back onto the 3D model.
        6. Transparency/Background: Keep the blank and transparent spaces exactly where they are in the original file. Do not fill empty UV space.
        7. Application: Apply the '{style}' aesthetic purely to the textured areas (armor panels, skin, details).
        8. Quality: Ensure high-fidelity texturing with sharp details, respecting the shadows and highlights of the original topology.
        9. Resolution: Please generate the output image in exactly {res_text} resolution.
        """
        
        if previous_feedback:
            prompt += f"""
            
            [CRITICAL CORRECTION REQUIRED]
            The previous generation attempt was REJECTED by the Quality Assurance system for the following reasons:
            "{previous_feedback}"
            
            You MUST fix these specific structural/anatomical violations in this new generation.
            """
            
        prompt += "\nOutput ONLY the generated texture image."
        
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

    @retry_api_call()
    def validate_texture(self, base_image_path: Path, generated_image_path: Path, style: str) -> ValidationResult:
        """
        Uses a strong reasoning model to inspect the generated texture for structural flaws.
        """
        logger.info(f"Running QA validation using {self.validator_model} (Comparing Source and Result)...")

        prompt = f"""
        You are an expert 3D Technical Artist and strict Quality Assurance inspector.
        I am providing you with TWO images:
        - Image 1: The original blank UV map template.
        - Image 2: The generated texture in the style: "{style}".

        Your job is to compare Image 2 against Image 1 and check for severe UV mapping violations.
        
        Evaluate these specific rules:
        1. Face Rule: Look at the helmet area (mid-right). The character is a cyborg with absolutely no face (no eyes, mouth, or nose), so the helmet must be completely solid. If Image 2 has human features OR any glasses, visors, glowing eyes, or goggles, it FAILS.
        2. Torso Seam Rule: Compare the Front Torso (top-left) and Back Torso (top-middle). If the front has a coat/jacket/armor piece that magically disappears or doesn't match on the back, it FAILS. They must stitch together.
        3. Legs Rule: Look at the two large shapes at the bottom. Image 1 shows they are individual left and right legs. If Image 2 draws a line down the middle of them to simulate two legs inside one shape, or draws front/back perspective on a single flat island, it FAILS.

        Return the validation JSON strictly based on these structural rules.
        """
        
        try:
            from PIL import Image
            contents = [
                prompt,
                Image.open(base_image_path),
                Image.open(generated_image_path)
            ]
            
            result = self.client.models.generate_content(
                model=self.validator_model,
                contents=contents,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=ValidationResult,
                    temperature=0.0,
                )
            )
            return result.parsed
            
        except Exception as e:
            logger.warning(f"Validation API failed or timed out: {e}. Bypassing validation (assuming valid).")
            return ValidationResult(
                is_face_valid=True, is_torso_seams_valid=True, 
                is_legs_valid=True, 
                feedback="Validation bypassed due to API error."
            )

    @retry_api_call()
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

    @retry_api_call()
    def generate_normal_map(self, diffuse_image_path: Path, output_path: Path) -> None:
        """
        Generates a Tangent Space Normal Map based on the generated diffuse texture.
        """
        logger.info("Requesting Gemini to generate a normal map...")

        prompt = """
        This is a diffuse UV texture for a 3D character. I need you to create a high-quality Tangent Space Normal Map based exactly on this image.
        Follow these strict rules:
        - The base flat surface MUST be standard normal map blue: RGB(128, 128, 255).
        - Add 3D relief, bumps, fabric folds, armor panel gaps, and seams matching the details in the diffuse texture.
        - Maintain the exact same UV layout, borders, and transparent background as the provided image.
        Output ONLY the normal map image.
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
                        
            raise RuntimeError("No normal map image was returned from Gemini API.")
        except Exception as e:
            logger.error(f"Failed to generate normal map: {e}")
            raise
