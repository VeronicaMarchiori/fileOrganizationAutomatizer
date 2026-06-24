from pathlib import Path
from fileCategories import FILE_CATEGORIES
import sys


class FileOrganizer:
    def __init__(self):
        self.currentDirectory = self.getCurrentDirectory()
    
    def getFileCategory(self, extension: str) -> str:
        if not extension:
            return "NoExtension"
        
        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                return category
        
        return "Others"

    def createCategoryDirectory(self, category: str) -> Path:
        categoryDirectory = self.currentDirectory / category

        categoryDirectory.mkdir(exist_ok=True)

        return categoryDirectory

    def getCurrentDirectory(self) -> Path:
        if getattr(sys, "frozen", False):
            return Path(sys.executable).parent

        return Path(__file__).parent.parent

    def listFiles(self) -> list[Path]:
        return [
            item for item in self.currentDirectory.iterdir()
            if item.is_file()
        ]
    
    def getFileExtension(self, file: Path) -> str:
        return file.suffix.lower().replace(".", "")

    def showFiles(self):
        files = self.listFiles()

        print(f"Pasta analisada: {self.currentDirectory}")
        print(f"{len(files)} arquivo(s) encontrados:")

        for file in files:
            extension = self.getFileExtension(file)
            category = self.getFileCategory(extension)

            self.createCategoryDirectory(category)

            print(f"- {file.name} -> {extension} -> {category}" )
        