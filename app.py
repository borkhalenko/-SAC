"""
TODO: write some smart at docstring
"""
import sys

from PySide6.QtWidgets import QApplication
from src.sac_window import SacWindow

app = QApplication(sys.argv)

window = SacWindow()

window.show()

sys.exit(app.exec())
g