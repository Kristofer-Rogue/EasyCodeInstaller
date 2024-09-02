import os
import sys


def resource_path(relative_path: str) -> str:
    """
    Получает путь к ресурсу, который может быть в собранной версии
    или в исходном коде.

    :param relative_path: Относительный путь к ресурсу.
    :return: Полный путь к ресурсу.
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
