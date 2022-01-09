from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from src.view.inputs_view import InputsView


class AddTreeView(QWidget):
    def __init__(self):
        super(AddTreeView, self).__init__()
        self.setWindowIcon(QIcon("../Media/Icons/tree.png"))
        self.setWindowTitle("Add Tree")
        self.setFixedSize(340, 460)
        self.layout = QVBoxLayout(self)

        tree_image = QPixmap("../Media/Images/tree.png")
        tree_label = QLabel()
        tree_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tree_label.setPixmap(tree_image)
        self.layout.addWidget(tree_label)

        self.inputs_view = InputsView()
        self.layout.addLayout(self.inputs_view)

        button_container = QVBoxLayout()
        button_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(button_container)

        self.add_button = QPushButton("Add")
        self.add_button.setFixedWidth(120)
        self.add_button.setFont(QFont("Arial", 11))
        button_container.addWidget(self.add_button)

