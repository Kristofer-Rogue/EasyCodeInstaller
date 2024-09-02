import os
import sys


def resource_path(relative_path):
    """Получение пути к ресурсу в собранной версии или в исходном коде."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
