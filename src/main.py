from fileOrganizer import FileOrganizer
from consoleUI import ConsoleUI

def main ():
    organizer = FileOrganizer()
    console = ConsoleUI()

    files = organizer.listFiles()
    preview = organizer.getOrganizationPreview()

    console.showStartup(
        organizer.currentDirectory,
        files,
        preview
    )

    if not console.askConfirmation():
        console.showCanceledMessage()
        console.waitBeforeClose()
        return
    
    organizer.organizeFiles()

    console.showSuccessMessage()
    console.waitBeforeClose()

if __name__ == "__main__":
    main()