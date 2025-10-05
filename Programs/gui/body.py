class Body:
    def __init__(self, gui_window):
        self.gui_window = gui_window
        self.original_list = []

    def add_object(self, body_data):
        # Add a new body to the simulation
        self.original_list.append(body_data)