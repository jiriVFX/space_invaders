import pygame
from constants import *
import time


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, spaceship_path, spaceship_width=160, spaceship_height=15, spaceship_color=RED):
        super().__init__()
        try:
            self.surface = pygame.image.load(spaceship_path).convert_alpha()
            self.surface.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        except FileNotFoundError:
            self.width = spaceship_width
            self.height = spaceship_height
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill(spaceship_color)

        # Top left corner position coordinates
        self.corner = self.surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40))
        self.speed = 7
        self.direction = 0

        # Time of the last shot
        self.last_shot = 0

    def control(self, pressed_keys):
        """Controls spaceship movement and shooting.
        :type pressed_keys: pygame.key.get_pressed()
        :rtype: bool"""
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

        if shoot:
            print(shoot)
        return shoot
