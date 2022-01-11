from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from src.view.inputs_view import InputsView


class SearchView(QWidget):
    def __init__(self):
        super(SearchView, self).__init__()
        self.setWindowIcon(QIcon("../media/icons/tree_controller.png"))
        self.setWindowTitle("Search")
        self.setFixedSize(340, 436)
        self.layout = QVBoxLayout(self)

        search_image = QPixmap("../media/images/search.png")
        search_label = QLabel()
        search_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        search_label.setPixmap(search_image)
        self.layout.addWidget(search_label)

        self.inputs_view = InputsView()
        self.layout.addLayout(self.inputs_view)

        button_container = QVBoxLayout()
        button_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(button_container)

        self.search_button = QPushButton("Search")
        self.search_button.setFixedWidth(120)
        self.search_button.setFont(QFont("Arial", 11))
        button_container.addWidget(self.search_button)
