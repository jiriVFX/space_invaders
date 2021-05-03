import pygame
from constants import *
from spaceship import SpaceShip
from alien import Alien
from shot import Shot
from alien_shot import AlienShot
from scoreboard import Scoreboard
import time
from random import choice

# Initialize pygame
pygame.init()

# ----------------------------------------------------------------------------------------------------------------------

# Create screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Breakout game")
# Set background colour
screen.fill(WHITE)

# Scoreboard
scoreboard = Scoreboard()

# Font
pygame.font.init()
font = pygame.font.SysFont("Consolas", 60, bold=True)
text_won = font.render("You won!", True, WHITE)
text_won_corner = text_won.get_rect(center=((SCREEN_WIDTH) / 2, SCREEN_HEIGHT / 2 - 40))

# Sounds
collision_sound = pygame.mixer.Sound("static/sound/hit1.mp3")
winning_sound = pygame.mixer.Sound("static/sound/chime.mp3")

# Gaming area surface
game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
game_surface.fill(DARK_GREY)
# rect = game_space.get_rect()

# Create spaceship
spaceship = SpaceShip(SPACESHIP_PATH)

# Create spaceship and obstacle group
obstacle_group = pygame.sprite.Group()
obstacle_group.add(spaceship)

# Create shot group
shots = pygame.sprite.Group()

# Create alien shot group
alien_shots = pygame.sprite.Group()

# Create alien fleet
fleet = pygame.sprite.Group()
groups_list = []

# Create fleet of aliens
for i in range(ROWS):
    # groups_list.append(pygame.sprite.Group())
    groups_list.append([])
    colour = None
    if i == 0:
        alien_path = POINTS_30_1
    elif i == 1:
        alien_path = POINTS_30_1
    elif i == 2:
        alien_path = POINTS_20_1
    elif i == 3:
        alien_path = POINTS_20_1
    elif i == 4:
        alien_path = POINTS_10_1
    else:
        alien_path = POINTS_10_1
    # Create one row of aliens
    for j in range(COLUMNS):
        # Each brick's starting position is
        # x = (j * width of the alien + half the size of the alien + offset from the left)
        # y = i * (height of the alien + space between lines) + offset from the top
        # print(colour)
        # new_alien = Alien((j * SCREEN_WIDTH // 13 + SCREEN_WIDTH // 9), i * (SCREEN_HEIGHT // 15) + 160, alien_path)
        new_alien = Alien((j * 1.5 * ALIEN_WIDTH + SCREEN_WIDTH // 9), i * (2 * ALIEN_HEIGHT) + 160, alien_path)
        # add all aliens to fleet group
        fleet.add(new_alien)
        # add aliens to the current row group
        #groups_list[i].add(new_alien)
        groups_list[i].append(new_alien)
# ----------------------------------------------------------------------------------------------------------------------

# Game loop
clock = pygame.time.Clock()
game_on = True
movement_time = time.time()
shoot_time = time.time()
movement_delay = MOVEMENT_DELAY
i = 0
while game_on:
    # Quit the game when X is clicked or Esc pressed to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False

    # Player Shot collision detection and spaceship movement -----------------------------------------------------------

    # Collision detection and movement of existing player shots
    for shot in shots:
        shot.move()
        shot.collision_detect(fleet, scoreboard)

    # Pressed down keys boolean list - 0 for keys not pressed and 1 for keys pressed
    pressed_keys = pygame.key.get_pressed()

    # Control spaceship - create shots
    if spaceship.control(pressed_keys):
        shots.add(Shot(ALIEN_SHOT_PATH, spaceship.corner))

    # Aliens movement and shooting -------------------------------------------------------------------------------------
    # TODO - alien shots have to destroy player
    # TODO - only the alien with no other aliens in front of him can shoot

    # Make random alien shoot
    if time.time() - shoot_time > ALIEN_SHOOT_DELAY:
        shoot_time = time.time()
        random_alien = choice(choice(groups_list))
        alien_shots.add(AlienShot(ALIEN_SHOT_PATH, random_alien.corner))

    # Collision detection and movement of existing alien shots
    for shot in alien_shots:
        shot.move()
        # TODO - if spaceship was hit, it has to be removed here in main
        shot.collision_detect(obstacle_group, spaceship, scoreboard)

    # move aliens in intervals
    if time.time() - movement_time > movement_delay:
        movement_time = time.time()

        # move only one row at each time
        # move starting from the last row
        for alien in groups_list[len(groups_list) - 1 - i]:
            increase_speed = alien.move()

        # increase speed
        if increase_speed:
            movement_delay /= 1.025

        # increment row
        if i < len(groups_list) - 1:
            i += 1
        else:
            i = 0

    # Rendering --------------------------------------------------------------------------------------------------------

    # Place the gaming area on the screen
    screen.blit(game_surface, (0, 0))

    # Render all aliens in the fleet
    for alien in fleet:
        # print(alien.corner)
        screen.blit(alien.surface, alien.corner)

    # Place the ship on the screen
    # Places ship in the middle + paddle corner(rect) position (changes when paddle moves)
    screen.blit(spaceship.surface, spaceship.corner)

    # Place player shots on the screen
    for shot in shots:
        screen.blit(shot.surface, shot.corner)

    # Place alien shots on the screen
    for shot in alien_shots:
        screen.blit(shot.surface, shot.corner)

    # Place scoreboard on the screen
    screen.blit(scoreboard.score_text, scoreboard.corner)

    # Check whether there are any bricks left
    # Render End Game text - has to be the last to render, otherwise covered by other surfaces
    if not fleet:
        # Play winning sound
        winning_sound.play()
        screen.blit(text_won, text_won_corner)
        pygame.display.update()
        # Wait for x miliseconds until closing the game
        pygame.time.delay(3000)
        game_on = False

    # Refresh display
    pygame.display.flip()

    # Set refresh rate to 60 times per second (60Hz/FPS)
    clock.tick(60)
    # print(clock.get_fps())

# Quit all the sounds and the game
pygame.mixer.quit()
pygame.quit()
