from PyQt6.QtCore import Qt

from src.view.search_view import SearchView


class SearchController(SearchView):
    def __init__(self, main_controller):
        super(SearchController, self).__init__()
        self.main_controller = main_controller
        self.search_button.clicked.connect(self.init_search_button)

    def init_search_button(self):
        x = int(self.inputs_view.input_x.value())
        y = int(self.inputs_view.input_y.value())
        z = int(self.inputs_view.input_z.value())
        self.main_controller.search_func(x, y, z)
        self.close()
