import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sphere as sp

class SimWindow:
    
    def __init__(self):
        
        pg.init()
        display = (800, 600)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)

        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -6)  # move camera back

        self.initGL()

        angle = 1

        running = True
        while running:
            for event in pg.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_UP:   # grow
                        sp.radius += 0.1
                    elif event.key == K_DOWN:  # shrink
                        sp.radius = max(0.1, sp.radius - 0.1)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glPushMatrix()
            glRotatef(angle, 0, 1, 1)  # rotate around axes
            sp.draw_sphere(0, 0, 0, sp.radius)

            glPopMatrix()

            angle += 1  # increment angle for rotation
            
            pg.display.flip()
            pg.time.wait(10)
    
    def initGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1)) # R, G, B, Alpha
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1)) # R, G, B, Alpha
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.4, 0.6, 0.9, 1.0)) # R, G, B, Alpha

    

    def quit(self):
        pg.quit()
        
if __name__ == "__main__":
    myApp = SimWindow()