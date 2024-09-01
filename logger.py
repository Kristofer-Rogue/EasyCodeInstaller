import logging
from typing import Callable


class TkinterLogHandler(logging.Handler):
    """
    Кастомный обработчик для вывода логов в виджет Tkinter.

    :param log_callback: Функция, которая принимает строку (сообщение) для вывода в интерфейс.
    """

    def __init__(self, log_callback: Callable[[str], None]) -> None:
        super().__init__()
        self.log_callback = log_callback

    def emit(self, record: logging.LogRecord) -> None:
        """
        Метод обработки логов для вывода в интерфейс.

        :param record: Лог-запись, которая будет передана в интерфейс.
        """
        log_entry = self.format(record)
        self.log_callback(log_entry)


def setup_logger(log_callback: Callable[[str], None], log_file: str = "installer.log") -> logging.Logger:
    """
    Настройка логгера с обработчиками для интерфейса Tkinter и файла.

    :param log_callback: Функция для вывода логов в интерфейс.
    :param log_file: Путь к файлу для записи логов.
    :return: Настроенный логгер.
    """
    logger = logging.getLogger("InstallerLogger")
    logger.setLevel(logging.DEBUG)

    # Обработчик для Tkinter
    tk_handler = TkinterLogHandler(log_callback)
    tk_handler.setLevel(logging.DEBUG)
    simple_formatter = logging.Formatter('%(message)s')
    tk_handler.setFormatter(simple_formatter)

    # Обработчик для файла
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    detailed_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(detailed_formatter)

    logger.addHandler(tk_handler)
    logger.addHandler(file_handler)

    return logger
