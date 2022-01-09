from src.view.add_repair_shop_view import AddRepairShopView


class AddRepairShopController(AddRepairShopView):
    def __init__(self, main_controller):
        super(AddRepairShopController, self).__init__()
        self.add_button.clicked.connect(self.init_add_button)

    def init_add_button(self):
        x = int(self.inputs_view.input_x.value())
        y = int(self.inputs_view.input_y.value())
        z = int(self.inputs_view.input_z.value())
        # Do Something
        self.close()
