import pygame
from vars import *
pygame.init()

font = pygame.font.Font('arial.ttf', 32)
text = font.render('Please Fullscreen this Window to Play', True, green, blue)
textRect = text.get_rect()

def fullscreen():
    display.fill(BLACK)
    display_surface.blit(text, textRect)
    pygame.display.update()

def update():
    display.fill(BLACK)
    pygame.display.update()

def main():
    global running
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if display.get_size() == (500, 500):
            fullscreen()
        else:
            update()
    pygame.quit()

if __name__ == "__main__":
    main()