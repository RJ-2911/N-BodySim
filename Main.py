import pygame
import gui.components as c
import gui.show as s
import gui.event as e
import gui.dynamicComponents as dc

pygame.init()

# main window
window = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("N-Body Simulation")
icon = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon)
    
# mainloop
while dc.Boolean.is_running:
    window.fill((c.Color.primary))
    
    # event handler
    for event in pygame.event.get():
        e.EventHandler.eventhandler(event)

    # show different screens or panles or frames
    s.Show.info_panel(window)
    s.Show.play_pause_buttons(window)
    s.Show.add_context(window)

    pygame.display.update()

pygame.quit()