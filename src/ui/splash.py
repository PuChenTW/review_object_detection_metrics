from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QMainWindow
from src.ui.splash_ui import Ui_Dialog as Splash_UI


class Splash_Dialog(QMainWindow, Splash_UI):
    def __init__(self):
        QMainWindow.__init__(self, None, QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setupUi(self)
        self.center_screen()

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

    def center_screen(self):
        size = self.size()
        desktopSize = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        top = (desktopSize.height() / 2) - (size.height() / 2)
        left = (desktopSize.width() / 2) - (size.width() / 2)
        self.move(left, top)

    def btn_close_clicked(self):
        self.close()
