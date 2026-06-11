import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from controllers.main_window_controller import MainWindowController

import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("EFS.MigrationTool")

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

    window = load_ui("ui/mainwindow.ui")

    controller = MainWindowController(window)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()