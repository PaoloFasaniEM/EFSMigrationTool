import os
import sys

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QSettings
from PySide6.QtGui import QIcon
from services.migration_service import MigrationService
from services.logger import Logger, LogLevel


class MainWindowController:

    def __init__(self, window):
        self.window = window
        
        if getattr(sys, 'frozen', False):
            BASE_PATH = os.path.join(os.path.dirname(sys.executable), '_internal')
        else:
            BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.window.setWindowIcon(QIcon(os.path.join(BASE_PATH, "resources", "icon.png")))

        Logger.init(self._log_to_ui)

        self.connect_events()
        self.migration_service = MigrationService()

        self.settings = QSettings("EFS", "MigrationTool")
        self.load_settings()

    def _log_to_ui(self, message: str, level: LogLevel):
        color = level.value
        prefix = f"[{level.name}]"
        self.window.txtLog.append(f'<span style="color:{color}">{prefix} {message}</span>')

    def load_settings(self):
        old_path = self.settings.value("old_path", "")
        new_path = self.settings.value("new_path", "")
        self.window.txtOldPath.setText(old_path)
        self.window.txtNewPath.setText(new_path)

    def connect_events(self):
        self.window.btnBrowseOld.clicked.connect(self.browse_old_directory)
        self.window.btnBrowseNew.clicked.connect(self.browse_new_directory)
        self.window.btnImport.clicked.connect(self.import_data)
        self.window.btnCopySessions.clicked.connect(self.copy_sessions)
        self.window.btnCopyJournal.clicked.connect(self.copy_journal)

    def browse_old_directory(self):
        directory = QFileDialog.getExistingDirectory(
            self.window, "Select Old EFS Installation"
        )
        if directory:
            self.window.txtOldPath.setText(directory)
            self.settings.setValue("old_path", directory)
            Logger.info(f"Old installation selected: {directory}")

    def browse_new_directory(self):
        directory = QFileDialog.getExistingDirectory(
            self.window, "Select New EFS Installation"
        )
        if directory:
            self.window.txtNewPath.setText(directory)
            self.settings.setValue("new_path", directory)
            Logger.info(f"New installation selected: {directory}")

    def import_data(self):
        old_path = self.window.txtOldPath.text()
        new_path = self.window.txtNewPath.text()

        if not old_path:
            Logger.error("Old installation path missing")
            return
        if not new_path:
            Logger.error("New installation path missing")
            return

        copy_sessions = self.window.chkSessions.isChecked()
        copy_journal  = self.window.chkJournal.isChecked()

        self.migration_service.import_all(old_path, new_path, copy_sessions, copy_journal)

    def copy_sessions(self):
        old_path = self.window.txtOldPath.text()
        new_path = self.window.txtNewPath.text()
        if not old_path or not new_path:
            Logger.error("Both paths must be set")
            return
        self.migration_service.copy_folder(old_path, new_path, "sessions")

    def copy_journal(self):
        old_path = self.window.txtOldPath.text()
        new_path = self.window.txtNewPath.text()
        if not old_path or not new_path:
            Logger.error("Both paths must be set")
            return
        self.migration_service.copy_folder(old_path, new_path, "journal")