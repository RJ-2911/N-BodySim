import pygame
from gui.components import *
from gui.dynamicComponents import *

pygame.init()

class Show:

    # show different panels respective to their name
    def info_panel(surface):

        # loading postion and dimensions
        x = CAS.info_surface[0]
        y = CAS.info_surface[1] + 10    # top padding
        w = CAS.info_surface[2] - 10    # right padding
        h = CAS.info_surface[3]
        pygame.draw.rect(surface, Color.primaryV, (x,y,w,h), 0, 10)

        # loading postion for (information panel) text
        x = x + 10      # top padding
        y = y + 10      # left padding
        surface.blit(String.info, (x,y))

        # break line
        x1 = CAS.info_surface[0]
        x2 =  CAS.info_surface[0] + w  - 2    # till the width, -2 for adjustments
        y = y + String.font_size + 10       # top padding
        pygame.draw.line(surface, Color.white, (x1, y), (x2, y))

    def play_pause_buttons(surface):
        if Boolean.is_playing:
        # if is playing show pause button
            surface.blit(Image.minus5x, CAS.minus5x)
            surface.blit(Image.pause, CAS.play_pause)
            surface.blit(Image.plus5x, CAS.plus5x)
        else:
        # else show play button
            surface.blit(Image.play, CAS.play_pause)
    
    def add_context(surface):
        if Boolean.is_add_context:
        # show add context menu when boolean is true, controlled by Event handler
            pygame.draw.rect(surface, Color.primaryV, CAS.add_context, 0, 2)
            surface.blit(String.add, (CAS.add_context[0]+5, CAS.add_context[1]+5))

    def remove_change_context(surface):
        if Boolean.is_remove_change_context:
        # show remove change context menu when boolean is true, controlled by Event handler
        # yet to implement
            pass

    def add_form(surface):
        # show add form
        pass

    def change_form(surface):
        # show change form
        pass