import os
import subprocess
import requests
import config


class Installer:
    def __init__(self) -> None:
        """
        Инициализация класса для установки программ.
        """
        self.temp_dir = config.TEMP_DIR
        os.makedirs(self.temp_dir, exist_ok=True)

    def download_file(self, url: str, dest: str) -> None:
        """
        Загрузка файла по указанному URL.

        :param url: URL для загрузки.
        :param dest: Путь к месту сохранения файла.
        """
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(dest, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    def install_python(self, installer_path: str) -> None:
        """
        Установка Python.

        :param installer_path: Путь к установщику Python.
        """
        subprocess.run(
            [installer_path] + config.INSTALL_SETTINGS["python_args"], check=True
        )

    def install_vscode(self, installer_path: str) -> None:
        """
        Установка VSCode.

        :param installer_path: Путь к установщику VSCode.
        """
        subprocess.run(
            [installer_path] + config.INSTALL_SETTINGS["vscode_args"], check=True
        )

    def install_python_packages(self) -> None:
        """
        Установка Python пакетов.
        """
        subprocess.run(
            ["py", "-m", "pip", "install"] + config.PYTHON_PACKAGES, check=True
        )

    def install_vscode_extensions(self) -> None:
        """
        Установка расширений для VSCode.
        """
        vscode_path = r"C:\Program Files\Microsoft VS Code\bin\code.cmd"
        subprocess.run(
            [vscode_path, "--install-extension", "ms-python.python", "--force"],
            capture_output=True,
            text=True,
            check=True,
        )

    def get_temp_file_path(self, name: str) -> str:
        """
        Получение пути к временному файлу.

        :param name: Имя файла.
        :return: Путь к временному файлу.
        """
        return os.path.join(self.temp_dir, name)

    def start_installation(self) -> None:
        """
        Начало процесса установки.
        """
        python_installer_path = self.get_temp_file_path("python_installer.exe")
        vscode_installer_path = self.get_temp_file_path("vscode_installer.exe")

        self.download_file(config.INSTALLERS["python"], python_installer_path)
        self.download_file(config.INSTALLERS["vscode"], vscode_installer_path)

        self.install_python(python_installer_path)
        self.install_vscode(vscode_installer_path)

        self.install_python_packages()
        self.install_vscode_extensions()
