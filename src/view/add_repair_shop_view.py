from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from src.view.inputs_view import InputsView


class AddRepairShopView(QWidget):
    def __init__(self):
        super(AddRepairShopView, self).__init__()
        self.setWindowIcon(QIcon("../media/icons/tree.png"))
        self.setWindowTitle("Add Repair Shop")
        self.setFixedSize(340, 426)
        self.layout = QVBoxLayout(self)

        repair_shop_image = QPixmap("../media/images/repair-shop.png")
        repair_shop_label = QLabel()
        repair_shop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        repair_shop_label.setPixmap(repair_shop_image)
        self.layout.addWidget(repair_shop_label)

        self.inputs_view = InputsView()
        self.layout.addLayout(self.inputs_view)

        button_container = QVBoxLayout()
        button_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(button_container)

        self.add_button = QPushButton("Add")
        self.add_button.setFixedWidth(120)
        self.add_button.setFont(QFont("Arial", 11))
        button_container.addWidget(self.add_button)
