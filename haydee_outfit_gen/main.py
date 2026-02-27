import argparse
import logging
import sys
import tempfile
from pathlib import Path

from haydee_outfit_gen.config import Settings
from haydee_outfit_gen.image_processor import ImageProcessor
from haydee_outfit_gen.gemini_client import GeminiModClient
from haydee_outfit_gen.mod_builder import ModBuilder, MultiModBuilder

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Haydee Outfit Mod Generator via Gemini API")
    subparsers = parser.add_subparsers(dest="command")

    # --- Command: Generate (Одиночный мод) ---
    gen_parser = subparsers.add_parser("generate", help="Generate a new single outfit mod")
    gen_parser.add_argument("--name", type=str, required=True, help="Name of the mod (e.g., Synthwave)")
    gen_parser.add_argument("--style", type=str, required=True, help="Visual style description")
    gen_parser.add_argument("--author", type=str, help="Add author name info slot (e.g., 'kejdi')")

    # --- Command: Group (Мультимод) ---
    group_parser = subparsers.add_parser("group", help="Group multiple existing mods into a single multi-mod")
    group_parser.add_argument("--name", type=str, required=True, help="Name of the new multi-mod (e.g., Rainbow)")
    group_parser.add_argument("--mods", nargs='+', required=True, help="List of source mod names to group (e.g., red green blue)")
    group_parser.add_argument("--slot-category", type=str, default="color", help="Slot category name (default: color)")
    group_parser.add_argument("--author", type=str, help="Add author name info slot (e.g., 'kejdi')")
    group_parser.add_argument("--delete-sources", action="store_true", help="Delete source mods after successful grouping")

    # --- Логика обратной совместимости (Default Subcommand) ---
    argv = sys.argv[1:]
    
    # Если аргументов нет вообще, просто показываем справку
    if not argv:
        parser.print_help()
        sys.exit(1)
        
    # Если первый аргумент не является известной командой или флагом справки, 
    # предполагаем, что пользователь использует старый синтаксис (generate)
    if argv[0] not in ['generate', 'group', '-h', '--help']:
        argv.insert(0, 'generate')

    args = parser.parse_args(argv)

    # Initialize settings only for the CLI execution
    config = Settings()

    try:
        if args.command == "generate":
            # 1. Setup Mod Directory and Builder
            builder = ModBuilder(args.name, outfits_dir=config.outfits_dir, author=args.author)
            builder.prepare_directory()

            # 2. Process Original Texture
            base_dds = config.base_texture_path
            if not base_dds.exists():
                raise FileNotFoundError(f"Base texture not found at {base_dds}")

            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                base_png = temp_path / "base_Suit_D.png"
                generated_jpg = temp_path / "generated_Suit_D.jpg"

                # Convert base DDS to PNG for Gemini
                ImageProcessor.dds_to_png(base_dds, base_png)

                # 3. Generate New Texture via Gemini
                client = GeminiModClient(api_key=config.gemini_api_key, image_resolution=config.image_resolution)
                client.generate_texture(
                    base_image_path=base_png,
                    style=args.style,
                    output_path=generated_jpg
                )

                # 4. Convert Result back to DDS in the new mod folder
                final_dds_path = builder.mod_dir / "Suit_D.dds"
                ImageProcessor.img_to_dds(generated_jpg, final_dds_path, resolution=config.image_resolution)

            # 5. Generate Configuration Files
            builder.generate_mtl_file()
            builder.generate_outfit_file()

            logger.info(f"Mod '{args.name}' generated successfully! You can now test it in Haydee.")

        elif args.command == "group":
            builder = MultiModBuilder(
                multimod_name=args.name,
                source_mods=args.mods,
                outfits_dir=config.outfits_dir,
                slot_category=args.slot_category,
                author=args.author
            )
            builder.validate_sources()
            builder.prepare_directory()
            builder.migrate_assets_and_generate_mtls()
            builder.generate_outfit_file()
            
            if args.delete_sources:
                builder.cleanup_sources()
                
            logger.info(f"Multi-mod '{args.name}' created successfully from {len(args.mods)} variants!")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()
