import pygame
from constants import *
import random


class Wall(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, wall_width=WALL_PIX_SIZE, wall_height=WALL_PIX_SIZE, wall_color=GREEN):
        """
        :param position_x: int
        :param position_y: int
        :param wall_width: int
        :param wall_height: int
        :param wall_color: (int, int, int)
        """
        super().__init__()
        self.width = wall_width
        self.height = wall_height
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(wall_color)

        # Top left corner position coordinates - position = (center=(X, Y))
        self.corner = self.surface.get_rect(center=(position_x, position_y))

    def destroy(self, wall_group):
        """
        Destroys the current wall piece (wall pixel) together with random pixels in its proximity.
        :param wall_group: pygame.sprite.Group()
        :return:
        """
        for wall_piece in wall_group:
            if abs(wall_piece.corner[0] - self.corner[0]) < 10 and abs(wall_piece.corner[1] - self.corner[1]) < 15:
                if random.randint(0, 1) == 1:
                    wall_piece.kill()
