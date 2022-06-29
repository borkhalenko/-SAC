from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Administrator's Center (SAC)")
        main_layout = QVBoxLayout()
        toolbar_layout = QHBoxLayout()
        content_layout = QHBoxLayout()
        main_layout.addLayout(toolbar_layout)
        main_layout.addLayout(content_layout)

        # test
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        toolbar_layout.addWidget(button)
        button2 = QPushButton("And then just touch me!")
        button2.setCheckable(True)
        button2.clicked.connect(self.the_button_was_clicked)
        toolbar_layout.addWidget(button2)

        self.setCentralWidget(central_widget)

    def the_button_was_clicked(self, checked):
        print(f"Clicked! Current state is {checked}" )
