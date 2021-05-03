import pygame
from constants import *


class Alien(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, alien_path, alien_color=WHITE):
        super().__init__()
        try:
            self.surface = pygame.image.load(alien_path).convert_alpha()
            self.surface.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        except FileNotFoundError:
            self.width = SCREEN_WIDTH // 11 - 5
            self.height = SCREEN_HEIGHT // 20
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill(alien_color)

        # Top left corner position coordinates
        self.corner = self.surface.get_rect(center=(position_x, position_y))
        # Movements counter
        self.movements = 0
        # Direction
        self.direction = 1
        self.step_down = 0

    def move(self):
        increase_speed = False
        # TODO - animate while moving
        # 4 movements to one side, then change sides
        if self.movements == MOVEMENTS_NUM:
            # Aliens have to move back to original 0 position, then 4 times more
            self.movements = - MOVEMENTS_NUM
            self.direction *= -1
            # each time aliens get to the edge, they have to step down one row
            self.step_down += ALIEN_HEIGHT
            # move
            self.corner.move_ip(self.direction * ALIEN_MOVEMENT, self.step_down)
            # increase speed
            increase_speed = True
        else:
            self.corner.move_ip(self.direction * ALIEN_MOVEMENT, self.step_down)

        self.step_down = 0
        self.movements += 1

        return increase_speed
    # def move_right(self):
    #     self.corner.move_ip((-1) * ALIEN_MOVEMENT, 0)
    #
    # def move_left(self):
    #     self.corner.move_ip(ALIEN_MOVEMENT, 0)
