from pathlib import Path

BLOCKED_DIRECTORY_NAMES = [
    "Windows",
    "System32",
    "Program Files",
    "Program Files(x86)"
]

def isSafeDirectory(directory: Path) -> bool:
    directoryParts = [part.lower() for part in directory.parts]

    for blockedDirectory in BLOCKED_DIRECTORY_NAMES:
        if blockedDirectory.lower() in directoryParts:
            return False
    return True