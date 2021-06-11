import pygame
from constants import *
import random


class Boss(pygame.sprite.Sprite):
    # Initialize the sound module
    pygame.mixer.init()
    boss_explosion_sound = pygame.mixer.Sound(BOSS_EXPLOSION_SOUND)
    # boss_sound = pygame.mixer.Sound(BOSS_SOUND)
    pygame.mixer.music.load(BOSS_SOUND)

    def __init__(self, position_y=ALIEN_BOSS_Y_POS, alien_color=RED):
        """
        :param position_y: int
        :param alien_color: (int, int, int)
        """
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
        # play the boss sound
        pygame.mixer.music.play(loops=-1)

    def move(self):
        """Moves alien boss."""
        # check whether alien is to be destroyed
        if not self.update_destroyed():
            # move
            self.corner.move_ip(self.direction * self.alien_movement, self.step_down_amount)
            # play boss sound
            # self.boss_sound.play()

    def hit_sound(self):
        """Plays alien boss explosion sound."""
        self.boss_explosion_sound.play()

    def stop_sound(self):
        """Stop playing alien boss sound"""
        pygame.mixer.music.stop()

    def update_destroyed(self):
        """
        Checks whether BOSS_DESTRUCTION_TIME has elapsed. If it has, calls self.destroy() on alien boss.
        Changes explosion sprite when BOSS_DESTRUCTION_TIME // 3 time has elapsed.
        :return: bool
        """
        # check whether alien is to be destroyed
        if self.destruct_start_time and (pygame.time.get_ticks() - self.destruct_start_time >= BOSS_DESTRUCTION_TIME):
            self.destroy()
            return True
        elif self.destruct_start_time and (pygame.time.get_ticks() - self.destruct_start_time >= BOSS_DESTRUCTION_TIME // 3):
            # change the explosion sprite during destruction
            self.surface = pygame.image.load(ALIEN_BOSS_EXPLOSIONS[1]).convert_alpha()
            self.surface.set_colorkey(BLACK, pygame.RLEACCEL)

        return False

    def init_destruction(self):
        """
        Initializes alien boss destruction.
        Changes boss sprite for the first alien boss explosion sprite.
        """
        # stop the boss sound
        pygame.mixer.music.stop()
        # show alien explosion
        self.surface = pygame.image.load(ALIEN_BOSS_EXPLOSIONS[0]).convert_alpha()
        self.surface.set_colorkey(BLACK, pygame.RLEACCEL)
        # get current time in milliseconds
        self.destruct_start_time = pygame.time.get_ticks()
        # play explosion sound
        self.hit_sound()

    def destroy(self):
        """Destroys alien boss."""
        # reset destruction start time
        self.destruct_start_time = None
        # destroy alien
        self.kill()

    def out_of_screen(self):
        """Detects whether alien bos has left the screen area. If it has, kills the alien boss object."""
        # If alien gets out of screen (reaches the bottom green HUD line)
        if self.corner.right <= 0 or self.corner.left >= SCREEN_WIDTH:
            # stop the boss sound
            pygame.mixer.music.stop()
            self.kill()
