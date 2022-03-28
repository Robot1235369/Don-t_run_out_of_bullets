import pygame
from vars import *

class player:
    def __init__(self):
        self.x = display.get_size()[0] // 2
        self.y = display.get_size()[1] // 2