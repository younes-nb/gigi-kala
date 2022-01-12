from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from src.view.inputs_view import InputsView


class RemoveView(QWidget):
    def __init__(self):
        super(RemoveView, self).__init__()
        self.setWindowIcon(QIcon("../media/icons/tree.png"))
        self.setWindowTitle("Remove")
        self.setFixedSize(340, 436)
        self.layout = QVBoxLayout(self)

        remove_image = QPixmap("../media/images/remove.png")
        remove_label = QLabel()
        remove_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        remove_label.setPixmap(remove_image)
        self.layout.addWidget(remove_label)

        self.inputs_view = InputsView()
        self.layout.addLayout(self.inputs_view)

        button_container = QVBoxLayout()
        button_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(button_container)

        self.remove_button = QPushButton("Remove")
        self.remove_button.setFixedWidth(120)
        self.remove_button.setFont(QFont("Arial", 11))
        button_container.addWidget(self.remove_button)
