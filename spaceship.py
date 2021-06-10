import pygame
from constants import *
import time


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, spaceship_path, spaceship_width=44, spaceship_height=32, spaceship_color=WHITE):
        """
        :param spaceship_path: str
        :param spaceship_width: int
        :param spaceship_height: int
        :param spaceship_color: (int, int, int)
        """
        super().__init__()
        try:
            self.surface = pygame.image.load(spaceship_path).convert_alpha()
            self.surface.set_colorkey(BLACK, pygame.RLEACCEL)
        except FileNotFoundError:
            self.width = spaceship_width
            self.height = spaceship_height
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill(spaceship_color)

        # Top left corner position coordinates - position = (center=(X, Y))
        self.corner = self.surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120))
        self.speed = SPACESHIP_MOVEMENT_SPEED
        self.direction = 0
        # Time of the last shot
        self.last_shot = 0
        # Lives
        self.lives = LIVES
        # destruction start time
        self.destruct_start_time = None
        # explosion sprite
        self.explosion = 1
        # last explosion sprite change time
        self.explosion_time = None

    def control(self, pressed_keys):
        """
        Controls spaceship movement and shooting.
        :type pressed_keys: pygame.key.ScancodeWrapper
        :rtype: bool
        """
        self.direction = 0
        shoot = False
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.corner.move_ip(-self.speed, 0)
            self.direction = - 1
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.corner.move_ip(self.speed, 0)
            self.direction = 1
        # Shoot
        if pressed_keys[pygame.K_SPACE] or pressed_keys[pygame.K_UP]:
            if time.time() - self.last_shot > SHOT_DELAY:
                self.last_shot = time.time()
                # Create a shot object
                shoot = True

        if self.corner.left < 0:
            self.corner.left = 0
        if self.corner.right > SCREEN_WIDTH:
            self.corner.right = SCREEN_WIDTH

        return shoot

    def update_destroyed(self):
        """
        Checks whether SPACESHIP_DESTRUCTION_TIME has elapsed.
        Removes spaceship explosion sprite SPACESHIP_DOWNTIME milliseconds before calling self.new_life().
        :return: bool
        """
        # check whether spaceship is to be destroyed
        if self.destruct_start_time and (
                pygame.time.get_ticks() - self.destruct_start_time >= SPACESHIP_DESTRUCTION_TIME):
            self.new_life()
            return True
        # remove surface just before bringing new spaceship to life
        elif self.destruct_start_time and (
                pygame.time.get_ticks() - self.destruct_start_time >= SPACESHIP_DESTRUCTION_TIME - SPACESHIP_DOWNTIME):
            self.surface = None
        elif pygame.time.get_ticks() - self.explosion_time >= SPACESHIP_EXPLOSION_TIME:
            # change explosion sprites to animate
            if self.explosion == 1:
                self.surface = pygame.image.load(SPACESHIP_EXPLOSION_2).convert_alpha()
                self.explosion = 2
                self.explosion_time = pygame.time.get_ticks()
            else:
                self.surface = pygame.image.load(SPACESHIP_EXPLOSION_1).convert_alpha()
                self.explosion = 1
                self.explosion_time = pygame.time.get_ticks()
        return False

    def new_life(self):
        """Resets self.explosion_time and self.destruct_start_time variables and displays spaceship sprite."""
        # display spaceship sprite
        self.surface = pygame.image.load(SPACESHIP_PATH).convert_alpha()
        self.explosion_time = None
        self.destruct_start_time = None

    def init_destruction(self):
        """Initializes spaceship destruction. Changes spaceship sprite for explosion sprite."""
        # set explosion and destruction times in milliseconds
        # explosion time is necessary for changing explosion sprites in update_destroyed
        self.explosion_time = pygame.time.get_ticks()
        self.destruct_start_time = pygame.time.get_ticks()
        # show spaceship explosion
        self.surface = pygame.image.load(SPACESHIP_EXPLOSION_1).convert_alpha()

    def remove_life(self):
        """Calls self.init_destruction() method and removes one life from self.lives."""
        self.init_destruction()
        self.lives -= 1
