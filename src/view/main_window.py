from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(1000, 700)
        self.setWindowTitle("Gigi Kala")
        self.setWindowIcon(QIcon("../media/icons/tree.png"))

        menu_bar = self.menuBar()
        options = menu_bar.addMenu("Options")

        self.add_tree = QAction(QIcon("../media/icons/add.png"), "Add Tree")
        self.add_tree.setShortcut("Alt+Insert")
        options.addAction(self.add_tree)

        self.add_repair_shop = QAction(QIcon("../media/icons/repair.png"), "Add Repair Shop")
        self.add_repair_shop.setShortcut("Ctrl+R")
        options.addAction(self.add_repair_shop)

        self.search = QAction(QIcon("../media/icons/search.png"), "Search")
        self.search.setShortcut("Ctrl+F")
        options.addAction(self.search)

        self.close_app = QAction(QIcon("../media/icons/close.png"), "Close")
        self.close_app.setShortcut("Ctrl+W")
        options.addAction(self.close_app)
