import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def draw_sphere(x, y, z, radius):
    quad = gluNewQuadric()
    glPushMatrix()
    glTranslatef(x, y, z)
    gluSphere(quad, radius, 32, 16)
    glPopMatrix()
    gluDeleteQuadric(quad)

class Body:
    def __init__(self, position, velocity, mass, radius, color):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
        self.radius = radius
        self.color = color

    def update(self, force, dt):
        acceleration = force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

    def draw(self):
        glColor3fv(self.color)
        draw_sphere(*self.position, self.radius)

def gravitationalforce(body1, body2, G=1.0):
    r_vec = body2.position - body1.position
    distance = np.linalg.norm(r_vec)
    if distance == 0:
        return np.zeros(3)
    force_mag = G * body1.mass * body2.mass / (distance ** 2)
    force_dir = r_vec / distance
    return force_mag * force_dir

def main():
    pg.init()
    display = (1200, 800)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, 0.0, -20)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (5, 5, 10, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.7, 0.7, 0.7, 1.0))


    body1 = Body(position=[-8, 0, 0], velocity=[0, 5, 0], mass=2, radius=0.3, color=(0.2, 0.6, 1.0))
    body2 = Body(position=[0, 0, 0], velocity=[0, 0, 0], mass=200, radius=1, color=(1.0, 0.4, 0.2))

    clock = pg.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pg.event.get():
            if event.type == QUIT:
                running = False


        force_on_1 = gravitationalforce(body1, body2)
        force_on_2 = -force_on_1


        body1.update(force_on_1, dt)
        body2.update(force_on_2, dt)



        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        body1.draw()
        body2.draw()
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
