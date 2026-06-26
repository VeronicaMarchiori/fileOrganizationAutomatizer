from pathlib import Path
import sys

IGNORED_FILES = [
    "README.md",
    ".gitignore",
    "requirements.txt",
    "desktop.ini",
    "Thumbs.db",
    ".DS_Store"
]

def shouldIgnoreFile(file: Path) -> bool:
    if file.name.lower() in [ignoredFile.lower() for ignoredFile in IGNORED_FILES]:
        return True
    if getattr(sys, "frozen", False):
        if file.name == Path(sys.executable).name:
            return True
    
    return False