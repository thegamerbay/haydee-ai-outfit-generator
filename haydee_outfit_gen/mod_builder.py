import os
import shutil
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class ModBuilder:
    """Handles the creation of directories and mod configuration files."""

    def __init__(self, mod_name: str, outfits_dir: Path, author: str = None):
        if mod_name.strip().lower() == "haydee":
            raise ValueError("Mod name cannot be 'Haydee'. This protects the system outfit.")
        
        self.mod_name = mod_name.strip()
        self.author = author
        self.outfits_dir = outfits_dir
        self.mod_dir = self.outfits_dir / self.mod_name

    def prepare_directory(self) -> None:
        """Creates the mod directory, overwriting if it already exists."""
        if self.mod_dir.exists():
            logger.warning(f"Mod directory '{self.mod_name}' already exists. Overwriting...")
            shutil.rmtree(self.mod_dir)
        
        self.mod_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created directory: {self.mod_dir}")

    def generate_mtl_file(self) -> None:
        """Generates the .mtl material mapping file."""
        mtl_content = f"""HD_DATA_TXT 300
material
{{
	type OPAQUE;
	twoSided false;
	width 64.0;
	height 64.0;
	normalMap "Outfits\\{self.mod_name}\\Suit_N.dds";
	diffuseMap "Outfits\\{self.mod_name}\\Suit_D.dds";
	specularMap "Outfits\\{self.mod_name}\\Suit_S.dds";
	speculars 1.0 2.0 0.0;
	surface Default;
}}
"""
        mtl_path = self.mod_dir / "Suit.mtl"
        mtl_path.write_text(mtl_content, encoding="utf-8")
        logger.info(f"Generated {mtl_path.name}")

    def generate_outfit_file(self) -> None:
        """Generates the .outfit configuration file."""
        author_slot = f'\n\t\tslot\t\t"mod by" "{self.author}";' if self.author else ""
        
        outfit_content = f"""HD_DATA_TXT 300

outfit
{{
	name			"{self.mod_name}";
	default			false;

	mesh
	{{
		mesh		"Outfits\\Haydee\\Suit.mesh";
		skin		"Outfits\\Haydee\\Suit.skin";
		material	"Outfits\\{self.mod_name}\\Suit.mtl";

		common		true;
		mask		true;
		visor		true;
		jacket		true;
	}}

	mesh
	{{
		mesh		"Outfits\\Haydee\\Helmet.mesh";
		skin		"Outfits\\Haydee\\Helmet.skin";
		material	"Outfits\\{self.mod_name}\\Suit.mtl";

		common		true;
		mask		true;
		visor		true;
		jacket		true;
		
		slot		"Head" "Haydee";
	}}
	
	mesh
	{{
		mesh		"Outfits\\Haydee\\Hands.mesh";
		skin		"Outfits\\Haydee\\Hands.skin";
		material	"Outfits\\{self.mod_name}\\Suit.mtl";

		common		true;
		mask		true;
		visor		true;
		jacket		true;

		slot		"Hands" "Haydee";
	}}

	mesh
	{{
		mesh		"Outfits\\Haydee\\Clock.mesh";
		skin		"Outfits\\Haydee\\Clock.skin";

		clock		true;

		common		true;
		mask		true;
		visor		true;
		jacket		true;
	}}

	mesh
	{{
		mesh		"Outfits\\Haydee\\MaskRobo.mesh";
		skin		"Outfits\\Haydee\\MaskRobo.skin";
		material	"Outfits\\Haydee\\MaskRobo.mtl";

		mask		true;
	}}

	mesh
	{{
		mesh		"Outfits\\Haydee\\Visor.mesh";
		skin		"Outfits\\Haydee\\Visor.skin";
		material	"Items\\Visor\\Visor.mtl";

		visor		true;
	}}
	
	mesh
	{{
		mesh		"Outfits\\Haydee\\Vest.mesh";
		skin		"Outfits\\Haydee\\Vest.skin";
		material	"Outfits\\Haydee\\Vest.mtl";

		common		false;
		mask		false;
		visor		false;
		jacket		true;{author_slot}
	}}

	ragdoll
	{{
		common		true;
		mask		true;
		visor		true;
		jacket		true;

		ragdoll		"Outfits\\Haydee\\Haydee.doll";
	}}
}}
"""
        outfit_path = self.outfits_dir / f"{self.mod_name}.outfit"
        outfit_path.write_text(outfit_content, encoding="utf-8")
        logger.info(f"Generated {outfit_path.name}")


