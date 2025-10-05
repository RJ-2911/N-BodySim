class Body:
    def __init__(self, gui_window):
        self.gui_window = gui_window
        self.original_list = []
        self.sim_spheres = []  # Store spheres data from simulation

    def add_object(self, body_data):
        # Add to local list
        self.original_list.append(body_data)
        # Send to simulation process via queue
        self.gui_window.body_to_sim_queue.put(body_data)

    def update_from_sim(self):
        # Check queue for updated spheres data from simulation
        while not self.gui_window.sim_to_body_queue.empty():
            self.sim_spheres = self.gui_window.sim_to_body_queue.get()