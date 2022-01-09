from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 700, 700)
        self.setWindowTitle("Gigi Kala")
        self.setWindowIcon(QIcon("../Media/Icons/tree.png"))

        menu_bar = self.menuBar()
        options = menu_bar.addMenu("Options")

        self.add_tree = QAction(QIcon("../Media/Icons/add.png"), "Add Tree")
        self.add_tree.setShortcut("Alt+Insert")
        options.addAction(self.add_tree)

        self.add_repair_shop = QAction(QIcon("../Media/Icons/repair.png"), "Add Repair Shop")
        self.add_repair_shop.setShortcut("Ctrl+R")
        options.addAction(self.add_repair_shop)

        self.search = QAction(QIcon("../Media/Icons/search.png"), "Search")
        self.search.setShortcut("Ctrl+F")
        options.addAction(self.search)

        self.close_app = QAction(QIcon("../Media/Icons/close.png"), "Close")
        self.close_app.setShortcut("Ctrl+W")
        options.addAction(self.close_app)