class MultiModBuilder:
    """Handles grouping of multiple generated mods into a single multi-variant outfit."""

    def __init__(self, multimod_name: str, source_mods: list[str], outfits_dir: Path, slot_category: str = "variant", author: str = None):
        if multimod_name.strip().lower() == "haydee":
            raise ValueError("Multi-mod name cannot be 'Haydee'. This protects the system outfit.")
        
        self.multimod_name = multimod_name.strip()
        self.source_mods = [m.strip() for m in source_mods]
        self.slot_category = slot_category
        self.author = author
        self.outfits_dir = outfits_dir
        self.mod_dir = self.outfits_dir / self.multimod_name

    def validate_sources(self) -> None:
        """Checks that all source mods exist and are not system protected."""
        for mod in self.source_mods:
            if mod.lower() == "haydee":
                raise ValueError(f"Cannot group the system 'Haydee' mod. Please remove it from the list.")
            
            mod_path = self.outfits_dir / mod
            if not mod_path.exists():
                raise FileNotFoundError(f"Source mod '{mod}' not found in {self.outfits_dir}.")
            
            dds_path = mod_path / "Suit_D.dds"
            if not dds_path.exists():
                raise FileNotFoundError(f"Texture file not found in source mod: {dds_path}")

    def prepare_directory(self) -> None:
        """Creates the multi-mod directory."""
        if self.mod_dir.exists():
            logger.warning(f"Multi-mod directory '{self.multimod_name}' already exists. Overwriting...")
            shutil.rmtree(self.mod_dir)
        
        self.mod_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created multi-mod directory: {self.mod_dir}")

    def migrate_assets_and_generate_mtls(self) -> None:
        """Copies textures from source mods and generates an MTL for each variant."""
        for mod in self.source_mods:
            # Copy texture and rename it to {mod}_d.dds to prevent collisions
            src_dds = self.outfits_dir / mod / "Suit_D.dds"
            dst_dds = self.mod_dir / f"{mod}_d.dds"
            shutil.copy2(src_dds, dst_dds)
            
            # Copy mask/specular texture and rename it to {mod}_s.dds to prevent collisions
            src_s_dds = self.outfits_dir / mod / "Suit_S.dds"
            dst_s_dds = self.mod_dir / f"{mod}_s.dds"
            # Fallback for old mods that might not have a Suit_S generated
            if src_s_dds.exists():
                shutil.copy2(src_s_dds, dst_s_dds)
            
            # Generate MTL file for this specific variant
            mtl_content = f"""HD_DATA_TXT 300
material
{{
	type OPAQUE;
	twoSided false;
	width 64.0;
	height 64.0;
	normalMap "Outfits\\{self.multimod_name}\\Suit_N.dds";
	diffuseMap "Outfits\\{self.multimod_name}\\{mod}_d.dds";
	specularMap "Outfits\\{self.multimod_name}\\{mod}_s.dds";
	speculars 1.0 2.0 0.0;
	surface Default;
}}
"""
            mtl_path = self.mod_dir / f"{mod}.mtl"
            mtl_path.write_text(mtl_content, encoding="utf-8")
            logger.info(f"Migrated texture and generated {mtl_path.name}")

    def generate_outfit_file(self) -> None:
        """Generates the main .outfit file grouping all variants."""
        outfit_path = self.outfits_dir / f"{self.multimod_name}.outfit"
        
        author_slot = f'\n\t\tslot\t\t"mod by" "{self.author}";' if self.author else ""
        
        lines = [
            "HD_DATA_TXT 300\n",
            "outfit\n{",
            f'\tname\t\t\t"{self.multimod_name}";',
            "\tdefault\t\t\tfalse;\n",
            # Add a common Vest mesh with the author slot, like in your example
            f"""\tmesh
\t{{
\t\tmesh\t\t"Outfits\\Haydee\\Vest.mesh";
\t\tskin\t\t"Outfits\\Haydee\\Vest.skin";
\t\tmaterial\t"Outfits\\Haydee\\Vest.mtl";

\t\tcommon\t\tfalse;
\t\tmask\t\tfalse;
\t\tvisor\t\tfalse;
\t\tjacket\t\ttrue;{author_slot}
\t}}\n"""
        ]

        # Add Helmet, Hands, and Suit blocks for each mod variant
        for mod in self.source_mods:
            variant_block = f"""\tmesh
\t{{
\t\tmesh\t\t"Outfits\\Haydee\\Helmet.mesh";
\t\tskin\t\t"Outfits\\Haydee\\Helmet.skin";
\t\tmaterial\t"Outfits\\{self.multimod_name}\\{mod}.mtl";

\t\tcommon\t\ttrue;
\t\tmask\t\ttrue;
\t\tvisor\t\ttrue;
\t\tjacket\t\ttrue;
\t\t
\t\tslot\t\t"{self.slot_category}" "{mod}";
\t}}
\t
\tmesh
\t{{
\t\tmesh\t\t"Outfits\\Haydee\\Hands.mesh";
\t\tskin\t\t"Outfits\\Haydee\\Hands.skin";
\t\tmaterial\t"Outfits\\{self.multimod_name}\\{mod}.mtl";

\t\tcommon\t\ttrue;
\t\tmask\t\ttrue;
\t\tvisor\t\ttrue;
\t\tjacket\t\ttrue;

\t\tslot\t\t"{self.slot_category}" "{mod}";
\t}}
\t
\tmesh
\t{{
\t\tmesh\t\t"Outfits\\Haydee\\Suit.mesh";
\t\tskin\t\t"Outfits\\Haydee\\Suit.skin";
\t\tmaterial\t"Outfits\\{self.multimod_name}\\{mod}.mtl";

\t\tcommon\t\ttrue;
\t\tmask\t\ttrue;
\t\tvisor\t\ttrue;
\t\tjacket\t\ttrue;

\t\tslot\t\t"{self.slot_category}" "{mod}";
\t}}\n"""
            lines.append(variant_block)

        # Add remaining common game elements
        common_elements = """\tmesh
\t{
\t\tmesh\t\t"Outfits\\Haydee\\Clock.mesh";
\t\tskin\t\t"Outfits\\Haydee\\Clock.skin";

\t\tclock		true;

\t\tcommon		true;
\t\tmask		true;
\t\tvisor		true;
\t\tjacket		true;
\t}

\tmesh
\t{
\t\tmesh\t\t"Outfits\\Haydee\\MaskRobo.mesh";
\t\tskin\t\t"Outfits\\Haydee\\MaskRobo.skin";
\t\tmaterial\t"Outfits\\Haydee\\MaskRobo.mtl";

\t\tmask		true;
\t}

\tmesh
\t{
\t\tmesh\t\t"Outfits\\Haydee\\Visor.mesh";
\t\tskin\t\t"Outfits\\Haydee\\Visor.skin";
\t\tmaterial\t"Items\\Visor\\Visor.mtl";

\t\tvisor		true;
\t}

\tragdoll
\t{
\t\tcommon		true;
\t\tmask		true;
\t\tvisor		true;
\t\tjacket		true;

\t\tragdoll		"Outfits\\Haydee\\Haydee.doll";
\t}
}"""
        lines.append(common_elements)
        outfit_path.write_text("\n".join(lines), encoding="utf-8")
        logger.info(f"Generated multi-mod config {outfit_path.name}")

    def cleanup_sources(self) -> None:
        """Deletes original mod folders and files if requested."""
        for mod in self.source_mods:
            mod_path = self.outfits_dir / mod
            if mod_path.exists():
                shutil.rmtree(mod_path)
            
            outfit_file = self.outfits_dir / f"{mod}.outfit"
            if outfit_file.exists():
                outfit_file.unlink()
                
            logger.info(f"Deleted source mod: {mod}")
