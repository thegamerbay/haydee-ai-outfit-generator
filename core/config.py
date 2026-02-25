import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    gemini_api_key: str
    haydee_path: Path
    image_resolution: str = "4K"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def outfits_dir(self) -> Path:
        return self.haydee_path / "Outfits"

    @property
    def base_texture_path(self) -> Path:
        return self.outfits_dir / "Haydee" / "Suit_D.dds"

settings = Settings()
