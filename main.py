import os
import shutil
import threading
import tkinter as tk

import customtkinter as ctk
from PIL import Image

import config
from common import resource_path
from installer import Installer
from logger import setup_logger


class InstallerApp:
    """
    Основное приложение для установки программ с двумя фреймами.
    """

    def __init__(self, root: ctk.CTk) -> None:
        """
        Инициализация приложения, создание фреймов и логгера.

        :param root: Корневое окно CustomTkinter.
        """
        self.root = root
        self.root.title("Easy Code Installer")
        self.root.geometry("600x400")
        self.root.minsize(600, 400)

        self.root.iconbitmap(resource_path(config.ICON_PATH))

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Настройка фреймов
        self.frame_welcome = ctk.CTkFrame(self.root, corner_radius=0)
        self.frame_installation = ctk.CTkFrame(self.root, corner_radius=0)

        # Создание виджетов
        self.create_welcome_frame()
        self.create_installation_frame()

        # Логгер и установка
        self.logger = setup_logger(self.log)
        self.installer = Installer(self.logger, self.update_progress_bar)

        # Изначально показываем первый фрейм
        self.show_welcome_frame()

    def create_welcome_frame(self) -> None:
        """
        Создание первого фрейма с приветственным сообщением и кнопкой установки.
        """
        # Установка растягиваемости окна
        self.frame_welcome.pack(fill="both", expand=True)  # Фрейм растягивается с окном

        # Создание контейнера для центрирования
        container = ctk.CTkFrame(self.frame_welcome, corner_radius=0)
        container.pack(expand=True, fill='both')  # Центрирование по вертикали и горизонтали

        # Использование grid для расположения элементов
        container.grid_rowconfigure(0, weight=1)  # Распределение пространства по вертикали
        container.grid_rowconfigure(1, weight=1)  # Распределение пространства по вертикали
        container.grid_rowconfigure(2, weight=1)  # Распределение пространства по вертикали
        container.grid_columnconfigure(0, weight=1)  # Распределение пространства по горизонтали

        # Лого компании
        logo_image = Image.open(resource_path(config.LOGO_PATH))
        logo_image = logo_image.resize((550, 100), Image.Resampling.LANCZOS)

        # Используем CTkImage
        logo_ctk_image = ctk.CTkImage(light_image=logo_image, size=(550, 100))
        logo_label = ctk.CTkLabel(container, image=logo_ctk_image, text="")
        logo_label.image = logo_ctk_image  # Сохранение ссылки на изображение
        logo_label.grid(row=0, column=0, pady=20)  # Центрирование по горизонтали и вертикали

        welcome_label = ctk.CTkLabel(container, text=config.WELCOME_MESSAGE, font=("Arial", 20), wraplength=550)
        welcome_label.grid(row=1, column=0, pady=20, padx=20, sticky='n')  # Верхняя часть контейнера

        # Кнопка для начала установки
        install_button = ctk.CTkButton(container, text=config.BUTTON_TEXT_INSTALL,
                                       command=self.show_installation_frame)
        install_button.grid(row=2, column=0, pady=20)  # Нижняя часть контейнера

    def create_installation_frame(self) -> None:
        """
        Создание второго фрейма с логами установки и прогресс-баром.
        """
        # Установка растягиваемости окна
        self.frame_installation.pack(fill="both", expand=True)  # Фрейм растягивается с окном

        # Создание контейнера для центрирования
        container = ctk.CTkFrame(self.frame_installation, corner_radius=0)
        container.pack(expand=True, fill='both')  # Центрирование по вертикали и горизонтали

        # Использование grid для расположения элементов
        container.grid_rowconfigure(0, weight=1)  # Распределение пространства по вертикали
        container.grid_rowconfigure(1, weight=0)  # Распределение пространства по вертикали
        container.grid_rowconfigure(2, weight=0)  # Распределение пространства по вертикали
        container.grid_columnconfigure(0, weight=1)  # Распределение пространства по горизонтали

        self.status_text = ctk.CTkTextbox(container, wrap='word')
        self.status_text.grid(row=0, column=0, pady=10, padx=20, sticky='nsew')  # Заполняет пространство

        self.progress_bar = ctk.CTkProgressBar(container)
        self.progress_bar.grid(row=1, column=0, pady=20, padx=20,
                               sticky='ew')  # Прогресс-бар растягивается по горизонтали

        self.finish_button = ctk.CTkButton(container, text=config.BUTTON_TEXT_FINISH,
                                           command=self.finish_installation, state=tk.DISABLED)
        self.finish_button.grid(row=2, column=0, pady=20, padx=20,
                                sticky='se')  # Привязка кнопки к нижнему правому углу

    def show_welcome_frame(self) -> None:
        """
        Показ первого фрейма с приветствием.
        """
        self.frame_installation.pack_forget()  # Скрыть второй фрейм
        self.frame_welcome.pack(padx=0, pady=0, fill='both', expand=True)

    def show_installation_frame(self) -> None:
        """
        Показ второго фрейма с логами установки и началом процесса установки.
        """
        self.frame_welcome.pack_forget()  # Скрыть первый фрейм
        self.frame_installation.pack(padx=0, pady=0, fill='both', expand=True)

        # Запуск установки в отдельном потоке
        threading.Thread(target=self.start_installation, daemon=True).start()

    def log(self, message: str) -> None:
        """
        Вывод логов в текстовое поле интерфейса.

        :param message: Сообщение для вывода.
        """
        self.status_text.insert(ctk.END, message + "\n")
        self.status_text.yview(ctk.END)

    def update_progress_bar(self, value: float) -> None:
        """
        Обновление прогресс-бара.

        :param value: Значение прогресса (от 0 до 1).
        """
        self.progress_bar.set(value)

    def start_installation(self) -> None:
        """
        Процесс установки программ и вывод логов в интерфейс.
        """
        self.logger.info("Начало установки...")

        # Имитация установки программ
        self.installer.start_installation()

        self.logger.info("Установка завершена.")

        # Активировать кнопку завершения
        self.finish_button.configure(state=tk.NORMAL)

    def finish_installation(self) -> None:
        """
        Завершение работы программы.
        """
        if os.path.exists(config.TEMP_DIR):
            shutil.rmtree(config.TEMP_DIR)
            self.logger.info("Временная папка удалена.")
        self.root.quit()


if __name__ == "__main__":
    root = ctk.CTk()
    app = InstallerApp(root)
    root.mainloop()
