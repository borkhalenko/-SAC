"""
TODO: write some smart at docstring
"""

from PySide6.QtWidgets import (
    QMainWindow,
)

from PySide6.QtGui import (
    QAction,
    QKeySequence,
    QIcon,
    QPixmap,
)

from src.utils.path import *
from src.sac_widget import SacWidget


class SacWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Administrator's Center (SAC)")

        icon_path = (IMAGES_DIR / "main_icon.png").resolve().as_posix()
        icon_pixmap = QPixmap(icon_path)
        self.setWindowIcon(QIcon(icon_pixmap))

        # test
        central_widget = SacWidget()

        self.setCentralWidget(central_widget)

        self.menu = None
        self.file_menu = None
        self.setup_menu_bar()

        self.showMaximized()

    def setup_menu_bar(self):
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)
