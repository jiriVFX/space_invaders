import time

import pygame
from constants import *


class Shot(pygame.sprite.Sprite):
    # Initialize the sound module
    pygame.mixer.init()
    col_sound = pygame.mixer.Sound(HIT_SOUND_1)
    col_sound_2 = pygame.mixer.Sound(HIT_SOUND_2)

    def __init__(self, position, shot_width=3, shot_height=20, shot_color=WHITE):
        super().__init__()
        self.surface = pygame.Surface((shot_width, shot_height))
        self.surface.fill(shot_color)
        # Top left corner position coordinates
        self.corner = self.surface.get_rect(center=(position[0] + SPACESHIP_WIDTH / 2, position[1]))
        self.direction_x = 0
        self.direction_y = -1
        self.speed = SHOT_SPEED
        # destruction start time
        self.destruct_start_time = None

    def move(self):
        self.corner.move_ip(self.direction_x * self.speed, self.direction_y * self.speed)

    def hit_sound(self):
        self.col_sound.play()

    def hit_sound_2(self):
        self.col_sound_2.play()

    def out_of_screen(self):
        # If shot gets out of screen area
        if self.corner.top <= 0:
            # destroy shot only if it has not been hit already
            if self.destruct_start_time is None:
                self.init_destruction()

    def init_destruction(self):
        # show player shot explosion
        self.surface = pygame.image.load(PLAYER_SHOT_EXPLOSION).convert_alpha()
        # get current time in milliseconds
        self.destruct_start_time = pygame.time.get_ticks()

    def destroy(self):
        # reset destruction start time
        self.destruct_start_time = None
        # destroy shot
        self.kill()

    def update_destroyed(self):
        # check whether player shot is to be destroyed
        if self.destruct_start_time and (pygame.time.get_ticks() - self.destruct_start_time >= DESTRUCTION_TIME):
            self.destroy()
            return True
        return False

    def fleet_collision(self, fleet_group, scoreboard):
        for alien in fleet_group:
            if alien is not None:
                if self.corner.colliderect(alien.corner):
                    # destroy alien if it has not been hit already
                    if alien.destruct_start_time is None:
                        alien.init_destruction(fleet_group)
                        # Increase score
                        scoreboard.increase(alien)
                        # destroy shot
                        self.kill()
                        # # BREAK is necessary to stop two aliens being destroyed at one impact
                        # break
                        return True
        return False

    def wall_collision(self, wall_group_list):
        for wall_group in wall_group_list:
            for wall_piece in wall_group:
                if self.corner.colliderect(wall_piece.corner):
                    # destroy the wall_piece
                    wall_piece.kill()
                    # destroy shot only if it has not been hit already
                    if self.destruct_start_time is None:
                        self.init_destruction()

    def alien_shot_collision(self, alien_shots):
        for alien_shot in alien_shots:
            if self.corner.colliderect(alien_shot.corner):
                # destroy alien shot
                alien_shot.kill()
                # destroy shot only if it has not been hit already
                if self.destruct_start_time is None:
                    self.init_destruction()

    def collision_detect(self, fleet_group, wall_group_list, alien_shots, scoreboard):
        hit = False
        # Alien fleet collision detection
        hit = self.fleet_collision(fleet_group, scoreboard)
        # Wall collision detection
        self.wall_collision(wall_group_list)
        # Alien shots collision detection
        self.alien_shot_collision(alien_shots)
        # Detect if shot is out of screen
        self.out_of_screen()

        return hit
