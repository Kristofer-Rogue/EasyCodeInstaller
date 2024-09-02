import logging
import os
import subprocess
from typing import Callable

import requests

import config


class Installer:
    def __init__(self, logger: logging.Logger, progress_callback: Callable[[float], None]) -> None:
        """
        Инициализация класса для установки программ.

        :param logger: Логгер для вывода сообщений.
        :param progress_callback: Коллбэк для обновления прогресс-бара.
        """
        self.logger = logger
        self.temp_dir = config.TEMP_DIR

        self.progress_callback = progress_callback

    def download_file(self, url: str, dest: str) -> None:
        """
        Скачивание файла по указанному URL.

        :param url: URL для загрузки.
        :param dest: Путь к месту сохранения файла.
        """
        self.logger.info(f"Скачивание {url} в {dest}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(dest, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        self.logger.info(f"Файл {dest} успешно загружен.")

    def install_python(self, installer_path: str) -> None:
        """
        Установка Python.

        :param installer_path: Путь к установщику Python.
        """
        self.logger.info("Установка Python...")
        subprocess.run(
            [installer_path] + config.INSTALL_SETTINGS["python_args"], check=True
        )
        self.logger.info("Python установлен.")

    def install_vscode(self, installer_path: str) -> None:
        """
        Установка VSCode.

        :param installer_path: Путь к установщику VSCode.
        """
        self.logger.info("Установка VSCode...")
        subprocess.run(
            [installer_path] + config.INSTALL_SETTINGS["vscode_args"], check=True
        )
        self.logger.info("VSCode установлен.")

    def install_python_packages(self) -> None:
        """
        Установка Python пакетов.
        """
        self.logger.info("Установка Python пакетов...")
        subprocess.run(
            ["py", "-m", "pip", "install"] + config.PYTHON_PACKAGES, check=True
        )
        self.logger.info("Пакеты установлены.")

    def install_vscode_extensions(self) -> None:
        """
        Установка расширений для VSCode.
        """
        self.logger.info("Установка расширений VSCode...")
        vscode_path = r"C:\Program Files\Microsoft VS Code\bin\code.cmd"
        subprocess.run(
            [vscode_path, "--install-extension", "ms-python.python", "--force"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.logger.info("Расширения VSCode установлены.")

    def start_installation(self) -> None:
        """
        Начало процесса установки.
        """
        os.makedirs(self.temp_dir, exist_ok=True)
        self.progress_callback(0.1)

        python_installer_path = os.path.join(self.temp_dir, "python_installer.exe")
        vscode_installer_path = os.path.join(self.temp_dir, "vscode_installer.exe")

        self.download_file(config.INSTALLERS["python"], python_installer_path)
        self.download_file(config.INSTALLERS["vscode"], vscode_installer_path)
        self.progress_callback(0.2)

        self.install_python(python_installer_path)
        self.progress_callback(0.4)
        self.install_vscode(vscode_installer_path)
        self.progress_callback(0.6)

        self.install_python_packages()
        self.progress_callback(0.8)
        self.install_vscode_extensions()
        self.progress_callback(1)
