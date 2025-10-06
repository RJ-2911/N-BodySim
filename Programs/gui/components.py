import pygame as pg
from pygame.locals import *

pg.init()

# Color definitions for GUI components
class Color:
    white = (255, 255, 255)
    text = (255, 255, 255)
    primary = (0, 0, 0)
    primary_v = (34, 34, 34)
    primary_vl = (44, 44, 44)
    secondary = (29, 205, 159)
    secondary_v = (22, 153, 118)


# String and font definitions for GUI text
class String:
    font_size = 25 
    
    font_style = pg.font.SysFont('Helvetica', font_size)
    small_font_style = pg.font.SysFont('Helvetica', font_size-10)

    info = font_style.render("Information Panel", True, Color.text)
    add = font_style.render("Add", True, Color.text, Color.primary_v)
    add_l = font_style.render("Add", True, Color.text, Color.primary_vl)
    remove = small_font_style.render("Remove", True, Color.text, Color.primary_v)
    change = small_font_style.render("Change", True, Color.text, Color.primary_v)


# Image assets for GUI buttons and controls
class Image:
    play = pg.image.load("resources/play.png")
    pause = pg.image.load("resources/pause.png")
    fast = pg.image.load("resources/fast.png")
    reset = pg.image.load("resources/reset.png")

    # Lighter versions for hover effects
    play_l = pg.image.load("resources/playL.png")
    pause_l = pg.image.load("resources/pauseL.png")
    fast_l = pg.image.load("resources/fastL.png")
    reset_l = pg.image.load("resources/resetL.png")