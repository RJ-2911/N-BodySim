from gui.components import *

class Surfaces:
    main_surface = [0, 0, 900, 700]
    info_control_surface = [main_surface[2], 0, 300, 700]
    info_surface = [info_control_surface[0], 0, 300, 600]
    control_surface = [info_control_surface[0], 600, 300, 100]
    is_fullscreen = False

class InfoPanel:
    cas = Surfaces.info_surface
    
    def show(self, surface):
        if not Surfaces.is_fullscreen:
            return None
        # loading postion and dimensions
        x = self.cas[0]
        y = self.cas[1] + 10    # top padding
        w = self.cas[2] - 10    # right padding
        h = self.cas[3]
        pygame.draw.rect(surface, Color.primaryV, (x,y,w,h), 0, 10)

        # loading postion for (information panel) text
        x = x + 10      # top padding
        y = y + 10      # left padding
        surface.blit(String.info, (x,y))

        # break line
        x1 = self.cas[0]
        x2 =  self.cas[0] + w  - 2    # till the width, -2 for adjustments
        y = y + String.font_size + 10       # top padding
        pygame.draw.line(surface, Color.white, (x1, y), (x2, y))

class PlayPause:
    cas = [Surfaces.control_surface[0]+118, Surfaces.control_surface[1]+18]
    isPlaying = False

    def show(self, surface):
        if self.is_playing:
            surface.blit(Image.pause, self.cas)

        else:
        # else show play button
            surface.blit(Image.play, self.cas)    

class Add:
    cas = [0,0,100,30]
    isVisible = False

    def show(self, surface):
        if not self.isVisible:
            return None
        cas = Add.cas   # --remove--
        # cas = Method.generate_cas()   # --implement--
        # show add context menu when boolean is true, controlled by Event handler
        pygame.draw.rect(surface, Color.primaryV, cas, 0, 2)
        surface.blit(String.add, (cas[0]+5, cas[1]+5))

class Reset:
    cas = [0,0,100,30]
    isVisible = PlayPause.isPlaying
    def show(surface):
        cas = Reset.cas
        if PlayPause.is_playing:
        # if is playing show pause button
            surface.blit(Image.minus5x, cas)
        else:
        # else show play button
            surface.blit(Image.play, cas)
class FastForward:
    pass
class Change:
    pass
class AddForm:
    pass
class ObjectInfo:
    pass