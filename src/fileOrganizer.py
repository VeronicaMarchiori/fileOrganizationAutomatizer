import shutil
from pathlib import Path
from fileRules import shouldIgnoreFile
from systemSafety import isSafeDirectory
from fileCategories import FILE_CATEGORIES
from fileRules import shouldIgnoreFile
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

    def moveFile(self, file: Path, destinationDirectory: Path):
        destinationPath = destinationDirectory / file.name

        shutil.move(str(file), str(destinationPath))

    def createCategoryDirectory(self, category: str) -> Path:
        categoryDirectory = self.currentDirectory / category

        categoryDirectory.mkdir(exist_ok=True)

        return categoryDirectory

    def getCurrentDirectory(self) -> Path:
        if getattr(sys, "frozen", False):
            return Path(__file__).parent

        return Path(__file__).parent.parent / "testFolder"

    def listFiles(self) -> list[Path]:
        return [
            item for item in self.currentDirectory.iterdir()
            if item.is_file()
        ]
    
    def getFileExtension(self, file: Path) -> str:
        return file.suffix.lower().replace(".", "")

    def organizeFiles(self):
        if not isSafeDirectory(self.currentDirectory):
            print("Essa pasta é protegida e não pode ser organizada.")
            return
        
        files = self.listFiles()

        for file in files:
            if shouldIgnoreFile(file):
                continue

            extension = self.getFileExtension(file)
            category = self.getFileCategory(extension)

            destinationDirectory = self.createCategoryDirectory(category)

            self.moveFile(file, destinationDirectory)
    
    def getOrganizationPreview(self) -> dict[str, int]:
        preview = {}
        files = self.listFiles()

        for file in files:
            if shouldIgnoreFile(file):
                continue
            extension = self.getFileExtension(file)
            category = self.getFileCategory(extension)

            preview[category] = preview.get(category,0) + 1
        return preview


    def showFiles(self):
        files = self.listFiles()

        print(f"Pasta Analisada: {self.currentDirectory}")
        print(f"{len(files)} arquivo(s) encontrados")
    
        for file in files:
            extension = self.getFileExtension(file)
            category = self.getFileCategory(extension)
        
        print(f"- {file.name} -> {extension} -> {category}")