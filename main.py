import pygame
import threading
from vars import *
from mainmenu import *
pygame.init()

def AddCharacter(X,Y):
    game_display.blit(character_1, (X,Y))

    y = (WIDTH * 0.95)
    x = (HEIGHT * 0.5)

def exit():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        game_display.blit(floor, (0,0))
        Loading_Ball(X,Y)


def load():
    modifier = 1
    while True:
        #display.fill(BLACK)
        if not done:
            display.blit(loading_ball, (loading_x, display.get_size()[1] // 2))
            loading_x += modifier
            if loading_x >= (display.get_size()[0] // 2) + 100:
                modifier *= -1
            pygame.display.update()
        else:
            break

def update():
    #display.fill(BLACK)
    pygame.display.update()
    done = True

def main():
    global running
    menu()
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)
        exit()

        if not loading:
            for event in pygame.event.get():
                pass

            update()
        else:
            threading.Thread(target=load).start()
            loading = False

if __name__ == "__main__":
    main()
    #this is a bit confusing could you posibly explain sometime
