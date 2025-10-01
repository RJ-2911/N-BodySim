import pygame as pg
from pygame.locals import *

import simWindow as sw



class Events:
    def __init__(self, simWin):
        self.simWin = simWin
    
    def handle_events(self, dt):
        
        pg.mouse.set_visible(False)
        pg.event.set_grab(True)
        for event in pg.event.get():
            if event.type == QUIT:
                self.simWin.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.simWin.running = False
                elif event.key == K_1:
                    self.simWin.renderer.showGridXY = not self.simWin.renderer.showGridXY
                elif event.key == K_2:
                    self.simWin.renderer.showGridYZ = not self.simWin.renderer.showGridYZ
                elif event.key == K_3:
                    self.simWin.renderer.showGridZX = not self.simWin.renderer.showGridZX
                elif event.key == K_4:
                    self.simWin.renderer.showAxes = not self.simWin.renderer.showAxes
            elif event.type == MOUSEMOTION:
                dx, dy = event.rel  
                sensitivity = 0.14   
                self.simWin.scene.camera.rotate(dtheta=dx * sensitivity, dphi=-dy * sensitivity)

        keys = pg.key.get_pressed()
        if self.simWin.scene.camera.move_speed_base <= 0:
                self.simWin.scene.camera.move_speed_base = 5
        move_speed = self.simWin.scene.camera.move_speed_base * dt
        rot_speed = 60.0 * dt 

        # movement (local camera space)
        if keys[K_s]:
            self.simWin.scene.camera.move_local(dz=-move_speed) 
        if keys[K_w]:
            self.simWin.scene.camera.move_local(dz=move_speed)
        if keys[K_a]:
            self.simWin.scene.camera.move_local(dx=-move_speed)
        if keys[K_d]:
            self.simWin.scene.camera.move_local(dx=move_speed)
        if keys[K_LSHIFT]:
            self.simWin.scene.camera.move_local(dy=-move_speed)
        if keys[K_SPACE]:
            self.simWin.scene.camera.move_local(dy=move_speed)
            
        # cmaera speed
        if keys[K_q]:
            self.simWin.scene.camera.move_speed_base += 5
        if keys[K_e]:
            self.simWin.scene.camera.move_speed_base -= 5

        # rotation yaw/pitch
        if keys[K_LEFT]:
            self.simWin.scene.camera.rotate(dtheta=-rot_speed)
        if keys[K_RIGHT]:
            self.simWin.scene.camera.rotate(dtheta=rot_speed)
        if keys[K_UP]:
            self.simWin.scene.camera.rotate(dphi=rot_speed)
        if keys[K_DOWN]:
            self.simWin.scene.camera.rotate(dphi=-rot_speed)
            