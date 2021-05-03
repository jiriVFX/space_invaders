import pygame
from constants import *


class Alien(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, alien_paths, alien_color=WHITE):
        super().__init__()
        try:
            self.alien_paths = alien_paths
            self.surface = pygame.image.load(alien_paths[0]).convert_alpha()
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
        # animation iterator
        self.anim_iterator = 0

    def animate(self):
        if self.anim_iterator == 0:
            self.anim_iterator = 1
        else:
            self.anim_iterator = 0
        # change image path to create animation effect
        self.surface = pygame.image.load(self.alien_paths[self.anim_iterator]).convert_alpha()

    def move(self):
        increase_speed = False
        # animate
        self.animate()
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
