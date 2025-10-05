from multiprocessing import Process
import simulation.simWindow as sw
import gui.guiWindow as gw

class Main:
    def __init__(self):
        gui_process = Process(target=self.run_gui)
        sim_process = Process(target=self.run_sim)

        gui_process.start()
        sim_process.start()

        gui_process.join()
        sim_process.join()

    def run_gui(self):
        gui = gw.GuiWindow()
        gui.main_loop()

    def run_sim(self):
        sim = sw.SimWindow()
        sim.main_loop()

if __name__ == "__main__":
    Main()
