import os

from pathlib import Path


BASE_DIR = Path(os.path.dirname(__file__)) / "../.."
IMAGES_DIR = BASE_DIR / "images"

__all__ = ["BASE_DIR", "IMAGES_DIR"]
