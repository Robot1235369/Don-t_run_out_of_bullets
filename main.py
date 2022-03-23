import pygame
from vars import *
pygame.init()

def fulscreen():
    display.fill(BLACK)
    pygame.display.update()

def update():
    display.fill(BLACK)
    pygame.display.update()

def main():
    clock = pygame.CLOCK()
    while running:
        clock.tick(FPS)
        for event in pygame.events.get():
            if event == pygame.QUIT():
                running = False
        if display.get_size() == (500 ,500):
            fulscreen()
        else:
            update()
    pygame.quit()

if __name__ == "__main__":
    main()

# hello, I just was bored, so I wrote the starting code for the game
# this will just create a black window that is resizable, and that will close
# P.S. the vars.py file is for creating variables, so that the program doesn't get messy
