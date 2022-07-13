import os
import sys

from PySide6.QtWidgets import QApplication
from src.MainWindow import MainWindow


os.environ['QSG_RHI_BACKEND'] = 'opengl'

app = QApplication(sys.argv)

window = MainWindow()

window.show()

sys.exit(app.exec())
