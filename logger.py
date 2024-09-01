import logging
from typing import Callable


class TkinterLogHandler(logging.Handler):
    def __init__(self, log_callback: Callable[[str], None]) -> None:
        """
        Инициализация обработчика логов для Tkinter.

        :param log_callback: Функция обратного вызова для передачи сообщений в интерфейс.
        """
        super().__init__()
        self.log_callback = log_callback

    def emit(self, record: logging.LogRecord) -> None:
        """
        Передача лог-сообщений через функцию обратного вызова.

        :param record: Запись логов.
        """
        log_entry = self.format(record)
        self.log_callback(log_entry)


def setup_logger(log_callback: Callable[[str], None]) -> logging.Logger:
    """
    Настройка логгера для приложения.

    :param log_callback: Функция обратного вызова для логов.
    :return: Настроенный логгер.
    """
    logger = logging.getLogger("InstallerLogger")
    logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования

    # Создаем обработчик для интерфейса
    tk_handler = TkinterLogHandler(log_callback)
    tk_handler.setLevel(logging.DEBUG)

    # Форматирование логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    tk_handler.setFormatter(formatter)

    # Добавляем обработчик в логгер
    logger.addHandler(tk_handler)

    return logger
