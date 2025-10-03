from gui.components import *
from gui.methods import *
import threading
from gui.body import Body

class Surfaces:
    main_surface = [0,0]        # resolution(1536,1080)
    object_surface = [0,0]
    info_surface = [0, 0]
    control_surface = [0, 0]
    is_running = False
    is_playing = False
    object_panel = [0,0]

    def initialize():
        Surfaces.info_control_surface = [0,0,400,850]
        Surfaces.info_surface = [10,10,400,700]
        Surfaces.control_surface = [0,710,400,150]
        Surfaces.object_surface = [400, 0, Surfaces.main_surface[0]-400, Surfaces.main_surface[1]]
        Surfaces.is_running = True
        Surfaces.object_panel = [10, 60, 380, 50]

class InfoControlPanel:
    is_visible = True
    def show(surface):
        if not InfoControlPanel.is_visible:
            return None
        InfoPanel.show(surface)
        PlayPause.show(surface)
        Reset.show(surface)
        Fast.show(surface)
        ObjectInfo.show(surface)

class OtherPanel:
    def show(surface):
        Add.show(surface)
        AddForm.show()

class InfoPanel:
    def show(surface):
        cas = Surfaces.info_surface
        # loading postion and dimensions
        x = cas[0]
        y = cas[1]
        w = cas[2]
        h = cas[3]
        pygame.draw.rect(surface, Color.primaryV, (x,y,w,h), 0, 10)

        # loading postion for (information panel) text
        x = x + 10      # top padding
        y = y + 10      # left padding
        surface.blit(String.info, (x,y))

        # break line
        x1 = cas[0]
        x2 =  cas[0] + w -2   # till the width, -2 for adjustments
        y = y + String.font_size + 10       # top padding
        pygame.draw.line(surface, Color.white, (x1, y), (x2, y))

class PlayPause:
    cas = [168, 743, 64, 64]
    is_hover = False

    def show(surface):
        cas = [Surfaces.control_surface[0]+168, Surfaces.control_surface[1]+43]
        if Surfaces.is_playing:
            if PlayPause.is_hover:
                surface.blit(Image.pauseL, cas)
            else:
                surface.blit(Image.pause, cas)
        else:
            if PlayPause.is_hover:
                surface.blit(Image.playL, cas)
            else:
                surface.blit(Image.play, cas)    
    
    def function():
        Surfaces.is_playing = not Surfaces.is_playing

class Reset:
    cas = [52, 743, 64, 64]
    is_hover = False

    def show(surface):
        cas = [Surfaces.control_surface[0]+52, Surfaces.control_surface[1]+43]
        if Surfaces.is_playing:
            if Reset.is_hover:
                surface.blit(Image.resetL, cas)
            else:
                surface.blit(Image.reset, cas)
    
    def function():
        print("Reset Button Clicked")

class Fast:
    cas = [284, 743, 64, 64]
    is_hover = False

    def show(surface):
        cas = [Surfaces.control_surface[0]+284, Surfaces.control_surface[1]+43]
        if Surfaces.is_playing:
            if Fast.is_hover:
                surface.blit(Image.fastL, cas)
            else:
                surface.blit(Image.fast, cas)
    
    def function():
        print("Fast Button Clicked")

class Hide:
    cas = [0,0,10, 10]
    is_visible = True
    is_hover = False
       
    def function():
        InfoControlPanel.is_visible = not InfoControlPanel.is_visible
        if InfoControlPanel.is_visible:
            Surfaces.object_surface = [400, 0, Surfaces.main_surface[0]-400, Surfaces.main_surface[1]]
        else:
            Surfaces.object_surface = [0, 0, Surfaces.main_surface[0], Surfaces.main_surface[1]]

class Add:
    width = 100; height = 30
    cas = [0,0,0,0]
    mouse_pos = []
    is_visible = False
    is_hover = False

    def show(surface):
        if not Add.is_visible:
            return None
        cas = [Add.mouse_pos[0], Add.mouse_pos[1], Add.width, Add.height]
        cas = Method.adjust_context_CAS(cas, Surfaces.object_surface)
        Add.cas = cas
        # show add context menu when boolean is true, controlled by Event handler
        if Add.is_hover:
            pygame.draw.rect(surface, Color.primaryVL, cas, 0, 2)
            surface.blit(String.addL, (cas[0]+5, cas[1]+5))
        else:
            pygame.draw.rect(surface, Color.primaryV, cas, 0, 2)
            surface.blit(String.add, (cas[0]+5, cas[1]+5))
    
    def function():
        Add.is_visible = False
        AddForm.is_visible = True

class AddForm:
    is_visible = False
    object = []
    def show():
        if AddForm.is_visible:
            AddForm.is_visible = False      # Change it on your own risk
            m = Method()
            thread1 = threading.Thread(target=m.showAddForm)
            thread1.start()

class ObjectInfo:
    cas = [0,0,0,0]
    def show(surface):
        for i in Body.original_list:
            cas = Surfaces.object_panel
            x=cas[0]; y=cas[1]; w=cas[2]; h=cas[3]
            x+=10; y+=5
            pygame.draw.rect(surface, Color.primary, (x,y,w,h), 0, 2)
            
            x+=5; y+=5
            surface.blit(Method.stringShow("Position:",i[0][0],i[0][1],i[0][2]), (x,y))
            x+=220
            surface.blit(Method.stringShow("Accelartaion:"), (x,y))
            x-=220; y+=20
            surface.blit(Method.stringShow("Velocity:",i[1][0],i[1][1],i[1][2]), (x,y))
            x+=220
            surface.blit(Method.stringShow("Force:"), (x,y))
            Surfaces.object_panel[1] += 60
        Surfaces.object_panel = [10, 60, 380, 50]
        