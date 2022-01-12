import copy
import sys

from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QMessageBox

from src.controller.add_repair_shop_controller import AddRepairShopController
from src.controller.add_tree_controller import AddTreeController
from src.controller.search_controller import SearchController
from src.controller.tree_controller import TreeController
from src.controller.remove_controller import RemoveController
from src.model.tree import Tree, Pos, nearest
from src.view.main_window import MainWindow

r = 'right'
l = 'left'
p = 'parent'


class MainController(MainWindow):
    def __init__(self):
        super(MainController, self).__init__()
        self.add_tree_controller = AddTreeController(self)
        self.add_repair_shop_controller = AddRepairShopController(self)
        self.search_controller = SearchController(self)
        self.remove_controller = RemoveController(self)
        self.tree_controller = TreeController(None)
        self.setCentralWidget(self.tree_controller)
        self.init_menu()
        self.history = []
        self.root = None
        self.tree_model = None
        self.target = None

    def init_menu(self):
        self.add_tree.triggered.connect(self.init_add_tree)
        self.add_repair_shop.triggered.connect(self.init_add_repair_shop)
        self.search.triggered.connect(self.init_search)
        self.remove.triggered.connect(self.init_remove)
        self.close_app.triggered.connect(self.closeEvent)

    def init_add_tree(self):
        self.add_tree_controller.show()

    def init_add_repair_shop(self):
        self.add_repair_shop_controller.show()

    def init_search(self):
        self.search_controller.show()

    def init_remove(self):
        self.remove_controller.show()

    def closeEvent(self, event):
        reply = QMessageBox().question(self, 'Quit?',
                                       'Are you sure you want to quit?',
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                       QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.add_tree_controller.close()
            self.add_repair_shop_controller.close()
            self.search_controller.close()
            self.remove_controller.close()
            if not type(event) == bool:
                event.accept()
            else:
                sys.exit()
        else:
            if not type(event) == bool:
                event.ignore()

    def add(self, tree: Tree, node: Pos):
        tree.insert(node)
        self.history.append(node)

    def delete(self, node: Pos):
        if self.is_root(node):
            tree2 = Tree(self.history[0])
            self.history.pop(0)
        else:
            node = self.search(node)
            self.history.remove(node)
            tree2 = Tree(self.root)
        for i in self.history:
            tree2.insert(i)
        return tree2

    def search(self, node: Pos):
        if node is not None:
            for i in self.history:
                if i.x == node.data.x and i.y == node.data.y and i.z == node.data.z:
                    return i

    def is_root(self, node):
        if self.root.x == node.data.x and self.root.y == node.data.y and self.root.z == node.data.z:
            return True

    def get_object(self, tree: Tree, node: Pos):
        if tree is None:
            return
        if node.x == tree.data.x and node.y == tree.data.y and node.z == tree.data.z:
            self.target = tree
        self.get_object(tree.left, node)
        self.get_object(tree.right, node)

    def add_tree_func(self, x, y, z):
        self.root = Pos(x, y, z)
        self.history = []
        self.tree_model = Tree(self.root)
        tree = copy.deepcopy(self.tree_model)
        self.tree_controller = TreeController(tree)
        self.setCentralWidget(self.tree_controller)

    def add_repair_shop_func(self, x, y, z):
        if self.tree_model:
            self.add(self.tree_model, Pos(x, y, z))
            tree = copy.deepcopy(self.tree_model)
            self.tree_controller = TreeController(tree)
            self.setCentralWidget(self.tree_controller)
        else:
            resultBox = QMessageBox()
            resultBox.setWindowTitle("Can Not Add A Repair Shop Without A Tree!")
            resultBox.setWindowIcon(QIcon("../media/icons/tree.png"))
            resultBox.setIcon(QMessageBox.Icon.Warning)
            resultBox.setFont(QFont("Arial", 11))
            resultBox.setText(
                "First please add a tree by options > Add Tree or using Alt+Ins")
            resultBox.exec()

    def search_func(self, x, y, z):
        if self.tree_model:
            result = nearest(self.tree_model, Pos(x, y, z))
            for node in self.tree_controller.nodes:
                if node.pos_x == result[0][0] and node.pos_y == result[0][1] and node.pos_z == result[0][2]:
                    node.setStyleSheet("""
                            background-color: green;
                            border-radius: 10px;
                            padding: 7px;
                            font-size: 18px;
                        """)
                    node.update()
                    resultBox = QMessageBox()
                    resultBox.setWindowTitle("Repair Shop Found!")
                    resultBox.setWindowIcon(QIcon("../media/icons/tree.png"))
                    resultBox.setIcon(QMessageBox.Icon.Information)
                    resultBox.setFont(QFont("Arial", 11))
                    resultBox.setText(
                        "Coordinates : ({} , {} , {})\nDistance : {}".format(result[0][0], result[0][1],
                                                                             result[0][2], result[1]))
                    resultBox.exec()
                    break
        else:
            resultBox = QMessageBox()
            resultBox.setWindowTitle("Can Not Search Without A Tree!")
            resultBox.setWindowIcon(QIcon("../media/icons/tree.png"))
            resultBox.setIcon(QMessageBox.Icon.Warning)
            resultBox.setFont(QFont("Arial", 11))
            resultBox.setText(
                "First please add a tree by options > Add Tree or using Alt+Ins")
            resultBox.exec()

    def remove_func(self, x, y, z):
        if self.tree_model:

            found = False
            for node in self.tree_controller.nodes:
                if node.pos_x == x and node.pos_y == y and node.pos_z == z:
                    found = True
                    break

            if found:
                try:
                    self.target = None
                    self.get_object(self.tree_model, Pos(x, y, z))
                    self.tree_model = self.delete(self.target)
                    self.target = None
                    # TODO:
                except Exception as e:
                    print(e)
                tree = copy.deepcopy(self.tree_model)
                self.tree_controller = TreeController(tree)
                self.setCentralWidget(self.tree_controller)
                resultBox = QMessageBox()
                resultBox.setWindowTitle("Repair Shop Removed!")
                resultBox.setWindowIcon(QIcon("../media/icons/tree.png"))
                resultBox.setIcon(QMessageBox.Icon.Information)
                resultBox.setFont(QFont("Arial", 11))
                resultBox.setText("Repair Shop in ({} , {} , {}) has been removed.".format(x, y, z))
                resultBox.exec()
            else:
                resultBox = QMessageBox()
                resultBox.setWindowTitle("Repair Shop Not Found!")
                resultBox.setWindowIcon(QIcon("../media/icons/tree.png"))
                resultBox.setIcon(QMessageBox.Icon.Warning)
                resultBox.setFont(QFont("Arial", 11))
                resultBox.setText(
                    "No Repair Shop found in ({} , {} , {}) .".format(x, y, z))
                resultBox.exec()
        else:
            resultBox = QMessageBox()
            resultBox.setWindowTitle("Can Not Remove A Repair Shop Without A Tree!")
            resultBox.setWindowIcon(QIcon("../media/icons/tree.png"))
            resultBox.setIcon(QMessageBox.Icon.Warning)
            resultBox.setFont(QFont("Arial", 11))
            resultBox.setText(
                "First please add a tree by options > Add Tree or using Alt+Ins")
            resultBox.exec()
