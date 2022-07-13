from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QToolBar,
    QWidget,
)
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QPixmap

from src.utils.path import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Administrator's Center (SAC)")

        icon_path = (IMAGES_DIR / 'main_icon.png').resolve().as_posix()
        icon_pixmap = QPixmap(icon_path)
        self.setWindowIcon(QIcon(icon_pixmap))

        # creating layouts
        main_layout = QVBoxLayout()
        toolbar_layout = QHBoxLayout()
        content_layout = QHBoxLayout()
        main_layout.addLayout(toolbar_layout)
        main_layout.addLayout(content_layout)

        # creating a toolbar in the toolbar layout
        toolbar = QToolBar("Main toolbar")
        self.addToolBar(toolbar)

        # test
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        toolbar_layout.addWidget(button)
        button2 = QPushButton("And then just touch me!")
        button2.setCheckable(True)
        button2.clicked.connect(self.the_button_was_clicked)
        toolbar_layout.addWidget(button2)

        self.setCentralWidget(central_widget)

        self.showMaximized()

#    def addMenuBar(self):
#        self.menu = self.MenuBar()



    @Slot()
    def the_button_was_clicked(self, checked):
        print(f"Clicked! Current state is {checked}")
