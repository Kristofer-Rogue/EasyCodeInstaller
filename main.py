import threading

import customtkinter as ctk

from installer import Installer
from logger import setup_logger


class InstallerApp:
    """
    Класс для создания и управления графическим интерфейсом установки программ с использованием CustomTkinter.
    """

    def __init__(self, root: ctk.CTk) -> None:
        """
        Инициализация приложения и настройка логгера.

        :param root: Корневое окно CustomTkinter.
        """
        self.root = root
        self.root.title("Установка программ")
        ctk.set_appearance_mode("dark")  # Выбор светлого или тёмного режима
        ctk.set_default_color_theme("blue")  # Установка цветовой схемы
        self.create_widgets()

        # Настройка логгера
        self.logger = setup_logger(self.log)
        self.installer = Installer(self.logger)

    def create_widgets(self) -> None:
        """
        Создание виджетов интерфейса.
        """
        self.status_text = ctk.CTkTextbox(self.root, wrap="word", height=400, width=500)
        self.status_text.pack(padx=10, pady=10)

        self.button_frame = ctk.CTkFrame(self.root)
        self.button_frame.pack(pady=10)

        self.install_button = ctk.CTkButton(
            self.button_frame, text="Установить", command=self.start_installation_thread
        )
        self.install_button.pack(side=ctk.LEFT, padx=10)

        self.exit_button = ctk.CTkButton(
            self.button_frame, text="Выход", command=self.root.quit, state=ctk.DISABLED
        )
        self.exit_button.pack(side=ctk.LEFT)

    def log(self, message: str) -> None:
        """
        Вывод логов в текстовое поле интерфейса.

        :param message: Сообщение для вывода.
        """
        self.status_text.insert(ctk.END, message + "\n")
        self.status_text.yview(ctk.END)

    def start_installation_thread(self) -> None:
        """
        Запуск процесса установки в отдельном потоке.
        """
        self.install_button.configure(state=ctk.DISABLED)
        threading.Thread(target=self.start_installation, daemon=True).start()

    def start_installation(self) -> None:
        """
        Процесс установки программ и вывод логов в интерфейс.
        """
        self.logger.info("Начало установки...")
        self.installer.start_installation()
        self.logger.info("Установка завершена.")
        self.exit_button.configure(state=ctk.NORMAL)


if __name__ == "__main__":
    root = ctk.CTk()  # Используем CustomTkinter
    app = InstallerApp(root)
    root.mainloop()
