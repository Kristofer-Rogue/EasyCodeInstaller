# Easy Code Installer

**Easy Code Installer** — это приложение для установки программного обеспечения, предоставляющее простой и удобный
графический интерфейс. Оно поддерживает установку Python-пакетов и других приложений, таких как Visual Studio Code, и
позволяет отслеживать процесс установки через логирование и индикаторы прогресса.

## Возможности программы:

### Установка программ:

1) Python 3.11.9
2) Visual Studio Code

### Установка пакетов pip:

1) aiogram v2.25.2
2) pygame
3) requests

### Установка расширений VSC

1) ms-python.python

Все установки полностью настраиваемы и легко дополняемы. Для этого дополните файл config.py

## Сборка установщика из исходников

Чтобы собрать установщик из исходных файлов, выполните следующие шаги:

### Установка зависимостей

1. Установите poetry:

    ```cmd
    pip install poetry
    ```

   Установите зависимости:

    ```cmd
    poetry install
    ```

### Соберите исполняемый файл с помощью PyInstaller:

- Запустите сборку:

    ```cmd
    pyinstaller main.spec
    ```

Это создаст папку `dist`, в которой будет находиться ваш скомпилированный исполняемый файл.

## Скриншоты программы:

![frame1](https://github.com/user-attachments/assets/8a0c7829-a4ac-46d4-a2ba-ce15cad94c34)
![frame2](https://github.com/user-attachments/assets/bb33adb3-c73d-4afe-bac4-9b2452e5c694)
