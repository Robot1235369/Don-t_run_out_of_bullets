import pygame
import threading
import sys
from vars import *
from main import load

def exit():
    global running_menu
    global left
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running_menu = False
            left = True

def update():
    pygame.display.update()
    done = True

def menu():
    global loading
    global done
    clock = pygame.time.Clock()

    while running_menu:
        clock.tick(FPS)
        exit()

        if not loading:
            for event in pygame.event.get():
                pass
        else:
            threading.Thread(target=load).start()
            loading = False
    
    if left:
        sys.exit()