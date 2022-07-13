import os
import sys

from PySide6.QtWidgets import QApplication
from src.SacWindow import SacWindow


os.environ["QSG_RHI_BACKEND"] = "opengl"

app = QApplication(sys.argv)

window = SacWindow()

window.show()

sys.exit(app.exec())
