import pygame as pg
from pygame.locals import *

import gui.components as comp
import gui.event as ev
import gui.models as mod
import gui.body as bd


# Main GUI Window for N-Body Simulation
class GuiWindow:
    def __init__(self):
        # Initialize main window
        self.window = pg.display.set_mode((420, 900)) 
        pg.display.set_caption("N-Body Simulation")
        icon = pg.image.load("resources/icon.png")
        pg.display.set_icon(icon)
        
        # Initialize surfaces
        self.surfaces = mod.Surfaces(self)
        self.surfaces.main_surface = self.window.get_size()
        self.surfaces.initialize()
        
        # Body handler
        self.body = bd.Body(self)
        
        # --- Instantiate all GUI objects here ---
        self.play_pause = mod.PlayPause(self)
        self.reset = mod.Reset(self)
        self.fast = mod.Fast(self)
        self.hide = mod.Hide(self)
        self.add = mod.Add(self)
        self.add_form = mod.AddForm(self)

        # Panels
        self.info_control_panel = mod.InfoControlPanel(self)
        self.other_panel = mod.OtherPanel(self)

        # Events and handler
        self.events = ev.Events(self)
        self.event_handler = ev.EventHandler(self)

        # Run state
        self.running = True

    def main_loop(self):
        while self.running:
            self.window.fill(comp.Color.primary)

            # Handle events
            for event in pg.event.get():
                self.event_handler.handle_event(event)

            # Draw UI
            self.info_control_panel.show(self.window)
            self.other_panel.show(self.window)

            pg.display.update()

        pg.quit()
