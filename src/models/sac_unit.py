from PySide6.QtGui import QStandardItem


class SacUnit(QStandardItem):
    pass

    def __init__(self):
        super().__init__()

    def type(self) -> int:
        return QStandardItem.UserType + 1
