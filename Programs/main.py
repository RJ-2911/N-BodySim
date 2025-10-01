import simWindow as sw

class Main():
    def __init__(self):
        self.simWin = sw.SimWindow()
        self.simWin.main_loop()
        
        

if __name__ == "__main__":
    Main()