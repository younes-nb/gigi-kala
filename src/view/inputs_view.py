from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QSpinBox


class InputsView(QHBoxLayout):
    def __init__(self):
        super(InputsView, self).__init__()
        self.addStretch(1)
        self.setContentsMargins(0, 15, 0, 20)

        input_container_x = QHBoxLayout()
        input_container_x.addStretch(1)
        input_container_x.setContentsMargins(5, 0, 0, 0)
        self.addLayout(input_container_x)

        label_x = QLabel("x :")
        label_x.setFont(QFont("Arial", 12))
        input_container_x.addWidget(label_x)

        self.input_x = QSpinBox()
        self.input_x.setMinimum(-1000)
        input_container_x.addWidget(self.input_x)

        input_container_y = QHBoxLayout()
        input_container_y.addStretch(1)
        input_container_y.setContentsMargins(30, 0, 30, 0)
        self.addLayout(input_container_y)

        label_y = QLabel("y :")
        label_y.setFont(QFont("Arial", 12))
        input_container_y.addWidget(label_y)

        self.input_y = QSpinBox()
        self.input_y.setMinimum(-1000)
        input_container_y.addWidget(self.input_y)

        input_container_z = QHBoxLayout()
        input_container_z.addStretch(1)
        input_container_z.setContentsMargins(0, 0, 5, 0)
        self.addLayout(input_container_z)

        label_z = QLabel("z :")
        label_z.setFont(QFont("Arial", 12))
        input_container_z.addWidget(label_z)

        self.input_z = QSpinBox()
        self.input_z.setMinimum(-1000)
        input_container_z.addWidget(self.input_z)
