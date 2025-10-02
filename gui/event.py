import pygame
from gui.models import *

pygame.init()

class Events:

    mouse_pos = [0, 0]
    key_press = ''

    def buttonInteraction(*args):
        click_list = [PlayPause, Reset, Fast]
        mouse_pos = Events.mouse_pos
        if InfoControlPanel.is_visible:
            for i in range(len(click_list)):
                obj = click_list[i]
                cas = obj.cas
                if mouse_pos[0]>=cas[0] and mouse_pos[1]>=cas[1] and mouse_pos[0]<=cas[0]+cas[2] and mouse_pos[1]<=cas[1]+cas[3]:
                    obj.is_hover = True
                    if len(args) == 1:
                        obj.function()
                else:
                    obj.is_hover = False
        
        click_list2 = [Hide, Add]
        for obj in click_list2:
            if obj.is_visible:
                cas = obj.cas
                if mouse_pos[0]>=cas[0] and mouse_pos[1]>=cas[1] and mouse_pos[0]<=cas[0]+cas[2] and mouse_pos[1]<=cas[1]+cas[3]:
                    obj.is_hover = True
                    if len(args) == 1:
                        obj.function()
                else:
                    obj.is_hover = False
                    if len(args) == 1:
                        obj.is_visible = False

    
    def rightClickInteraction():
        if Events.mouse_pos[0] > Surfaces.object_surface[0]:
            Add.is_visible = True
            Add.mouse_pos = Events.mouse_pos
    


class EventHandler:
        
    def eventhandler(event):
        # handle window close event
        if event.type == pygame.QUIT:
            Surfaces.is_running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Surfaces.is_running = False
        
        # button interaction
        Events.mouse_pos = pygame.mouse.get_pos()
        Events.buttonInteraction()
        # Events.interaction()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Events.buttonInteraction(1)
            elif event.button == 3:
                Events.rightClickInteraction()



    