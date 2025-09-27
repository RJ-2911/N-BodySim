from OpenGL.GL import *
from OpenGL.GLU import *

x = 0
y = 0
z = 0
radius = 1

def draw_sphere(x, y, z, radius):
        glPushMatrix()
        glTranslatef(x, y, z)   # move sphere to position
        quad = gluNewQuadric()
        gluQuadricNormals(quad, GLU_SMOOTH)
        gluSphere(quad, radius, 32, 32) #  sphere object, size, x, y (subdivisions: higher = smoother = more POWER!!!)
        gluDeleteQuadric(quad)
        glPopMatrix() 