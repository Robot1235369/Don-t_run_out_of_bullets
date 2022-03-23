import pygame
from vars import *
pygame.init()

def fullscreen():
    display.fill(BLACK)
    pygame.display.update()

def update():
    display.fill(BLACK)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.events.get():
            if event == pygame.QUIT():
                running = False
        if display.get_size() == (500 ,500):
            fullscreen()
        else:
            update()
    pygame.quit()

if __name__ == "__main__":
    main()
