from PySide6.QtCore import Slot

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QToolBar,
)


class SacWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # creating layouts
        main_layout = QVBoxLayout()
        toolbar_layout = QHBoxLayout()
        content_layout = QHBoxLayout()
        main_layout.addLayout(toolbar_layout)
        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

        # creating a toolbar in the toolbar layout
        #toolbar = QToolBar("Main toolbar")
        #self.addToolBar(toolbar)



    @Slot()
    def the_button_was_clicked(self, checked):
        print(f"Clicked! Current state is {checked}")