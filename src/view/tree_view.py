from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QFont
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from src.view.node_view import NodeView


class TreeView(QWidget):
    def __init__(self, tree):
        super(TreeView, self).__init__()
        self.setFixedSize(1000, 700)
        self.lines = []
        self.nodes = []
        if tree:
            cord_x = int(self.width() / 2)
            cord_y = 20
            r = cord_x
            self.add_node(tree, cord_x, cord_y, r)
        else:
            self.layout = QVBoxLayout(self)
            self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            massage = QLabel("Please Add a Tree by options > Add Tree or using Alt+Ins")
            massage.setFont(QFont("Arial", 13))
            self.layout.addWidget(massage)

    def add_node(self, tree, cord_x, cord_y, r):
        node = NodeView(self, tree.data.x, tree.data.y, tree.data.z, cord_x, cord_y, r)
        self.nodes.append(node)
        if tree.has("right"):
            x = node.x() + int(node.width() / 2)
            y = node.y() + node.height()
            x_child = x + int(node.r / 2)
            y_child = y + 30
            self.lines.append((x - 10, y + 10, x_child, y_child - 1))
            self.add_node(tree.right, x_child, y_child, int(r / 2))
        if tree.has("left"):
            x = node.x() + int(node.width() / 2)
            y = node.y() + node.height()
            x_child = x - int(r / 2)
            y_child = y + 30
            self.lines.append((x - 10, y + 10, x_child - 10, y_child - 1))
            self.add_node(tree.left, x_child, y_child, int(r / 2))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        self.drawLines(painter)
        painter.end()

    def drawLines(self, painter):
        pen = QPen(Qt.GlobalColor.white, 2, Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        for line in self.lines:
            painter.drawLine(line[0], line[1], line[2], line[3])
