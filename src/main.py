from fileOrganizer import FileOrganizer
from consoleUI import ConsoleUI
from backupManager import BackupManager
from systemSafety import isSafeDirectory

def main():
    organizer = FileOrganizer()
    console = ConsoleUI()
    backupManager = BackupManager()

    if not isSafeDirectory(organizer.currentDirectory):
        console.showHeader()
        console.showDirectory(organizer.currentDirectory)
        print("\nEssa pasta é protegida e não pode ser organizada.")
        console.waitBeforeClose()
        return

    files = organizer.listFiles()
    preview = organizer.getOrganizationPreview()

    if not files:
        console.showHeader()
        console.showDirectory(organizer.currentDirectory)
        print("\nNenhum arquivo encontrado para organizar.")
        console.waitBeforeClose()
        return

    console.showStartup(
        organizer.currentDirectory,
        files,
        preview
    )

    if not console.askConfirmation():
        console.showCanceledMessage()
        console.waitBeforeClose()
        return
    
    if console.askBackup():
        wasCreated, errorMessage, backupDirectory = backupManager.createBackup(
            organizer.currentDirectory
        )

        if wasCreated:
            print(f"\nBackup criado em: {backupDirectory}")
        else:
            print(f"\nErro ao criar backup: {errorMessage}")
            console.waitBeforeClose()
            return

    organizer.organizeFiles()

    console.showSuccessMessage()
    console.waitBeforeClose()

if __name__ == "__main__":
    main()