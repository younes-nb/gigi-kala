import sys

from PyQt6.QtWidgets import QMessageBox

from src.controller.add_repair_shop_controller import AddRepairShopController
from src.controller.add_tree_controller import AddTreeController
from src.controller.search_controller import SearchController
from src.controller.tree_controller import TreeController
from src.view.main_window import MainWindow


class MainController(MainWindow):
    def __init__(self):
        super(MainController, self).__init__()
        self.add_tree_controller = AddTreeController(self)
        self.add_repair_shop_controller = AddRepairShopController(self)
        self.search_controller = SearchController(self)
        self.tree = TreeController()
        self.setCentralWidget(self.tree)
        self.init_menu()

    def init_menu(self):
        self.add_tree.triggered.connect(self.init_add_tree)
        self.add_repair_shop.triggered.connect(self.init_add_repair_shop)
        self.search.triggered.connect(self.init_search)
        self.close_app.triggered.connect(self.closeEvent)

    def init_add_tree(self):
        self.add_tree_controller.show()

    def init_add_repair_shop(self):
        self.add_repair_shop_controller.show()

    def init_search(self):
        self.search_controller.show()

    def closeEvent(self, event):
        try:
            reply = QMessageBox.question(self, 'Quit?',
                                         'Are you sure you want to quit?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                self.add_tree_controller.close()
                self.add_repair_shop_controller.close()
                self.search_controller.close()
                if not type(event) == bool:
                    event.accept()
                else:
                    sys.exit()
            else:
                if not type(event) == bool:
                    event.ignore()

        except Exception as e:
            print(e)
