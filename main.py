import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from controllers.main_window_controller import MainWindowController

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("EFS.MigrationTool")

if getattr(sys, 'frozen', False):
    BASE_PATH = os.path.join(os.path.dirname(sys.executable), '_internal')
else:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def load_ui(ui_file_path):
    loader = QUiLoader()

    ui_file = QFile(ui_file_path)

    if not ui_file.open(QFile.ReadOnly):
        raise Exception(f"Cannot open UI file: {ui_file_path}")

    window = loader.load(ui_file)

    ui_file.close()

    if window is None:
        raise Exception("Failed to load UI")

    return window


def main():
    app = QApplication(sys.argv)

    qss_path = os.path.join(BASE_PATH, "resources", "style.qss")
    with open(qss_path, "r") as f:
        app.setStyleSheet(f.read())

    window = load_ui(os.path.join(BASE_PATH, "ui", "mainwindow.ui"))

    controller = MainWindowController(window)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()