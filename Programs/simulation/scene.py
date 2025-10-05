import simulation.sphere as sp
import simulation.camera as camera

class Scene:
    def __init__(self, simWin):
        self.simWin = simWin
        
        
        self.spheres = [
            sp.Sphere([30, 0, 0], [-5, 5, 0], 2000, 3, (1, 0.6, 0, 1)),
            sp.Sphere([0, 30, 0], [0, -5, 5], 2000, 3, (0, 1, 0.6, 1)),
            sp.Sphere([0, 0, 30], [5, 0, -5], 2000, 3, (0.6, 0, 1, 1)),
        ]
        
        
        self.camera = camera.Camera(self.simWin, [0.0, 0.0, 100.0])