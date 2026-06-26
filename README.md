# 📂 File Organization Automatizer

Automatically organize your files into categorized folders with optional backup creation.

## ✨ Features

- 📁 Organizes files by category based on their extension.
- 💾 Optional backup before organizing.
- 🔒 Prevents overwriting duplicate files.
- 🛡️ Protects system and development directories.
- 🚫 Ignores the executable and project-related files.
- ⚠️ Handles common file operation errors safely.

---

## 📥 Download

You don't need Python installed to use this application.

1. Go to the **Releases** page.
2. Download the latest version of **FileOrganizationAutomatizer.exe**.
3. Place the executable inside the folder you want to organize.
4. Double-click the executable and follow the instructions.

---

## 🚀 How It Works

The application will:

1. Analyze the current folder.
2. Display all detected files.
3. Show a summary of the organization.
4. Ask whether you want to create a backup.
5. Organize the files into categorized folders.

Example:

```
Documents/
Images/
Videos/
Archives/
Design Projects/
Others/
```

---

## 💾 Backup

If you choose to create a backup, the application creates a complete copy of the folder before organizing it.

Example:

```
Downloads_backup_2026-06-25_18-42-15
```

---

## 🔐 Safety Features

- Prevents organizing Windows system folders.
- Prevents organizing development project folders.
- Prevents organizing backup folders.
- Prevents duplicate file overwriting.
- Ignores the executable itself.

---

## 🛠️ Technologies

- Python
- PyInstaller
- pathlib
- shutil

---

## 📦 Build

Clone the repository:

```bash
git clone https://github.com/VeronicaMarchiori/fileOrganizationAutomatizer.git
```

Install PyInstaller:

```bash
pip install pyinstaller
```

Generate the executable:

```bash
python -m PyInstaller --onefile --console --name FileOrganizationAutomatizer src/main.py
```

---

## 🤝 Contributing

Suggestions and improvements are always welcome!

Feel free to open an Issue or submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.
