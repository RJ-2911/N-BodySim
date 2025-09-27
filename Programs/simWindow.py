import pygame as pg
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import sphere as sp
import camera
import physicsCalc as pc

# Simple scene holder
class Scene:
    def __init__(self):
        # Put spheres inside the view frustum (z negative is forward)
        self.spheres = [
            sp.Sphere([0, 0, 0], [0, 0, 0], 1200, 5, (1, 0.4, 0.0, 1)),
            sp.Sphere([0, 40, 0], [6, 0, 0], 5, 3, (0.6, 0.4, 1, 1))
        ]
        # Camera placed back on +Z, looking towards -Z by default (theta=0)
        self.camera = camera.Camera([0.0, 0.0, 100.0])

    def update(self, dt):
        # future physics/animation updates could go here
        pass

class Renderer:
    def __init__(self, width, height):
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
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (0.4, 0.6, 0.9, 1.0))
        glViewport(0, 0, width, height)

    def drawGL(self, spheres, camera_obj, angle):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Use the Camera's gluLookAt
        camera_obj.apply_view()

        # optional spin applied per object (keeps transforms local)
        for i, s in enumerate(spheres):
            glPushMatrix()
            # if you want each sphere to slowly spin around its own Y axis:
            glTranslatef(float(s.position[0]), float(s.position[1]), float(s.position[2]))
            glRotatef(angle + i * 10.0, 0.0, 1.0, 0.0)
            # draw sphere centered at origin now (because we translated)
            quad = gluNewQuadric()
            gluQuadricNormals(quad, GLU_SMOOTH)
            gluSphere(quad, s.radius, 24, 24)
            gluDeleteQuadric(quad)
            glPopMatrix()

class SimWindow:
    def __init__(self):
        pg.init()
        display = (1900, 1200)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)
        pg.display.set_caption("N-Body - Debug Camera & Spheres")

        # Projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, (display[0] / display[1]), 0.1, 500.0)
        glMatrixMode(GL_MODELVIEW)

        self.renderer = Renderer(display[0], display[1])
        self.scene = Scene()
        self.clock = pg.time.Clock()
        
        self.angle = 0.0
        self.running = True
        self.main_loop()
    
    def calcForce(self, dt):
         force_on_1 = pc.gravitationalforce(self.scene.spheres[0], self.scene.spheres[1])
         force_on_2 = -force_on_1
         self.scene.spheres[0].update(force_on_1, dt)
         self.scene.spheres[1].update(force_on_2, dt)

    def handle_events(self, dt):
        # keyboard controls for camera
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

        keys = pg.key.get_pressed()
        move_speed = 5.0 * dt
        rot_speed = 60.0 * dt  # degrees per second

        # movement (local camera space)
        if keys[K_w]:
            self.scene.camera.move_local(dz=-move_speed)  # forward (negative because forwards goes -Z)
        if keys[K_s]:
            self.scene.camera.move_local(dz=move_speed)
        if keys[K_a]:
            self.scene.camera.move_local(dx=-move_speed)
        if keys[K_d]:
            self.scene.camera.move_local(dx=move_speed)
        if keys[K_q]:
            self.scene.camera.move_local(dy=-move_speed)
        if keys[K_e]:
            self.scene.camera.move_local(dy=move_speed)

        # rotation yaw/pitch
        if keys[K_LEFT]:
            self.scene.camera.rotate(dtheta=-rot_speed)
        if keys[K_RIGHT]:
            self.scene.camera.rotate(dtheta=rot_speed)
        if keys[K_UP]:
            self.scene.camera.rotate(dphi=rot_speed)
        if keys[K_DOWN]:
            self.scene.camera.rotate(dphi=-rot_speed)

    def main_loop(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0  # seconds per frame
            self.calcForce(dt)
            self.handle_events(dt)
            self.scene.update(dt)

            # debug prints (one-liners)
            # Uncomment to see camera info in console:
            # print(f"Cam pos: {self.scene.camera.position}, forward: {self.scene.camera.forwards}")

            self.renderer.drawGL(self.scene.spheres, self.scene.camera, self.angle)
            pg.display.flip()
            self.angle += 30.0 * dt  # spin speed (deg/sec)

        self.quit()

    def quit(self):
        pg.quit()

if __name__ == "__main__":
    SimWindow()
