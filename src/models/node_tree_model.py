from PySide6.QtCore import Qt, QAbstractItemModel, QModelIndex
from PySide6.QtGui import QColor


class NodeTreeModel(QAbstractItemModel):
    def __init__(self, data=None):
        QAbstractItemModel.__init__(self)

        self.input_dates = None
        self.input_magnitudes = None
        self.column_count = None
        self.row_count = None
        self.load_data()

    def load_data(self):
        self.input_dates = [1, 2, 3]
        self.input_magnitudes = [4, 5, 6]
        self.column_count = 2
        self.row_count = len(self.input_magnitudes)

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Date", "Magnitude")[section]
        else:
            return f"{section}"

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()
        if role == Qt.DisplayRole:
            if column == 0:
                date = self.input_dates[row]
                return str(date)
            elif column == 1:
                magnitude = self.input_magnitudes[row]
                return f"{magnitude:.2f}"
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight
        return None
