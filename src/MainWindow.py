from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Administrator's Center (SAC)")
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)
