from src.view.add_tree_view import AddTreeView


class AddTreeController(AddTreeView):
    def __init__(self, main_controller):
        super(AddTreeController, self).__init__()
        self.main_controller = main_controller
        self.add_button.clicked.connect(self.init_add_button)

    def init_add_button(self):
        x = int(self.inputs_view.input_x.value())
        y = int(self.inputs_view.input_y.value())
        z = int(self.inputs_view.input_z.value())
        self.main_controller.add_tree_func(x, y, z)
        self.close()
