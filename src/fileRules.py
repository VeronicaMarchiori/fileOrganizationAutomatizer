from pathlib import Path
import sys

IGNORED_FILES = [
    "README.md",
    ".gitignore",
    "requirements.txt"
]

def shouldIgnoreFile(file: Path) -> bool:
    if file.name  in IGNORED_FILES:
        return True
    if getattr(sys, "frozen", False):
        if file.name == Path(sys.executable).name:
            return True
    
    return False