import pygame
from constants import *


class Alien(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, row, column, alien_paths, points, alien_color=WHITE):
        super().__init__()
        try:
            self.alien_paths = alien_paths
            self.surface = pygame.image.load(alien_paths[0]).convert_alpha()
            self.surface.set_colorkey(BLACK, pygame.RLEACCEL)
        except FileNotFoundError:
            self.width = SCREEN_WIDTH // 11 - 5
            self.height = SCREEN_HEIGHT // 20
            self.surface = pygame.Surface((self.width, self.height))
            self.surface.fill(alien_color)

        # Top left corner position coordinates
        self.corner = self.surface.get_rect(center=(position_x, position_y))
        # coordinates in the fleet
        self.row = row
        self.column = column
        # Movements counter
        self.movements = 0
        # Number of movements
        self.movements_num = MOVEMENTS_NUM
        # Alien movement speed
        self.alien_movement = ALIEN_MOVEMENT
        # Direction
        self.direction = 1
        self.step_down_amount = 0
        # animation iterator
        self.anim_iterator = 0
        # destruction start time
        self.destruct_start_time = None
        # points received for alien destruction
        self.points = points
        # destruction fleet
        self.fleet_group = []
        # # next iteration movement increase
        # self.movements_num_increase = None

    def animate(self):
        if self.anim_iterator == 0:
            self.anim_iterator = 1
        else:
            self.anim_iterator = 0
        # change image path to create animation effect
        self.surface = pygame.image.load(self.alien_paths[self.anim_iterator]).convert_alpha()

    def calculate_speed(self):
        # movement speed
        self.alien_movement
        # Number of movements to each side
        self.movements_num

    # def increase_movements(self, increase_by):
    #     self.movements_num_increase = increase_by

    def move(self):
        # check whether alien is to be destroyed
        if not self.update_destroyed():
            # animate
            self.animate()
            # move
            self.corner.move_ip(self.direction * self.alien_movement, self.step_down_amount)

    def step_down(self):
        # check whether alien is to be destroyed
        if not self.update_destroyed():
            # increase step_down_amount coordinates
            self.step_down_amount += ALIEN_HEIGHT
            # step down
            self.corner.move_ip(self.direction * self.alien_movement, self.step_down_amount)
            self.step_down_amount = 0

    def update_destroyed(self):
        # check whether alien is to be destroyed
        if self.destruct_start_time and (pygame.time.get_ticks() - self.destruct_start_time >= DESTRUCTION_TIME):
            self.destroy()
            return True
        return False

    def init_destruction(self, fleet):
        # show alien explosion
        self.surface = pygame.image.load(ALIEN_EXPLOSION).convert_alpha()
        # get current time in milliseconds
        self.destruct_start_time = pygame.time.get_ticks()
        # remember the row
        self.fleet_group = fleet

    def destroy(self):
        # calculate position in the fleet
        position = self.row * COLUMNS + self.column
        # remove alien - replace with None
        self.fleet_group[position] = None
        # reset destruction start time
        self.destruct_start_time = None
        # destroy alien
        self.kill()

    def wall_collision(self, wall_group_list):
        for wall_group in wall_group_list:
            for wall_piece in wall_group:
                if self.corner.colliderect(wall_piece.corner):
                    # destroy wall_piece on collision with alien
                    wall_piece.kill()

    def out_of_screen(self):
        # If alien gets out of screen (reaches the bottom green HUD line)
        if self.corner.bottom >= SCREEN_HEIGHT - 70:
            return True
        return False

    def collision_detection(self, wall_group_list):
        self.wall_collision(wall_group_list)
