import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *

class Sphere:
    def __init__(self, position, velocity, mass, radius, color):
        self.position = np.array(position, dtype=np.float32)
        self.radius = float(radius)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
        self.color = color

    def update(self, force, dt):
        acceleration = force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

    def draw_sphere(self):
        """
        Draws the sphere at its own position with its own radius.
        This function expects the caller to manage the GL matrix stack.
        """
        glPushMatrix()
        glTranslatef(float(self.position[0]), float(self.position[1]), float(self.position[2]))
        quad = gluNewQuadric()
        gluQuadricNormals(quad, GLU_SMOOTH)
        # Note: using 24/24 slices/stacks for reasonable quality
        gluSphere(quad, self.radius, 24, 24)
        gluDeleteQuadric(quad)
        glPopMatrix()