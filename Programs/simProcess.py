# Under Construction

import numpy as np

class CelestialBody:
    def __init__(self, position, velocity, mass = 1):
        self.poition = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
    
    def update(self, acceleration, dt):
        self.velocity += acceleration * dt
        self.poition += self.velocity * dt
        
        
# Constants

G = (6.67 * (pow(10, -11))) # Gravitational Constant
dt = 0.01 # Rate of change of time, basically 'delta t'
t = 0 # Initial time 
sofetening = 0.1 # Prevention of 0 division in force calculation



