import pygame
from constants import *


class AlienShot(pygame.sprite.Sprite):
    # Initialize the sound module
    pygame.mixer.init()
    col_sound = pygame.mixer.Sound(HIT_SOUND_1)
    col_sound_2 = pygame.mixer.Sound(HIT_SOUND_2)

    def __init__(self, shot_path, position, shot_size=20, shot_color=WHITE):
        super().__init__()
        try:
            self.sprites = []
            # load sprites for animation
            for path in ALIEN_SHOT_PATHS:
                self.sprites.append(pygame.image.load(path).convert_alpha())

            self.current = 0
            self.surface = self.sprites[self.current]
            self.surface.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        except (FileNotFoundError, TypeError) as exception:
            self.shot_radius = shot_size
            self.surface = pygame.Surface((self.shot_radius, self.shot_radius))
            self.surface.fill(shot_color)
        # Top left corner position coordinates
        self.corner = self.surface.get_rect(center=(position[0] + SPACESHIP_WIDTH / 2, position[1]))
        self.direction_x = 0
        self.direction_y = 1
        self.speed = ALIEN_SHOT_SPEED
        self.update_count = 0

    def move(self):
        self.update()
        self.corner.move_ip(self.direction_x * self.speed, self.direction_y * self.speed)

    def update(self):
        # update only every 6 calls
        if self.update_count % ALIEN_SHOT_UPDATE_SPEED == 0:
            if self.current < len(self.sprites) - 1:
                self.current += 1
            else:
                self.current = 0
            # change the sprite
            self.surface = self.sprites[self.current]
            # reset update counter
            self.update_count = 0
        self.update_count += 1

    def hit_sound(self):
        self.col_sound.play()

    def hit_sound_2(self):
        self.col_sound_2.play()

    def out_of_screen(self):
        # If shot gets out of screen area
        if SCREEN_HEIGHT - 100 > self.corner.bottom < 0:
            self.kill()

    def wall_collision(self, wall_group):
        for target in wall_group:
            if self.corner.colliderect(target.corner):
                # destroy alien
                target.kill()
                # destroy shot
                self.kill()

    def spaceship_collision(self, spaceship, scoreboard):
        if self.corner.colliderect(spaceship.corner):
            # Remove life from scoreboard
            scoreboard.remove_life()
            # Remove life from spaceship
            spaceship.remove_life()
            # destroy shot
            self.kill()
            # return True as spaceship was hit
            return True
        # return False if spaceship was not hit
        return False

    def collision_detect(self, wall_group, spaceship, scoreboard):
        """Handles collision detection methods. Returns True when spaceship was hit, otherwise False.
        :type wall_group: pygame.sprite.Group
        :type spaceship: pygame.sprite.Sprite
        :type scoreboard: scoreboard.Scoreboard
        :rtype: bool"""
        # Shield obstacles fleet collision detection
        self.wall_collision(wall_group)
        # Detect if shot is out of screen
        self.out_of_screen()
        # Spaceship collision detection
        if spaceship is not None and self.spaceship_collision(spaceship, scoreboard):
            return True

        return False

