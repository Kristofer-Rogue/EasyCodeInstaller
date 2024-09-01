import os
import subprocess
import requests
import tkinter as tk
from tkinter import scrolledtext
import config
import threading


class InstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Установка программ")

        self.create_widgets()

    def create_widgets(self):
        self.status_text = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, height=20, width=60
        )
        self.status_text.pack(padx=10, pady=10)

        self.install_button = tk.Button(
            self.root, text="Установить", command=self.start_installation_thread
        )
        self.install_button.pack(pady=10)

    def log(self, message):
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.yview(tk.END)

    def download_file(self, url, dest):
        self.log(f"Скачивание {url} в {dest}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(dest, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        self.log(f"Файл {dest} успешно загружен.")

    def install_python(self, installer_path):
        self.log("Установка Python...")
        subprocess.run(
            [installer_path] + config.INSTALL_SETTINGS["python_args"], check=True
        )
        self.log("Python установлен.")

    def install_vscode(self, installer_path):
        self.log("Установка VSCode...")
        subprocess.run(
            [installer_path] + config.INSTALL_SETTINGS["vscode_args"], check=True
        )
        self.log("VSCode установлен.")

    def install_python_packages(self):
        self.log("Установка Python пакетов...")
        try:
            subprocess.run(
                ["py", "-m", "pip", "install"] + config.PYTHON_PACKAGES,
                check=True,
            )
            self.log("Пакеты установлены.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при установке расширения: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Вывод ошибки: {e.stderr}")
        except Exception as e:
            self.log(f"Неизвестная ошибка: {e}")

    def install_vscode_extensions(self):
        self.log("Установка расширений VSCode...")
        vscode_path = r"C:\Program Files\Microsoft VS Code\bin\code.cmd"
        try:
            subprocess.run(
                [vscode_path, "--install-extension", "ms-python.python", "--force"],
                capture_output=True,
                text=True,
                check=True,
            )
            self.log("Расширение установлено.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при установке расширения: {e}")
            print(f"Стандартный вывод: {e.stdout}")
            print(f"Вывод ошибки: {e.stderr}")
        except Exception as e:
            self.log(f"Неизвестная ошибка: {e}")

    def get_temp_file_path(self, name):
        return os.path.join(config.TEMP_DIR, name)

    def start_installation(self):
        self.log("Начало установки...")

        os.makedirs(config.TEMP_DIR, exist_ok=True)

        python_installer_path = self.get_temp_file_path("python_installer.exe")
        vscode_installer_path = self.get_temp_file_path("vscode_installer.exe")

        self.download_file(config.INSTALLERS["python"], python_installer_path)
        self.download_file(config.INSTALLERS["vscode"], vscode_installer_path)

        self.install_python(python_installer_path)
        self.install_vscode(vscode_installer_path)

        self.install_python_packages()
        self.install_vscode_extensions()

        self.log("Установка завершена.")

    def start_installation_thread(self):
        threading.Thread(target=self.start_installation, daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()
