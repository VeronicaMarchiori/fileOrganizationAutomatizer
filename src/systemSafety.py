from pathlib import Path


BLOCKED_DIRECTORY_NAMES = [
    "Windows",
    "System32",
    "Program Files",
    "Program Files (x86)"
]

PROJECT_DIRECTORY_NAMES = [
    "src",
    ".git",
    ".venv",
    "venv"
]

def isBackupDirectory(directory: Path) -> bool:
    return "_backup_" in directory.name.lower()


def isSafeDirectory(directory: Path) -> bool:
    if isBackupDirectory(directory):
        return False

    directoryParts = [part.lower() for part in directory.parts]

    for blockedDirectory in BLOCKED_DIRECTORY_NAMES:
        if blockedDirectory.lower() in directoryParts:
            return False

    for item in directory.iterdir():
        if item.is_dir() and item.namelower() in PROJECT_DIRECTORY_NAMES:
            return False
        
    return True