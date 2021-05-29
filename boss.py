import pygame
from constants import *
import random


class Boss(pygame.sprite.Sprite):
    def __init__(self, position_y=ALIEN_BOSS_Y_POS, alien_color=RED):
        super().__init__()
        try:
            self.surface = pygame.image.load(POINTS_100).convert_alpha()
            self.surface.set_colorkey(BLACK, pygame.RLEACCEL)
        except FileNotFoundError:
            self.width = 40
            self.height = 28
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill(alien_color)

        # Top left corner position coordinates
        random_num = random.randint(0, 1)
        self.start_x = (- ALIEN_BOSS_WIDTH // 2, SCREEN_WIDTH + ALIEN_BOSS_WIDTH // 2)
        self.corner = self.surface.get_rect(center=(self.start_x[random_num], position_y))
        # Movements counter
        self.movements = 0
        # Alien movement speed
        self.alien_movement = BOSS_MOVEMENT
        # Direction
        directions = (1, -1)
        self.direction = directions[random_num]
        self.step_down_amount = 0
        # animation iterator
        self.anim_iterator = 0
        # destruction start time
        self.destruct_start_time = None
        # points received for alien destruction
        self.points = ALIENS_BOSS_POINTS

    def move(self):
        # check whether alien is to be destroyed
        if not self.update_destroyed():
            # move
            self.corner.move_ip(self.direction * self.alien_movement, self.step_down_amount)

    def update_destroyed(self):
        # check whether alien is to be destroyed
        if self.destruct_start_time and (pygame.time.get_ticks() - self.destruct_start_time >= DESTRUCTION_TIME):
            self.destroy()
            return True
        return False

    def init_destruction(self):
        # show alien explosion
        self.surface = pygame.image.load(ALIEN_EXPLOSION).convert_alpha()
        # get current time in milliseconds
        self.destruct_start_time = pygame.time.get_ticks()

    def destroy(self):
        # reset destruction start time
        self.destruct_start_time = None
        # destroy alien
        self.kill()

    def out_of_screen(self):
        # If alien gets out of screen (reaches the bottom green HUD line)
        if self.corner.right <= 0 or self.corner.left >= SCREEN_WIDTH:
            self.kill()
