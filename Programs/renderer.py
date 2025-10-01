from OpenGL.GL import *
from OpenGL.GLU import *

class Renderer:
    def __init__(self, simWin, width, height):
        # basic GL setup
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE)      # keep normals ok if we scale anything
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        # light position and colors
        glLightfv(GL_LIGHT0, GL_POSITION, (5.0, 5.0, 5.0, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))

        # nice clear color
        glClearColor(0.05, 0.05, 0.08, 1.0)

        # material default
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (0.3, 0.3, 0.3, 1.0))
        glViewport(0, 0, width, height)
                
        self.showGridXY = True
        self.showGridYZ = True
        self.showGridZX = True
        self.showAxes = True
    
    def draw_axes(self, camera_obj, size, distance): # Big Distance = Small Crosshair
           
        base = camera_obj.position + camera_obj.forwards * distance
        glPushAttrib(GL_ENABLE_BIT | GL_LINE_BIT | GL_CURRENT_BIT)
        glDisable(GL_LIGHTING)
        glDisable(GL_DEPTH_TEST)
        glLineWidth(3.0)
        glBegin(GL_LINES)

        # X axis
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(base[0], base[1], base[2])
        glVertex3f(base[0] + size, base[1], base[2])

        # Y axis 
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(base[0], base[1], base[2])
        glVertex3f(base[0], base[1] + size, base[2])

        # Z axis 
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(base[0], base[1], base[2])
        glVertex3f(base[0], base[1], base[2] + size)

        glEnd()
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glPopAttrib()

    def draw_grid(self, size, step):   
        glDisable(GL_LIGHTING)
        glColor3f(0.3, 0.3, 0.3) 
        glBegin(GL_LINES)
        
        if self.showGridXY:
            for i in range(-size, size + 1, step):
                glVertex3f(i, -size, 0)
                glVertex3f(i,  size, 0)
                glVertex3f(-size, i, 0)
                glVertex3f( size, i, 0)

        if self.showGridZX:
            for i in range(-size, size + 1, step):
                glVertex3f(i, 0, -size)
                glVertex3f(i, 0,  size)
                glVertex3f(-size, 0, i)
                glVertex3f( size, 0, i)

        if self.showGridYZ:
            for i in range(-size, size + 1, step):
                glVertex3f(0, i, -size)
                glVertex3f(0, i,  size)
                glVertex3f(0, -size, i)
                glVertex3f(0,  size, i)
        glEnd()
        glEnable(GL_LIGHTING)
    
    def drawGL(self, spheres, camera_obj, angle):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Use the Camera's gluLookAt
        camera_obj.apply_view()
        
        if self.showAxes:
            self.draw_axes(camera_obj, 1, 20)
        self.draw_grid(50000, 100)


        for sphere in spheres:
            sphere.draw_sphere()
