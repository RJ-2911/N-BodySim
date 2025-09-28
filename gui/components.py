import pygame

pygame.init()

# initializing different static assets
class Color:
    white = (255,255,255)
    text = (255,255,255)
    primary = (0,0,0)
    primaryV = (34,34,34)
    secondary = (29, 205, 159)
    secondaryV = (22, 153, 118)

class String:
    font_size = 25 
    
    font_style = pygame.font.SysFont('Helvetica', font_size)
    small_font_style = pygame.font.SysFont('Helvetica', font_size-10)

    info = font_style.render("Information Panel", True, Color.text)
    add = small_font_style.render("Add", True, Color.text, Color.primaryV )
    remove = small_font_style.render("Remove", True, Color.text, Color.primaryV)
    change = small_font_style.render("Change", True, Color.text, Color.primaryV)

class Image:
    play = pygame.image.load("resources/play.png")
    pause = pygame.image.load("resources/pause.png")
    plus5x = pygame.image.load("resources/+5x.png")
    minus5x = pygame.image.load("resources/-5x.png")

    # for lighter version when hovered
    playL = pygame.image.load("resources/playL.png")
    pauseL = pygame.image.load("resources/pauseL.png")
    plus5xL = pygame.image.load("resources/+5xL.png")
    minus5xL = pygame.image.load("resources/-5xL.png")