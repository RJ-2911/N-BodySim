import numpy as np   

class Physics:
    
    def __init__(self, simWin):
        self.simWin = simWin
        
    
    def compute_forces(self, bodies, G=1.0):
        # Computes Gravitaional Forces among 2 relative
        
        n = len(bodies)
        forces = [np.zeros(3) for _ in range(n)]
        eps = 0.1  # softening length

        for i in range(n):
            for j in range(i + 1, n):
                r_vec = bodies[j].position - bodies[i].position
                r2 = np.dot(r_vec, r_vec)  # squared distance
                if r2 == 0:
                    continue
                denom = (r2 + eps**2)**1.5
                force = G * bodies[i].mass * bodies[j].mass * r_vec / denom

                forces[i] += force
                forces[j] -= force
        return forces

    def calcForce(self, spheres, dt):
        # Compiles all Relative Forces on the bodies
        
        forces = self.compute_forces(spheres)
        for sphere, force in zip(spheres, forces):
            sphere.update(force, dt)  