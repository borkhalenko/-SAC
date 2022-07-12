from PySide6.QtWidgets import QApplication
from src.MainWindow import MainWindow

import sys

app = QApplication(sys.argv)

window = MainWindow()

window.show()

sys.exit(app.exec())
