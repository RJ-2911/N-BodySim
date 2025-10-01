import sphere as sp
import camera

import simWindow as sw

class Scene:
    def __init__(self, simWin):
        self.simWin = simWin
        
        # Set Spheres i.e. bodies
        self.spheres = [
          sp.Sphere([0, 0, 0], [0, 0, 5], 20000, 10, (1, 0, 0, 1)),
          sp.Sphere([0, 30, 0], [20, 0, 0], 5, 2, (0, 1, 0, 1)),
          sp.Sphere([0, 50, 0], [18, 0, 0], 20, 4, (0, 0, 1, 1)),
          sp.Sphere([0, 80, 0], [-15, 0, 0], 50, 6, (1, 0, 1, 1)),
          sp.Sphere([0, 120, 0], [10, 0, 0], 40, 4, (0.6, 0.6, 1, 1))
        ]
        
        # Sets Camera
        self.camera = camera.Camera(self.simWin, [0.0, 0.0, 100.0])