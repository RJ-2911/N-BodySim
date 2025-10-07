import pygame as pg

class Events:
    def __init__(self, guiWin):
        self.guiWin = guiWin
        self.mouse_pos = [0, 0]
        self.key_press = ''

    def button_interaction(self, *args):
        mouse_pos = self.mouse_pos
        click_list = [
            self.guiWin.play_pause,
            self.guiWin.reset,
            self.guiWin.fast,   
            self.guiWin.add
        ]

        for obj in click_list:
            cas = obj.cas
            if cas[0] <= mouse_pos[0] <= cas[0] + cas[2] and cas[1] <= mouse_pos[1] <= cas[1] + cas[3]:
                obj.is_hover = True
                if len(args) == 1:
                    obj.function()
            else:
                obj.is_hover = False

        click_list2 = [self.guiWin.hide, self.guiWin.add]
        for obj in click_list2:
            if obj.is_visible:
                cas = obj.cas
                if cas[0] <= mouse_pos[0] <= cas[0] + cas[2] and cas[1] <= mouse_pos[1] <= cas[1] + cas[3]:
                    obj.is_hover = True
                    if len(args) == 1:
                        obj.function()
                else:
                    obj.is_hover = False
                    if len(args) == 1 and obj != self.guiWin.add:
                        obj.is_visible = False

class EventHandler:
    def __init__(self, gui_window):
        self.gui_window = gui_window
        self.events = Events(self.gui_window)  # Initialize Events

    def handle_event(self, event):
        """
        Handles GUI events, including mouse movements, clicks, and window closure.
        """
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            self.gui_window.surfaces.is_running = False
            self.gui_window.running = False

        self.events.mouse_pos = pg.mouse.get_pos()
        self.events.button_interaction()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                self.events.button_interaction(1)