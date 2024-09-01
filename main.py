import tkinter as tk
from tkinter import scrolledtext
import threading
from installer import Installer


class InstallerApp:
    def __init__(self, root: tk.Tk) -> None:
        """
        Инициализация приложения для установки программ.

        :param root: Корневой элемент Tkinter.
        """
        self.root = root
        self.root.title("Установка программ")
        self.installer = Installer()
        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Создание виджетов для интерфейса.
        """
        self.status_text = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, height=20, width=60
        )
        self.status_text.pack(padx=10, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.install_button = tk.Button(
            self.button_frame, text="Установить", command=self.start_installation_thread
        )
        self.install_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(
            self.button_frame, text="Выход", command=self.root.quit, state=tk.DISABLED
        )
        self.exit_button.pack(side=tk.LEFT)

    def log(self, message: str) -> None:
        """
        Логирование сообщения в текстовое поле.

        :param message: Сообщение для логирования.
        """
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.yview(tk.END)

    def start_installation(self) -> None:
        """
        Начало установки и логирование процесса.
        """
        self.install_button.config(state=tk.DISABLED)
        self.log("Начало установки...")
        try:
            self.installer.start_installation()
            self.log("Установка завершена.")
            self.exit_button.config(state=tk.NORMAL)
        except Exception as e:
            self.log(f"Ошибка установки: {e}")

    def start_installation_thread(self) -> None:
        """
        Запуск процесса установки в отдельном потоке.
        """
        threading.Thread(target=self.start_installation, daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()
