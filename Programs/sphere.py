import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from collections import deque

class Sphere:
    def __init__(self, position, velocity, mass, radius, color):
        self.position = np.array(position, dtype=np.float32)
        self.radius = float(radius)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
        self.color = color
        self.trail = deque(maxlen=1000)

    def update(self, force, dt):
        # Updates Body's attributes
        
        acceleration = force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt
        self.trail.append(self.position.copy())

    def draw_sphere(self):
        # Draws a Sphere for rendring.
        
        glPushMatrix()
        glTranslatef(float(self.position[0]), float(self.position[1]), float(self.position[2]))
        quad = gluNewQuadric()
        gluQuadricNormals(quad, GLU_SMOOTH)
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, self.color)
        gluSphere(quad, self.radius, 24, 24)
        gluDeleteQuadric(quad)
        glPopMatrix()
        
        # draws shpere trails
        if len(self.trail) > 1:
            glBegin(GL_LINE_STRIP)
            for i, pos in enumerate(self.trail):
                alpha = (i + 1) / len(self.trail)  
                glColor4f(1, 1, 1, 1)
                glVertex3f(pos[0], pos[1], pos[2])
            glEnd()