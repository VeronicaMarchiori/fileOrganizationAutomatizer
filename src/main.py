from pathlib import Path
import sys

def getCurrentDirectory() -> Path:
    if  getattr(sys,"frozen", False):
        return path(sys.executable).parent
    
    return(__file__).parent.parent

def listFiles(directory: Path) -> list[Path]:
    return [item for item in directory.iterdir() if item.is_file()]

def main():
    currentDirectory = getCurrentDirectory()
    files = listFiles(currentDirectory)

    print(f"Pasta analisada: {currentDirectory}")
    print(f"{len(files)} arquivo(s) encontrados:")

    for file in files:
        print(f"- {file.name}")

if __name__ == "__main__":
    main()
    