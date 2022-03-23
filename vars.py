import pygame

WIDTH, HEIGHT = 500, 500
TITLE = "Don't Run Out of Bullets"
display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(TITLE)

FPS = 60
running = True

# colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)