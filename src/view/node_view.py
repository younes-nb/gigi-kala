from PyQt6.QtWidgets import QLabel


class NodeView(QLabel):
    def __init__(self, parent, pos_x, pos_y, pos_z, x, y, r):
        super(NodeView, self).__init__(parent)
        self.parent = parent
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.r = r

        self.setText("{} , {} , {}".format(self.pos_x, self.pos_y, self.pos_z))
        self.setStyleSheet("""
            background-color: #1A7BA9;
            border-radius: 10px;
            padding: 5px;
            font-size: 16px;
        """)
        self.move(x - int(self.width() / 2), y)
