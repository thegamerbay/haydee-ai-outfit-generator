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

    # --- Command: Generate (Single mod) ---
    gen_parser = subparsers.add_parser("generate", help="Generate a new single outfit mod")
    gen_parser.add_argument("--name", type=str, required=True, help="Name of the mod (e.g., Synthwave)")
    gen_parser.add_argument("--style", type=str, help="Visual style description (required unless --skip-d is used)")
    gen_parser.add_argument("--author", type=str, help="Add author name info slot (e.g., 'kejdi')")
    gen_parser.add_argument("--skip-d", action="store_true", help="Skip generation of Suit_D (diffuse map)")
    gen_parser.add_argument("--skip-s", action="store_true", help="Skip generation of Suit_S (specular map)")
    gen_parser.add_argument("--skip-n", action="store_true", help="Skip generation of Suit_N (normal map)")

    # --- Command: Group (Multi-mod) ---
    group_parser = subparsers.add_parser("group", help="Group multiple existing mods into a single multi-mod")
    group_parser.add_argument("--name", type=str, required=True, help="Name of the new multi-mod (e.g., Rainbow)")
    group_parser.add_argument("--mods", nargs='+', required=True, help="List of source mod names to group (e.g., red green blue)")
    group_parser.add_argument("--slot-category", type=str, default="color", help="Slot category name (default: color)")
    group_parser.add_argument("--author", type=str, help="Add author name info slot (e.g., 'kejdi')")
    group_parser.add_argument("--delete-sources", action="store_true", help="Delete source mods after successful grouping")

    # --- Backward compatibility logic (Default Subcommand) ---
    argv = sys.argv[1:]
    
    # If there are no arguments at all, just show help
    if not argv:
        parser.print_help()
        sys.exit(1)
        
    # If the first argument is not a known command or help flag, 
    # assume the user is using the old syntax (generate)
    if argv[0] not in ['generate', 'group', '-h', '--help']:
        argv.insert(0, 'generate')

    args = parser.parse_args(argv)

    # Initialize settings only for the CLI execution
    config = Settings()

    try:
        if args.command == "generate":
            if not getattr(args, "skip_d", False) and not args.style:
                parser.error("argument --style is required unless --skip-d is used")

            # 1. Setup Mod Directory and Builder
            is_partial = getattr(args, "skip_d", False)
            builder = ModBuilder(args.name, outfits_dir=config.outfits_dir, author=args.author)
            builder.prepare_directory(clear_dir=not is_partial)

            # 2. Process Original Texture
            base_dds = config.base_texture_path
            if not base_dds.exists():
                raise FileNotFoundError(f"Base texture not found at {base_dds}")

            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                base_png = temp_path / "base_Suit_D.png"
                generated_d_png = temp_path / "generated_Suit_D.png"
                generated_mask = temp_path / "material_mask.png"
                generated_n_png = temp_path / "generated_normal.png"

                client = GeminiModClient(
                    api_key=config.gemini_api_key, 
                    image_resolution=config.image_resolution,
                    model_name=config.model_name
                )
                
                final_d_dds = builder.mod_dir / "Suit_D.dds"

                if not args.skip_d:
                    # 1. Convert base DDS to PNG
                    ImageProcessor.dds_to_png(base_dds, base_png)

                    # 2. Generate Suit_D New Texture
                    client.generate_texture(
                        base_image_path=base_png,
                        style=args.style,
                        output_path=generated_d_png
                    )

                    # 3. Save Diffuse as DDS
                    ImageProcessor.img_to_dds(generated_d_png, final_d_dds, resolution=config.image_resolution)
                else:
                    if not final_d_dds.exists():
                        if not args.skip_s or not args.skip_n:
                            raise FileNotFoundError(
                                f"Cannot generate Suit_S or Suit_N because Suit_D generation was skipped and {final_d_dds.name} does not exist from previous runs."
                            )
                    else:
                        if not args.skip_s or not args.skip_n:
                            ImageProcessor.dds_to_png(final_d_dds, generated_d_png)

                if not args.skip_s:
                    # 4. Generate Material Mask
                    client.generate_material_mask(
                        diffuse_image_path=generated_d_png,
                        output_path=generated_mask
                    )

                    # 5. Pack and Save Specular as DDS
                    final_s_dds = builder.mod_dir / "Suit_S.dds"
                    ImageProcessor.create_specular_map(generated_mask, final_s_dds, resolution=config.image_resolution)

                if not args.skip_n:
                    # 6. Generate Custom Normal Map
                    client.generate_normal_map(
                        diffuse_image_path=generated_d_png,
                        output_path=generated_n_png
                    )
                    
                    # 7. Save Custom Normal as DDS
                    final_n_dds = builder.mod_dir / "Suit_N.dds"
                    ImageProcessor.create_custom_normal_map(generated_n_png, final_n_dds, resolution=config.image_resolution)

            # 8. Generate Configuration Files
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
            
            # Since all variants use flat normals and speculars, we can just grab them from one of the source mods,
            # or regenerate a shared flat normal map for the grouped mod.
            final_n_dds = builder.mod_dir / "Suit_N.dds"
            ImageProcessor.create_neutral_normal_map(final_n_dds, resolution=config.image_resolution)
            
            builder.generate_outfit_file()
            
            if args.delete_sources:
                builder.cleanup_sources()
                
            logger.info(f"Multi-mod '{args.name}' created successfully from {len(args.mods)} variants!")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()
