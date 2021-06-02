import pygame
from constants import *


class Shot(pygame.sprite.Sprite):
    # Initialize the sound module
    pygame.mixer.init()
    shoot_sound = pygame.mixer.Sound(SHOOT_SOUND)

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
        # how deep in the wall the shot gets before its destruction
        self.penetration_counter = 0
        # play the shoot sound
        self.player_shoot_sound()

    def move(self):
        self.corner.move_ip(self.direction_x * self.speed, self.direction_y * self.speed)

    def player_shoot_sound(self):
        self.shoot_sound.play()

    def player_shoot_sound_stop(self):
        self.shoot_sound.stop()

    def out_of_screen(self):
        # If shot gets out of screen area
        if self.corner.top <= SHOT_EXPLOSION_WIDTH // 2:
            # destroy shot only if it has not been hit already
            if self.destruct_start_time is None:
                # stop playing the shoot sound
                self.player_shoot_sound_stop()
                # initialize destruction
                self.init_destruction(explosion_sprite=PLAYER_SHOT_EXPLOSION_RED)

    def init_destruction(self, explosion_sprite=PLAYER_SHOT_EXPLOSION):
        # center the player shot explosion sprite
        self.corner = self.surface.get_rect(center=(self.corner[0] - SHOT_EXPLOSION_WIDTH // 2, self.corner[1]))
        # show player shot explosion
        self.surface = pygame.image.load(explosion_sprite).convert_alpha()
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
                        # stop playing the shoot sound
                        self.player_shoot_sound_stop()
                        # initialize alien destruction
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
                    # destroy shot only if it has not been hit already
                    # and only if it destroyed ALIEN_SHOT_PENETRATION amount of wall pieces
                    if self.destruct_start_time is None and self.penetration_counter == PLAYER_SHOT_PENETRATION:
                        # stop playing the shoot sound (has to be first)
                        self.player_shoot_sound_stop()
                        # destroy wall
                        wall_piece.destroy(wall_group)
                        # initiate shot destruction
                        self.init_destruction(explosion_sprite=ALIEN_SHOT_EXPLOSION_GREEN)
                        # reset penetration counter
                        self.penetration_counter = 0
                    else:
                        wall_piece.kill()
                        self.penetration_counter += 1

    def alien_shot_collision(self, alien_shots):
        for alien_shot in alien_shots:
            if self.corner.colliderect(alien_shot.corner):
                # destroy alien shot
                alien_shot.kill()
                # stop playing the shoot sound (has to be first)
                self.player_shoot_sound_stop()
                # destroy shot only if it has not been hit already
                if self.destruct_start_time is None:
                    self.init_destruction()

    def boss_collision(self, boss_group, scoreboard):
        for boss in boss_group:
            if boss is not None:
                if self.corner.colliderect(boss.corner):
                    # destroy boss if it has not been hit already
                    if boss.destruct_start_time is None:
                        # stop playing the shoot sound (has to be first)
                        self.player_shoot_sound_stop()
                        # initialize boss destruction
                        boss.init_destruction()
                        # Increase score
                        scoreboard.increase(boss)
                        # destroy shot
                        self.kill()

    def collision_detect(self, fleet_group, wall_group_list, alien_shots, boss_group, scoreboard):
        hit = False
        # Alien fleet collision detection
        hit = self.fleet_collision(fleet_group, scoreboard)
        # Wall collision detection
        self.wall_collision(wall_group_list)
        # Alien shots collision detection
        self.alien_shot_collision(alien_shots)
        # Boss shots collision detection
        self.boss_collision(boss_group, scoreboard)
        # Detect if shot is out of screen
        self.out_of_screen()

        return hit
