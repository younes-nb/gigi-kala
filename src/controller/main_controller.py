import sys

from PyQt6.QtWidgets import QMessageBox

from src.controller.add_repair_shop_controller import AddRepairShopController
from src.controller.add_tree_controller import AddTreeController
from src.controller.search_controller import SearchController
from src.controller.tree_controller import TreeController
from src.view.main_window import MainWindow
from src.model.tree import Tree, Pos, nearest

r = 'right'
l = 'left'
p = 'parent'

class MainController(MainWindow):
    def __init__(self):
        super(MainController, self).__init__()
        self.add_tree_controller = AddTreeController(self)
        self.add_repair_shop_controller = AddRepairShopController(self)
        self.search_controller = SearchController(self)
        self.tree = TreeController()
        self.setCentralWidget(self.tree)
        self.init_menu()
        self.history = []
        self.root = None
        self.t = None
        self.target = None

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
        self.t = Tree(self.root)
        # TODO:
        self.t.display()

    def add_repair_shop_func(self, x, y, z):
        self.add(self.t, Pos(x, y, z))
        # TODO:
        self.t.display()

    def search_func(self, x, y, z):
        result = nearest(self.t, Pos(x, y, z))
        # TODO:
        print(result)

    def remove_func(self, x, y, z):
        self.target = None
        self.get_object(self.t, Pos(x, y, z))
        self.t = self.delete(self.target)
        self.target = None
        # TODO:
