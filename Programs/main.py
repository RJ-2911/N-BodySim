from multiprocessing import Process, Queue
import simulation.simWindow as sw
import gui.guiWindow as gw

class Main:
    def __init__(self):
        self.sim_speed = 10  
        
        self.body_to_sim_queue = Queue() 
        self.sim_to_body_queue = Queue()  
        
        gui_process = Process(target=self.run_gui)
        sim_process = Process(target=self.run_sim)

        gui_process.start()
        sim_process.start()

        gui_process.join()
        sim_process.join()

    def run_gui(self):
        gui = gw.GuiWindow(self, self.body_to_sim_queue, self.sim_to_body_queue)
        gui.main_loop()

    def run_sim(self):
        sim = sw.SimWindow(self, self.body_to_sim_queue, self.sim_to_body_queue)
        sim.main_loop()

if __name__ == "__main__": 
    Main()