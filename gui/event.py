import pygame
from gui.components import *
from gui.dynamicComponents import *

pygame.init()

class Events:

    mouse_pos = [0, 0]
    key_press = ''

    def isClicked(lst):
    # accept a hitbox and return if mouse clicked in it or not 
        mouse_pos = Events.mouse_pos
        if mouse_pos[0]>=lst[0] and mouse_pos[1]>=lst[1] and mouse_pos[0]<=lst[0]+lst[2] and mouse_pos[1]<=lst[1]+lst[3]:
            return True
        else:
            return False

class EventHandler:
        
    def eventhandler(event):
        # handle window close event
        if event.type == pygame.QUIT:
            Boolean.is_running = False

        # mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            Events.mouse_pos = pygame.mouse.get_pos()

            # left click events
            if event.button == 1:

                # add context selection
                if Events.isClicked(Hitbox.add_context):
                    print("Hello World")        # temporary
                    Boolean.is_add_context = False
                else:
                # clear context menu
                    List.clear_context_CAS(CAS.add_context, Hitbox.add_context)
                    Boolean.is_add_context = False

                # play pause buttons
                if Events.isClicked(Hitbox.play_pause):
                    Boolean.is_playing = not Boolean.is_playing

                # remove change context apperance
                # yet to implement


            # right click events
            if event.button == 3:

                # add context menu appearance
                if Events.isClicked(CAS.main_surface):
                    List.generate_context_CAS(CAS.add_context, Hitbox.add_context)
                    Boolean.is_add_context = True


# Some Lists and methods
class List:
    def generate_context_CAS(*args):
    # generate new context CAS if CAS exceeds the boundary of main screen else return old CAS
        for arg in args:
            mouse_pos = Events.mouse_pos
            x=mouse_pos[0]
            y=mouse_pos[1]
            if mouse_pos[0]+100 >= CAS.main_surface[2]:
                x = mouse_pos[0] - 100
            if mouse_pos[1]+30 >= CAS.main_surface[3]:
                y = mouse_pos[1] - 30
            arg[:] = [x,y, arg[2], arg[3]]
    
    def clear_context_CAS(*args):
    # clear defined context
        for arg in args:
            arg[:] = [5000,5000,arg[2],arg[3]]