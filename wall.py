import pygame
from constants import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, wall_width=WALL_PIX_SIZE, wall_height=WALL_PIX_SIZE, wall_color=GREEN):
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(wall_color)

        # Top left corner position coordinates - position = (center=(X, Y))
        self.corner = self.surface.get_rect(center=(position_x, position_y))
