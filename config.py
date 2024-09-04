# Текстовая конфигурация
WELCOME_MESSAGE = "Эта программа поможет вам установить все необходимое ПО для прохождения курса по Python от Easy Code"
BUTTON_TEXT_INSTALL = "Начать установку"
BUTTON_TEXT_FINISH = "Завершить установку"

# Графическая конфигурация
LOGO_PATH = "img/easy_code_logo.png"
ICON_PATH = "img/easy_code_icon.ico"

# URL для загрузки установщиков
INSTALLERS = {
    "python_win7": "https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe",  # Python 3.8 для Windows 7
    "python_win10_11": "https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe",  # Python 3.11.9 для Windows 10/11
    "vscode_win7": "https://update.code.visualstudio.com/1.70.0/win32-x64/stable",  # VS Code 1.70 для Windows 7
    "vscode_win10_11": "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64",  # Последняя версия VS Code для Windows 10/11
}
# Расширения VSCode и их URL
VSCODE_EXTENSIONS = {"ms-python.python","ms-vsliveshare.vsliveshare", "ms-vscode.live-server"}

# Пакеты Python
PYTHON_PACKAGES = ["requests", "pygame", "aiogram==2.25.2", "emoji", "Flask"]

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
