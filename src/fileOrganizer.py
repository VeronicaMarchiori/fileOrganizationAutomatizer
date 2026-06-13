from pathlib import Path
import sys


class FileOrganizer:
    def __init__(self):
        self.currentDirectory = self.getCurrentDirectory()

    def getCurrentDirectory(self) -> Path:
        if getattr(sys, "frozen", False):
            return Path(sys.executable).parent

        return Path(__file__).parent.parent

    def listFiles(self) -> list[Path]:
        return [
            item for item in self.currentDirectory.iterdir()
            if item.is_file()
        ]

    def showFiles(self):
        files = self.listFiles()

        print(f"Pasta analisada: {self.currentDirectory}")
        print(f"{len(files)} arquivo(s) encontrados:")

        for file in files:
            print(f"- {file.name}")