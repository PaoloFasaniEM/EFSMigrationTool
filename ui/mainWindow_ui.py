# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 680)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12)
        self.groupOld = QGroupBox(self.centralwidget)
        self.groupOld.setObjectName(u"groupOld")
        self.horizontalLayoutOld = QHBoxLayout(self.groupOld)
        self.horizontalLayoutOld.setObjectName(u"horizontalLayoutOld")
        self.txtOldPath = QLineEdit(self.groupOld)
        self.txtOldPath.setObjectName(u"txtOldPath")

        self.horizontalLayoutOld.addWidget(self.txtOldPath)

        self.btnBrowseOld = QPushButton(self.groupOld)
        self.btnBrowseOld.setObjectName(u"btnBrowseOld")
        self.btnBrowseOld.setMaximumWidth(80)

        self.horizontalLayoutOld.addWidget(self.btnBrowseOld)


        self.verticalLayout.addWidget(self.groupOld)

        self.groupNew = QGroupBox(self.centralwidget)
        self.groupNew.setObjectName(u"groupNew")
        self.horizontalLayoutNew = QHBoxLayout(self.groupNew)
        self.horizontalLayoutNew.setObjectName(u"horizontalLayoutNew")
        self.txtNewPath = QLineEdit(self.groupNew)
        self.txtNewPath.setObjectName(u"txtNewPath")

        self.horizontalLayoutNew.addWidget(self.txtNewPath)

        self.btnBrowseNew = QPushButton(self.groupNew)
        self.btnBrowseNew.setObjectName(u"btnBrowseNew")
        self.btnBrowseNew.setMaximumWidth(80)

        self.horizontalLayoutNew.addWidget(self.btnBrowseNew)


        self.verticalLayout.addWidget(self.groupNew)

        self.groupExtraData = QGroupBox(self.centralwidget)
        self.groupExtraData.setObjectName(u"groupExtraData")
        self.verticalLayoutExtraData = QVBoxLayout(self.groupExtraData)
        self.verticalLayoutExtraData.setObjectName(u"verticalLayoutExtraData")
        self.lblExtraDataNote = QLabel(self.groupExtraData)
        self.lblExtraDataNote.setObjectName(u"lblExtraDataNote")
        self.lblExtraDataNote.setWordWrap(True)

        self.verticalLayoutExtraData.addWidget(self.lblExtraDataNote)

        self.chkSessions = QCheckBox(self.groupExtraData)
        self.chkSessions.setObjectName(u"chkSessions")

        self.verticalLayoutExtraData.addWidget(self.chkSessions)

        self.chkJournal = QCheckBox(self.groupExtraData)
        self.chkJournal.setObjectName(u"chkJournal")

        self.verticalLayoutExtraData.addWidget(self.chkJournal)


        self.verticalLayout.addWidget(self.groupExtraData)

        self.groupLog = QGroupBox(self.centralwidget)
        self.groupLog.setObjectName(u"groupLog")
        self.verticalLayoutLog = QVBoxLayout(self.groupLog)
        self.verticalLayoutLog.setObjectName(u"verticalLayoutLog")
        self.txtLog = QTextEdit(self.groupLog)
        self.txtLog.setObjectName(u"txtLog")
        self.txtLog.setReadOnly(True)

        self.verticalLayoutLog.addWidget(self.txtLog)


        self.verticalLayout.addWidget(self.groupLog)

        self.horizontalLayoutBottomButtons = QHBoxLayout()
        self.horizontalLayoutBottomButtons.setObjectName(u"horizontalLayoutBottomButtons")
        self.btnCopySessions = QPushButton(self.centralwidget)
        self.btnCopySessions.setObjectName(u"btnCopySessions")
        self.btnCopySessions.setMinimumHeight(44)

        self.horizontalLayoutBottomButtons.addWidget(self.btnCopySessions)

        self.btnCopyJournal = QPushButton(self.centralwidget)
        self.btnCopyJournal.setObjectName(u"btnCopyJournal")
        self.btnCopyJournal.setMinimumHeight(44)

        self.horizontalLayoutBottomButtons.addWidget(self.btnCopyJournal)

        self.btnImport = QPushButton(self.centralwidget)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setMinimumHeight(44)

        self.horizontalLayoutBottomButtons.addWidget(self.btnImport)


        self.verticalLayout.addLayout(self.horizontalLayoutBottomButtons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EFS Migration Tool", None))
        self.groupOld.setTitle(QCoreApplication.translate("MainWindow", u"Old EFS Installation", None))
        self.txtOldPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select old EFS installation folder...", None))
        self.btnBrowseOld.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.groupNew.setTitle(QCoreApplication.translate("MainWindow", u"New EFS Installation", None))
        self.txtNewPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select new EFS installation folder...", None))
        self.btnBrowseNew.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.groupExtraData.setTitle(QCoreApplication.translate("MainWindow", u"Additional Data Transfer", None))
        self.lblExtraDataNote.setText(QCoreApplication.translate("MainWindow", u"Note: copying sessions and journal may take a long time depending on file size.", None))
        self.chkSessions.setText(QCoreApplication.translate("MainWindow", u"Include sessions in import", None))
        self.chkJournal.setText(QCoreApplication.translate("MainWindow", u"Include journal in import", None))
        self.groupLog.setTitle(QCoreApplication.translate("MainWindow", u"Conversion Log", None))
        self.btnCopySessions.setText(QCoreApplication.translate("MainWindow", u"Copy Sessions Only", None))
        self.btnCopyJournal.setText(QCoreApplication.translate("MainWindow", u"Copy Journal Only", None))
        self.btnImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
    # retranslateUi

