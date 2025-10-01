import pygame as pg
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import sphere as sp
import camera
import scene as sc
import renderer as rd
import events as ev
import physicsCalc as phy



# Holds Everything For Simulation Window
class SimWindow:
    def __init__(self):
       
        # Initializing Classes for all files to access.
        self.physics = phy.Physics(self)
        self.scene = sc.Scene(self)    
        self.renderer = rd.Renderer(self, display[0], display[1])
        self.event = ev.Events(self)
        
        # Inititalizing attributes for simulation window.
        display = (1900, 1200)    
        self.setWindow(display)
        self.clock = pg.time.Clock()
        self.angle = 0.0
        self.running = True    
    

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
            dt = self.clock.tick(60) / 1000.0  # seconds per frame
            self.physics.calcForce(self.scene.spheres, dt)
            self.event.handle_events(dt)

            self.renderer.drawGL(self.scene.spheres, self.scene.camera, self.angle)
            pg.display.flip()
            self.angle += 30.0 * dt  # spin speed (deg/sec)

        pg.quit()