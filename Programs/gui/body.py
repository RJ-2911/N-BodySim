class Body:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.original_list = []
        self.sim_spheres = []  # List to store sphere data from simulation

    def add_object(self, body_data):
        self.original_list.append(body_data)
        self.guiWin.body_to_sim_queue.put(body_data)

    def update_from_sim(self):
        while not self.guiWin.sim_to_body_queue.empty():
            self.sim_spheres = self.guiWin.sim_to_body_queue.get()