import pygame as pg
import threading

import gui.components as comp
import gui.methods as meth
import gui.body as bd

# Surface management for GUI layout
class Surfaces:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.main_surface = [0, 0]        # Resolution (1536, 1080)
        self.object_surface = [0, 0]
        self.info_surface = [0, 0]
        self.control_surface = [0, 0]
        self.is_running = False
        self.is_playing = False
        self.object_panel = [0, 0]

    def initialize(self):
        # Initialize surface dimensions and positions
        self.info_control_surface = [0, 0, 400, 850]
        self.info_surface = [10, 10, 400, 700]
        self.control_surface = [0, 710, 400, 150]
        self.object_surface = [400, 0, self.main_surface[0]-400, self.main_surface[1]]
        self.is_running = True
        self.object_panel = [10, 60, 380, 120]

# Main information and control panel
class InfoControlPanel:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.is_visible = True
        
    def show(self, surface):
        if not self.is_visible:
            return None

        InfoPanel(self.guiWin).show(surface)
        self.guiWin.play_pause.show(surface)
        self.guiWin.reset.show(surface)
        self.guiWin.fast.show(surface)
        self.guiWin.add.show(surface)  
        ObjectInfo(self.guiWin).show(surface)

# Additional panels and overlays
class OtherPanel:
    def __init__(self, gui_window):
        self.gui_window = gui_window

    def show(self, surface):
        self.gui_window.add.show(surface)
        self.gui_window.add_form.show()

# Information display panel
class InfoPanel:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        
    def show(self, surface):
        cas = self.guiWin.surfaces.info_surface
        # Loading position and dimensions
        x = cas[0]
        y = cas[1]
        w = cas[2]
        h = cas[3]
        pg.draw.rect(surface, comp.Color.primary_v, (x, y, w, h), 0, 10)

        # Loading position for information panel text
        x = x + 10      # Top padding
        y = y + 10      # Left padding
        surface.blit(comp.String.info, (x, y))

        # Break line
        x1 = cas[0]
        x2 = cas[0] + w - 2   # Till the width, -2 for adjustments
        y = y + comp.String.font_size + 10       # Top padding
        pg.draw.line(surface, comp.Color.white, (x1, y), (x2, y))

# Play/Pause control button
class PlayPause:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.cas = [168, 743, 64, 64]
        self.is_hover = False

    def show(self, surface):
        cas = [self.guiWin.surfaces.control_surface[0]+168, self.guiWin.surfaces.control_surface[1]+43]
        if self.guiWin.surfaces.is_playing:
            if self.is_hover:
                surface.blit(comp.Image.pause_l, cas)
            else:
                surface.blit(comp.Image.pause, cas)
        else:
            if self.is_hover:
                surface.blit(comp.Image.play_l, cas)
            else:
                surface.blit(comp.Image.play, cas)    
    
    def function(self):
        self.guiWin.surfaces.is_playing = not self.guiWin.surfaces.is_playing
        if self.guiWin.surfaces.is_playing:
            self.guiWin.mainObj.sim_speed = 10
        else:
            self.guiWin.mainObj.sim_speed = 0
            

# Reset control button
class Reset:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.cas = [52, 743, 64, 64]
        self.is_hover = False

    def show(self, surface):
        cas = [self.guiWin.surfaces.control_surface[0]+52, self.guiWin.surfaces.control_surface[1]+43]
        if self.guiWin.surfaces.is_playing:
            if self.is_hover:
                surface.blit(comp.Image.reset_l, cas)
            else:
                surface.blit(comp.Image.reset, cas)
    
    def function(self):
        print("Reset Button Clicked")

# Fast forward control button
class Fast:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.cas = [284, 743, 64, 64]
        self.is_hover = False

    def show(self, surface):
        cas = [self.guiWin.surfaces.control_surface[0]+284, self.guiWin.surfaces.control_surface[1]+43]
        if self.guiWin.surfaces.is_playing:
            if self.is_hover:
                surface.blit(comp.Image.fast_l, cas)
            else:
                surface.blit(comp.Image.fast, cas)
    
    def function(self):
        print("Fast Button Clicked")

# Hide/show panel button
class Hide:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.cas = [0, 0, 10, 10]
        self.is_visible = True
        self.is_hover = False
       
    def function(self):
        self.guiWin.info_control_panel.is_visible = not self.guiWin.info_control_panel.is_visible
        if self.guiWin.info_control_panel.is_visible:
            self.guiWin.surfaces.object_surface = [400, 0, self.guiWin.surfaces.main_surface[0]-400, self.guiWin.surfaces.main_surface[1]]
        else:
            self.guiWin.surfaces.object_surface = [0, 0, self.guiWin.surfaces.main_surface[0], self.guiWin.surfaces.main_surface[1]]

# Add object context menu
class Add:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.cas = [150, 660, 100, 40]  # Position near bottom of info panel
        self.is_visible = True
        self.is_hover = False

    def show(self, surface):
        if not self.is_visible:
            return

        x, y, w, h = self.cas
        color = comp.Color.primary_vl if self.is_hover else comp.Color.primary_v
        pg.draw.rect(surface, color, (x, y, w, h), 0, 5)
        text_surface = comp.String.add_l if self.is_hover else comp.String.add
        surface.blit(text_surface, (x + 25, y + 10))

    def function(self):
        self.guiWin.add_form.is_visible = True

# Add form dialog
class AddForm:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.is_visible = False
        self.object = []
        self.method = meth.Method(self.guiWin)  # Initialize Method to access result_list
        
    def show(self):
        if self.is_visible:
            thread1 = threading.Thread(target=self._show_add_form)
            thread1.start()
            thread1.join()  # Wait for form to close to get result_list
            if self.method.result_list:  # Check if result_list has data
                # Normalize color values from (0-255) to (0.0-1.0)
                body_data = self.method.result_list
                position, velocity, mass, radius, color = body_data
                normalized_color = (color[0]/255.0, color[1]/255.0, color[2]/255.0, color[3])
                normalized_body_data = [position, velocity, mass, radius, normalized_color]
                self.guiWin.body.add_object(normalized_body_data)
            self.is_visible = False  # Reset visibility after processing

    def _show_add_form(self):
        self.method.show_add_form()  # Run Tkinter form to collect user input

# Object information display
class ObjectInfo:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.cas = [0, 0, 0, 0]
        
    def show(self, surface):
        # Use sim_spheres to display current simulation state
        for i, sphere in enumerate(self.guiWin.body.sim_spheres):
            cas = self.guiWin.surfaces.object_panel
            x = cas[0]
            y = cas[1]
            w = cas[2]
            h = cas[3]
            x += 10
            y += 5
            pg.draw.rect(surface, comp.Color.primary, (x, y, w, 105), 0, 2)
            
            x += 5
            y += 5
            pos = sphere[0]  # position
            vel = sphere[1]  # velocity
            mass = sphere[2]  # mass
            radius = sphere[3]  # radius
            color = sphere[4]  # color
            surface.blit(meth.Method(self.guiWin).string_show("Position:", pos[0], pos[1], pos[2]), (x, y))
            y += 25
            surface.blit(meth.Method(self.guiWin).string_show("Velocity:", vel[0], vel[1], vel[2]), (x, y))            
            y += 25
            surface.blit(meth.Method(self.guiWin).string_show("Mass:", mass), (x, y))
            y += 25
            surface.blit(meth.Method(self.guiWin).string_show("Radius:", radius), (x, y))
           
            self.guiWin.surfaces.object_panel[1] += 120  # Spacing for fields
        self.guiWin.surfaces.object_panel = [10, 60, 380, 50]