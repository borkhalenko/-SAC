from PySide6.QtGui import QStandardItemModel

from sac_unit import SacUnit


class SacUnitModel(QStandardItemModel):
    def __init__(self, parent=None):
        QStandardItemModel.__init__(self, parent)

    def data(self, index, role):
        return super().data(index, role)
