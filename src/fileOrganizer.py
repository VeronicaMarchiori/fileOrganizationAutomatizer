import shutil
from pathlib import Path
from fileRules import shouldIgnoreFile
from systemSafety import isSafeDirectory
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

    def moveFile(self, file: Path, destinationDirectory: Path) -> tuple[bool, str]:
        try:
            destinationPath = destinationDirectory / file.name

            destinationPath = self.getAvailableDestinationPath(destinationPath)

            shutil.move(str(file), str(destinationPath))

            return True, ""

        except PermissionError:
            return False, "Permissão negada ou arquivo em uso."

        except OSError as error:
            return False, f"Erro do sistema: {error}"

        except Exception as error:
            return False, f"Erro inesperado: {error}"

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

            wasMoved, errorMessage = self.moveFile(file, destinationDirectory)

            if wasMoved:
                print(f"Movido: {file.name}")
            else: 
                print(f"Erro ao mover {file.name}: {errorMessage}")

    
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
    
    def getAvailableDestinationPath(self, destinationPath: Path) -> Path:
        if not destinationPath.exists():
            return destinationPath

        counter = 1

        while True:
            newFileName = f"{destinationPath.stem}_{counter}{destinationPath.suffix}"
            newDestinationPath = destinationPath.parent / newFileName

            if not newDestinationPath.exists():
                return newDestinationPath
            
            counter += 1