from src.view.remove_view import RemoveView


class RemoveController(RemoveView):
    def __init__(self, main_controller):
        super(RemoveController, self).__init__()
        self.main_controller = main_controller
        self.remove_button.clicked.connect(self.init_remove_button)

    def init_remove_button(self):
        x = int(self.inputs_view.input_x.value())
        y = int(self.inputs_view.input_y.value())
        z = int(self.inputs_view.input_z.value())
        self.close()
        self.main_controller.remove_func(x, y, z)
