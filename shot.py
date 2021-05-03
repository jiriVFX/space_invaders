import pygame
from constants import *


class Shot(pygame.sprite.Sprite):
    # Initialize the sound module
    pygame.mixer.init()
    col_sound = pygame.mixer.Sound(HIT_SOUND_1)
    col_sound_2 = pygame.mixer.Sound(HIT_SOUND_2)

    def __init__(self, shot_path, position, shot_size=20, shot_color=WHITE):
        super().__init__()
        try:
            self.surface = pygame.image.load(shot_path).convert_alpha()
            self.surface.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        except FileNotFoundError:
            self.ball_radius = shot_size
            self.surface = pygame.Surface((self.ball_radius, self.ball_radius))
            self.surface.fill(shot_color)
        # Top left corner position coordinates
        self.corner = self.surface.get_rect(center=(position[0] + SPACESHIP_WIDTH / 2, position[1]))
        # Make correct collision circle around the ball
        self.radius = self.corner.width / 2
        self.direction_x = 0
        self.direction_y = -1
        self.speed = SHOT_SPEED
        self.bounce_count = 0

    def move(self):
        self.corner.move_ip(self.direction_x * self.speed, self.direction_y * self.speed)

    def hit_sound(self):
        self.col_sound.play()

    def hit_sound_2(self):
        self.col_sound_2.play()

    def out_of_screen(self):
        # If shot gets out of screen area
        if SCREEN_HEIGHT - 100 > self.corner.bottom < 0:
            self.kill()

    def fleet_collision(self, fleet_group, scoreboard):
        # TODO - alien destruction animation
        for alien in fleet_group:
            if self.corner.colliderect(alien.corner):
                # The difference between y position of shot and alien is usually < 3 px
                # destroy alien
                alien.kill()
                # Increase score
                scoreboard.increase()
                # destroy shot
                self.kill()
                # BREAK is necessary to stop two bricks being destroyed at one impact
                # - otherwise ball continues in the original direction and destroys 3 bricks
                # - because y position reverses twice when hitting two bricks at the same time
                # - changes in y negate and ball continues in the original direction
                break

    def collision_detect(self, fleet_group, scoreboard):
        # Alien fleet collision detection
        self.fleet_collision(fleet_group, scoreboard)
        # Detect if shot is out of screen
        self.out_of_screen()

