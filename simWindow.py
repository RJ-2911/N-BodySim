import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class SimWindow:

    def __init__(self):
        
        pg.init()
        pg.display.set_mode((950, 540), pg.OPENGL, pg.DOUBLEBUF)
        pg.display.set_caption("Simulation Window")
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.1, 0.2, 1)
        self.mainLoop()

    def mainLoop(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                
            # Refresh Screen
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()  
            
            # FPS
            self.clock.tick(60)
        
        self.quit()

    def quit():
        pg.quit()
        
if __name__ == "__main__":
    myApp = SimWindow()