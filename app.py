import sys

from PySide6.QtWidgets import QApplication
from src.SacWindow import SacWindow

app = QApplication(sys.argv)

window = SacWindow()

window.show()
  

  
sys.exit(app.exec())
