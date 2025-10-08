import pygame as pg
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import simulation.scene as sc
import simulation.renderer as rd
import simulation.events as ev
import simulation.physicsCalc as phy
from simulation.sphere import Sphere

# Holds Everything For Simulation Window
class SimWindow:
    def __init__(self, body_to_sim_queue, sim_to_body_queue):
        # Store queues for communication
        self.body_to_sim_queue = body_to_sim_queue
        self.sim_to_body_queue = sim_to_body_queue
        
        # Initializing attributes for simulation window
        display = (800, 600)    
        self.setWindow(display)
        self.clock = pg.time.Clock()
        self.angle = 0.0
        self.running = True   
        self.sim_speed = 10 # Keep below 100, if 100+ then calculation precision suffers and simulation breaks
       
        # Initializing Classes for all files to access
        self.physics = phy.Physics(self)
        self.scene = sc.Scene(self)    
        self.renderer = rd.Renderer(self, display[0], display[1])
        self.event = ev.Events(self)
        
    def setWindow(self, display):
        # Sets up the Simulation Window
        pg.init()
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)
        pg.display.set_caption("N-Body - Debug Camera & Spheres")

        # Projection of simulation space
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, (display[0] / display[1]), 0.1, 10000.0)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
      
    def main_loop(self):
        # Keeps the Window running and updated
        while self.running:
            dt = 0.001  # seconds per frame
            scaled_dt = dt * self.sim_speed
            self.physics.calcForce(self.scene.spheres, scaled_dt)
            self.event.handle_events(60/1000)

            # Check queue for new body data from GUI
            while not self.body_to_sim_queue.empty():
                body_data = self.body_to_sim_queue.get()
                # Assuming body_data is a tuple: (position, velocity, mass, radius, color)
                self.scene.spheres.append(Sphere(
                    body_data[0],  # position
                    body_data[1],  # velocity
                    body_data[2],  # mass
                    body_data[3],  # radius
                    body_data[4]   # color
                ))

            # Send current spheres data to GUI
            spheres_data = [
                (sphere.position, sphere.velocity, sphere.mass, sphere.radius, sphere.color)
                for sphere in self.scene.spheres
            ]
            self.sim_to_body_queue.put(spheres_data)

            self.renderer.drawGL(self.scene.spheres, self.scene.camera, self.angle)
            pg.display.flip()
            self.angle += 30.0 * dt  # spin speed (deg/sec)

        pg.quit()