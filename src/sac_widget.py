from PySide6.QtCore import Slot

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QToolBar,
    QTreeView,
    QHeaderView,
    QSizePolicy
)

from src.models.node_tree_model import NodeTreeModel


class SacWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.model = NodeTreeModel()
        self.table_view = QTreeView()
        self.table_view.setModel(self.model)

        # # QTableView Headers
        # self.horizontal_header = self.table_view.horizontalHeader()
        # self.vertical_header = self.table_view.verticalHeader()
        # self.horizontal_header.setSectionResizeMode(
        #                        QHeaderView.ResizeToContents
        #                        )
        # self.vertical_header.setSectionResizeMode(
        #                      QHeaderView.ResizeToContents
        #                      )
        #
        # self.horizontal_header.setStretchLastSection(True)

        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size.setHorizontalStretch(1)
        self.table_view.setSizePolicy(size)

        # creating layouts
        self.main_layout = QVBoxLayout()
        self.toolbar_layout = QHBoxLayout()
        self.content_layout = QHBoxLayout()
        self.main_layout.addLayout(self.toolbar_layout)
        self.main_layout.addLayout(self.content_layout)

        self.content_layout.addWidget(self.table_view)
        self.setLayout(self.main_layout)

        # creating a toolbar in the toolbar layout
        #toolbar = QToolBar("Main toolbar")
        #self.addToolBar(toolbar)



    @Slot()
    def the_button_was_clicked(self, checked):
        print(f"Clicked! Current state is {checked}")