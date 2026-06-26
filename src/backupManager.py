from pathlib import Path
from datetime import datetime
import shutil
from fileRules import shouldIgnoreFile


class BackupManager:
    def createBackup(self, sourceDirectory: Path) -> tuple[bool, str, Path | None]:
        if "_backup_" in sourceDirectory.name.lower():
            return False, "Não é permitido criar backup de outro backup.", None

        try:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            backupDirectory = (
                sourceDirectory.parent
                / f"{sourceDirectory.name}_backup_{timestamp}"
            )

            backupDirectory.mkdir()

            for item in sourceDirectory.iterdir():
                if item.is_file():
                    if shouldIgnoreFile(item):
                        continue

                    shutil.copy2(item, backupDirectory / item.name)

                elif item.is_dir():
                    shutil.copytree(item, backupDirectory / item.name)

            return True, "", backupDirectory

        except PermissionError:
            return False, "Permissão negada ao criar backup.", None

        except OSError as error:
            return False, f"Erro do sistema ao criar backup: {error}", None

        except Exception as error:
            return False, f"Erro inesperado ao criar backup: {error}", None