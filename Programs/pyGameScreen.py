# Prototype

import pygame

pygame.init()

# main window
window = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("N-Body Simulation")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

# booleans
running = True
isPlaying = False

# colors
white = (255,255,255)
black = (0,0,0)
grey = (125,125,125)

# coordinates and sizes
information_cas = [940, 10, 250, 600]
play_cas = [1033, 623]
plus5x_cas = [954, 623]
minus5x_cas = [1112, 623]

# coordinates and sizes but for handling events
play_pause_case = [1033, 613, 64, 64]

# initialization of images and assets
font = pygame.font.Font(None ,30)
t_info = font.render("Information Panel", True, (255,255,255))
play_image = pygame.image.load("assets/play.png")
pause_image = pygame.image.load("assets/pause.png")
plus5x_image = pygame.image.load("assets/+5x.png")
minus5x_image = pygame.image.load("assets/-5x.png")

# methods
def isClicked(lst:list):
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    if mouse_pos[0]>=lst[0] and mouse_pos[1]>=lst[1] and mouse_pos[0]<=lst[0]+lst[2] and mouse_pos[1]<=lst[1]+lst[3]:
        return True
    else:
        return False

# mainloop
while running:
    window.fill(black)
    
    # event handler
    for event in pygame.event.get():
        # handle window close event
        if event.type == pygame.QUIT:
            running = False

        # mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if isClicked(play_pause_case):
                if isPlaying:
                    isPlaying = False
                else:
                    isPlaying = True
    
    if isPlaying:
        # play-pause button
        window.blit(pause_image, play_cas)
        window.blit(plus5x_image, plus5x_cas)
        window.blit(minus5x_image, minus5x_cas)
        
    
    else:
        # play-pause button
        window.blit(play_image, play_cas)
    
    # information panel
    information_panel = pygame.draw.rect(window, grey, information_cas)
    window.blit(t_info, information_cas)

    # to apply and write changes to screen
    pygame.display.update()

pygame.quit()