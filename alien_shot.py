import pygame
from constants import *
import random


class AlienShot(pygame.sprite.Sprite):
    # Initialize the sound module
    pygame.mixer.init()
    player_explosion_sound = pygame.mixer.Sound(PLAYER_EXPLOSION_SOUND)

    def __init__(self, shot_path, position, shot_size=20, shot_color=WHITE):
        """
        :param shot_path: string
        :param position: pygame.Rect
        :param shot_size: int
        :param shot_color: (int, int, int)
        """
        super().__init__()
        try:
            # choose one of two types of alien shots
            paths = random.choice((ALIEN_SHOT_PATHS, ALIEN_SHOT_2_PATHS, ALIEN_SHOT_3_PATHS))
            self.sprites = []
            # load sprites for animation
            for path in paths:
                self.sprites.append(pygame.image.load(path).convert_alpha())

            self.current = 0
            self.surface = self.sprites[self.current]
            self.surface.set_colorkey(BLACK, pygame.RLEACCEL)
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
        # destruction start time
        self.destruct_start_time = None
        # how deep in the wall the shot gets before its destruction
        self.penetration_counter = 0

    def move(self):
        """Moves alien."""
        self.update()
        self.corner.move_ip(self.direction_x * self.speed, self.direction_y * self.speed)

    def update(self):
        """Animates alien shot."""
        # update only every 6 calls
        if self.update_count % ALIEN_SHOT_UPDATE_SPEED == 0:
            if self.current < len(self.sprites) - 1:
                self.current += 1
            else:
                self.current = 0
            # change the sprite
            self.surface = self.sprites[self.current]
            self.surface.set_colorkey(BLACK, pygame.RLEACCEL)
            # reset update counter
            self.update_count = 0
        self.update_count += 1

    def player_hit_sound(self):
        """Plays player hit sound."""
        self.player_explosion_sound.play()

    def out_of_screen(self):
        """Initiates shot destruction if it has left the screen."""
        # If shot gets out of screen area
        if SCREEN_HEIGHT + ALIEN_SHOT_EXPLOSION_HEIGHT // 2 <= self.corner.bottom:
            if self.destruct_start_time is None:
                # initiate shot destruction
                self.init_destruction(explosion_sprite=ALIEN_SHOT_EXPLOSION_GREEN)

    def init_destruction(self, explosion_sprite=ALIEN_SHOT_EXPLOSION):
        """
        Initiates shot destruction and changes shot sprite for shot explosion sprite.
        :param explosion_sprite: str
        :return:
        """
        # show alien shot explosion
        self.surface = pygame.image.load(explosion_sprite).convert_alpha()
        # get current time in milliseconds
        self.destruct_start_time = pygame.time.get_ticks()

    def destroy(self):
        """Destroys the alien shot."""
        # reset destruction start time
        self.destruct_start_time = None
        # destroy shot
        self.kill()

    def update_destroyed(self):
        """
        Checks whether DESTRUCTION_TIME has elapsed. If it has, calls self.destroy method on the alien shot.
        :return: bool
        """
        # check whether alien shot is to be destroyed
        if self.destruct_start_time and (pygame.time.get_ticks() - self.destruct_start_time >= DESTRUCTION_TIME):
            self.destroy()
            return True
        return False

    def wall_collision(self, wall_group_list):
        """
        Detects alien shot collision with walls in wall_group_list.
        Initiates shot destruction after ALIEN_SHOT_PENETRATION of wall objects is killed.
        :param wall_group_list: list[list[Wall]]
        :return:
        """
        for wall_group in wall_group_list:
            for wall_piece in wall_group:
                if self.corner.colliderect(wall_piece.corner):
                    # destroy shot only if it has not been hit already
                    # and only if it destroyed ALIEN_SHOT_PENETRATION amount of wall pieces
                    if self.destruct_start_time is None and self.penetration_counter == ALIEN_SHOT_PENETRATION:
                        # destroy wall
                        wall_piece.destroy(wall_group)
                        # initiate shot destruction
                        self.init_destruction(explosion_sprite=ALIEN_SHOT_EXPLOSION_GREEN)
                        # reset penetration counter
                        self.penetration_counter = 0
                    else:
                        wall_piece.kill()
                        self.penetration_counter += 1

    def spaceship_collision(self, spaceship, scoreboard):
        """
        Detects collision with spaceship. Initiates alien shot destruction if spaceship is hit.
        :param spaceship: Spaceship
        :param scoreboard: Scoreboard
        :return: bool
        """
        if self.corner.colliderect(spaceship.corner) and spaceship.destruct_start_time is None:
            if self.destruct_start_time is None:
                # initiate shot destruction
                self.init_destruction()
                # play explosion sound
                self.player_hit_sound()
                # Remove life from scoreboard
                scoreboard.remove_life()
                # Remove life from spaceship
                spaceship.remove_life()
                # return True as spaceship was hit
                return True
        # return False if spaceship was not hit
        return False

    def line_collision(self, green_line):
        """
        Detects alien shot collision with the green HUD line on the bottom of the screen.
        :param green_line: list[dict[pygame.Surface, pygame.Rect]]
        :return:
        """
        for i in range(len(green_line)):
            if green_line[i] is not None:
                if self.corner.colliderect(green_line[i]["corner"]) and self.destruct_start_time is None:
                    # initiate shot destruction
                    self.init_destruction(explosion_sprite=ALIEN_SHOT_EXPLOSION_GREEN)
                    # destroy pixel and the one next to it
                    green_line[i] = None

    def collision_detect(self, wall_group_list, green_line, spaceship, scoreboard):
        """Handles collision detection methods. Returns True when spaceship was hit, otherwise False.
        :type wall_group_list: pygame.sprite.Group
        :type green_line: list[dict]
        :type spaceship: pygame.sprite.Sprite
        :type scoreboard: scoreboard.Scoreboard
        :rtype: bool
        """
        # Shield obstacles fleet collision detection
        self.wall_collision(wall_group_list)
        # Detect if shot is out of screen
        self.out_of_screen()
        # Detect collision with bottom HUD line
        self.line_collision(green_line)
        # Spaceship collision detection
        if spaceship is not None and self.spaceship_collision(spaceship, scoreboard):
            return True

        return False
