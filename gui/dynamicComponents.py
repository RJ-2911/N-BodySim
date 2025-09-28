import pygame
pygame.init()

# control booleans
class Boolean:
    is_running = True
    is_fullscreen = False
    is_playing = False
    is_add_context = False
    is_remove_change_context = False
    is_add_form = False
    is_change_form = False

# coordinates and sizes for surfaces
class CAS:
    # surfaces
    main_surface = [0, 0, 900, 700]
    info_control_surface = [main_surface[2], 0, 300, 700]
    info_surface = [info_control_surface[0], 0, 300, 600]
    control_surface = [info_control_surface[0], 600, 300, 100]

    # buttons positions
    minus5x = [control_surface[0]+27, control_surface[1]+18]
    play_pause = [control_surface[0]+118, control_surface[1]+18]
    plus5x = [control_surface[0]+209, control_surface[1]+18]

    # context menu
    add_context = [5000,5000,100,30]

# coordinates and sizes for handling event
class Hitbox:
    main_surface = CAS.main_surface
    minus5x = [CAS.control_surface[0]+27, CAS.control_surface[1]+18, 64, 64]
    play_pause = [CAS.control_surface[0]+118, CAS.control_surface[1]+18, 64, 64]
    plus5x = [CAS.control_surface[0]+209, CAS.control_surface[1]+18, 64, 64]

    # dynamic according to user input
    add_context = CAS.add_context
