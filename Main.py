import pygame
from gui.components import Color
from gui.event import EventHandler
from gui.models import *

pygame.init()

# main window
window = pygame.display.set_mode((0, 0))    # (0,0) set to fullscreen
pygame.display.set_caption("N-Body Simulation")
icon = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon)
    
Surfaces.main_surface = window.get_size()
Surfaces.initialize()

# mainloop
while Surfaces.is_running:
    window.fill((Color.primary))
    
    # event handler
    for event in pygame.event.get():
        EventHandler.eventhandler(event)

    # show info panel
    InfoControlPanel.show(window)
    OtherPanel.show(window)


    pygame.display.update()

pygame.quit()