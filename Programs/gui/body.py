class Body:
    def __init__(self, gui_window):
        self.gui_window = gui_window
        self.original_list = []
        self.sim_spheres = []  

    def add_object(self, body_data):
        
        self.original_list.append(body_data)
        
        self.gui_window.body_to_sim_queue.put(body_data)

    def update_from_sim(self):
        while not self.gui_window.sim_to_body_queue.empty():
            self.sim_spheres = self.gui_window.sim_to_body_queue.get()