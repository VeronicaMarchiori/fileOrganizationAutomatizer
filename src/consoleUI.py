class ConsoleUI:
    def showHeader(self):
        print("=" * 50)
        print("     File Organization Automatizer")
        print("=" * 50)

    def showDirectory(self, directory):
        print(f"\nDiretório analisado:\n{directory}")
    
    def showFilesPreview(self, files):
        print (f"\nArquivos Encontrados: {len(files)}")

        for file in files:
            print(f"- {file.name}")

    def askConfirmation(self) -> bool:
        answer = input("\nDeseja organizar estes arquivos? [y/n]: ")
        return answer.lower() == "y"
    
    def showCanceledMessage(self):
        print("\nOperação cancelada.")
    
    def showSuccessMessage(self):
        print("\nOrganização concluída com sucesso!")
    
    def waitBeforeClose(self):
        input("\nPressione ENTER para fechar...")

    def showOrganizationPreview(self, preview: dict[str,int]):
        print("\nResumo da organização:")

        if not preview:
            print("Nenhum arquivo para organizar.")
            return
        
        for category, amount in preview.items():
            print(f"- {category}: {amount} arquivo(s)")

    def showStartup(self, directory, files, preview):
        self.showHeader()
        self.showDirectory(directory)
        self.showFilesPreview(files)
        self.showOrganizationPreview(preview)