# URL для загрузки установщиков
INSTALLERS = {
    "python": "https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe",
    "vscode": "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64",
}

# Расширения VSCode и их URL
VSCODE_EXTENSIONS = {"ms-python.python"}

# Пакеты Python
PYTHON_PACKAGES = ["requests", "pygame", "aiogram==2.25.2"]

# Путь для временного хранения скачанных файлов
TEMP_DIR = "temp_downloads"

INSTALL_PATHES = {
    "python": r"C:\Program Files\Python311",
    "vscode": r"C:\Program Files\Microsoft VS Code",
}

# Настройки установки
INSTALL_SETTINGS = {
    "python_args": [
        "/quiet",
        "InstallAllUsers=0",
        f'InstallPath={INSTALL_PATHES["python"]}',
        "PrependPath=1",
    ],
    "vscode_args": [
        "/VERYSILENT",
        f"/dir={INSTALL_PATHES['vscode']}",
        "/MERGETASKS=desktopicon,quicklaunchicon,!runcode",
    ],
}
