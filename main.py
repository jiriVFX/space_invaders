import pygame
from constants import *
from spaceship import SpaceShip
from alien import Alien
from shot import Shot
from alien_shot import AlienShot
from scoreboard import Scoreboard
from wall import Wall
import time
from random import choice

# Initialize pygame
pygame.init()

# ----------------------------------------------------------------------------------------------------------------------

# Create screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Space Invaders")
# Set background colour
screen.fill(WHITE)

# Scoreboard
scoreboard = Scoreboard()

# Font
pygame.font.init()
font = pygame.font.SysFont("Consolas", 80, bold=True)
text_won = font.render("You won!", True, RED)
text_won_corner = text_won.get_rect(center=((SCREEN_WIDTH) / 2, SCREEN_HEIGHT / 2 - 40))
text_lost = font.render("You lost.", True, RED)
text_lost_corner = text_won.get_rect(center=((SCREEN_WIDTH) / 2, SCREEN_HEIGHT / 2 - 40))

# Sounds
collision_sound = pygame.mixer.Sound("static/sound/hit1.mp3")
winning_sound = pygame.mixer.Sound("static/sound/chime.mp3")

# Gaming area surface
game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
game_surface.fill(DARK_GREY)
# rect = game_space.get_rect()

# Create obstacle group
wall_group = pygame.sprite.Group()

# Create spaceship
spaceship = SpaceShip(SPACESHIP_PATH)

# Create walls
# for i in range(WALLS):
#     for j in range(WALL_HEIGHT):
#         for k in range(WALL_WIDTH):
#             wall_piece = Wall(((i + 1) * (SCREEN_WIDTH // 5.5)) + k * WALL_PIX_SIZE,
#                               j * WALL_PIX_SIZE + SCREEN_HEIGHT - 220)
#             wall_group.add(wall_piece)

# walls
for w in range(4):
    # columns
    for i in range(24):
        # rows
        if i < 5:
            for j in range(22):
                if (i == 0 and j < 5) or (i == 1 and j < 4) or (i == 2 and j < 3) or (i == 3 and j < 2) or (i == 4 and j < 1):
                    pass
                else:
                    wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group.add(wall_piece)
        elif i == 5:
            for j in range(20):
                wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                wall_group.add(wall_piece)
        elif i == 6:
            for j in range(19):
                wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                wall_group.add(wall_piece)
        elif i == 7:
            for j in range(18):
                wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                wall_group.add(wall_piece)
        elif i == 8:
            for j in range(17):
                wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                wall_group.add(wall_piece)
        elif 8 < i < 15:
            for j in range(16):
                wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                wall_group.add(wall_piece)
        elif i == 15:
            for j in range(17):
                wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                wall_group.add(wall_piece)
        elif i == 16:
            for j in range(18):
                wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                wall_group.add(wall_piece)
        elif i == 17:
            for j in range(19):
                wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                wall_group.add(wall_piece)
        elif i == 18:
            for j in range(20):
                wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                wall_group.add(wall_piece)
        elif i == 19:
            for j in range(22):
                if j < 1:
                    pass
                else:
                    wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group.add(wall_piece)
        elif i == 20:
            for j in range(22):
                if j < 2:
                    pass
                else:
                    wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group.add(wall_piece)
        elif i == 21:
            for j in range(22):
                if j < 3:
                    pass
                else:
                    wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group.add(wall_piece)
        elif i == 22:
            for j in range(22):
                if j < 4:
                    pass
                else:
                    wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group.add(wall_piece)
        elif i == 23:
            for j in range(22):
                if j < 5:
                    pass
                else:
                    wall_piece = Wall((w * 175) + (SCREEN_WIDTH // 6 + i * WALL_PIX_SIZE), (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group.add(wall_piece)

# basic rectangular walls finished
# for i in range(WALLS):
#     # create wall roofs
#     for j in range(5):
#         for k in range(WALL_WIDTH - ((1 + j) * WALL_PIX_SIZE)):
#             wall_piece = Wall(((i + 1) * (SCREEN_WIDTH // 5.5)) + (k + j) * WALL_PIX_SIZE,
#                               j * WALL_PIX_SIZE + SCREEN_HEIGHT - (220 + WALL_HEIGHT + 4))
#             wall_group.add(wall_piece)

# Create shot group
shots = pygame.sprite.Group()

# Create alien shot group
alien_shots = pygame.sprite.Group()

# Create alien fleet
# fleet_group = pygame.sprite.Group()
fleet_group = []
alien_count = 0

# Create fleet of aliens
for i in range(ROWS):
    # groups_list.append(pygame.sprite.Group())
    if i == 0:
        alien_path = POINTS_30
    elif i == 1:
        alien_path = POINTS_30
    elif i == 2:
        alien_path = POINTS_20
    elif i == 3:
        alien_path = POINTS_20
    elif i == 4:
        alien_path = POINTS_10
    else:
        alien_path = POINTS_10
    # Create one row of aliens
    for j in range(COLUMNS):
        # Each brick's starting position is
        # x = (j * width of the alien + half the size of the alien + offset from the left)
        # y = i * (height of the alien + space between lines) + offset from the top
        # print(colour)
        # new_alien = Alien((j * SCREEN_WIDTH // 13 + SCREEN_WIDTH // 9), i * (SCREEN_HEIGHT // 15) + 160, alien_path)
        new_alien = Alien((j * 1.5 * ALIEN_WIDTH + SCREEN_WIDTH // 9), i * (2 * ALIEN_HEIGHT) + 160, i, j, alien_path)
        # add alien to fleet group
        fleet_group.append(new_alien)
        # increase alien_count
        alien_count += 1
# ----------------------------------------------------------------------------------------------------------------------

# Game loop
clock = pygame.time.Clock()
game_on = True
movement_time = time.time()
shoot_time = time.time()
movement_delay = MOVEMENT_DELAY
i = 0
life_icon = pygame.image.load(SPACESHIP_PATH).convert_alpha()
life_icon.set_colorkey(BLACK, pygame.RLEACCEL)

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
        hit = shot.collision_detect(fleet_group, wall_group, scoreboard)
        # when alien is hit, decrease alien count
        if hit:
            alien_count -= 1
    # Pressed down keys boolean list - 0 for keys not pressed and 1 for keys pressed
    pressed_keys = pygame.key.get_pressed()

    # Control spaceship - create shots
    if spaceship.control(pressed_keys):
        shots.add(Shot(position=spaceship.corner))

    # Aliens movement and shooting -------------------------------------------------------------------------------------
    # TODO - make another type of alien shot (rocket?)
    # TODO - make alien shots animated
    # TODO - make the "boss" alien spaceship appear

    # Make random alien shoot
    if time.time() - shoot_time > ALIEN_SHOOT_DELAY:
        random_alien = None
        while True:
            shoot_time = time.time()
            random_alien = choice(fleet_group)
            # check whether alien is None
            if random_alien is None:
                # force the next iteration
                continue
            # calculate alien's position
            #random_alien_pos = random_alien.row * COLUMNS + random_alien.column
            # make sure only alien with no other aliens in the rows in front of it can shoot
            # calculate positions in front of alien
            # check the same position in the rows in front of alien
            can_shoot = True
            for j in range(random_alien.row + 1, ROWS):
                position = j * COLUMNS + random_alien.column
                # if there is an alien in front of random_alien, it can't shoot
                if fleet_group[position] is not None:
                    can_shoot = False
                    break
            # if random_alien is clear to shoot, exit the while loop
            if can_shoot:
                break

        alien_shots.add(AlienShot(ALIEN_SHOT_PATH, random_alien.corner))


    # Collision detection and movement of existing alien shots
    for shot in alien_shots:
        shot.move()
        shot.collision_detect(wall_group, spaceship, scoreboard)

    # move aliens in intervals
    if time.time() - movement_time > movement_delay:
        movement_time = time.time()
        increase_speed = None

        # move only one row at each time
        # move starting from the last row
        # for alien in fleet_groups[len(fleet_groups) - 1 - i]:
        #     increase_speed = alien.move()

        for alien in fleet_group:
            if alien is not None:
                if alien.row == ROWS - i:
                    increase_speed = alien.move()
        # increase speed
        if increase_speed:
            movement_delay /= 1.025

        # increment row
        if i < ROWS:
            i += 1
        else:
            i = 0
    else:
        # do not move, but update anyway - for aliens that are being destroyed
        for alien in fleet_group:
            if alien is not None:
                alien.update_destroyed()

    # Rendering --------------------------------------------------------------------------------------------------------

    # Place the gaming area on the screen
    screen.blit(game_surface, (0, 0))

    # Render all aliens in the fleet
    for alien in fleet_group:
        # print(alien.corner)
        if alien is not None:
            screen.blit(alien.surface, alien.corner)

    # Place the ship on the screen
    # Places ship in the middle + spaceship corner(rect) position (changes when paddle moves)
    screen.blit(spaceship.surface, spaceship.corner)

    # Place the wall on the screen
    for wall_piece in wall_group:
        screen.blit(wall_piece.surface, wall_piece.corner)

    # Place player shots on the screen
    for shot in shots:
        screen.blit(shot.surface, shot.corner)

    # Place alien shots on the screen
    for shot in alien_shots:
        screen.blit(shot.surface, shot.corner)

    # Place score on the screen
    screen.blit(scoreboard.score_text, scoreboard.score_corner)
    # Place hi-score on the screen
    screen.blit(scoreboard.hi_score_text, scoreboard.hi_score_corner)
    # Place remaining lives on the screen
    screen.blit(scoreboard.lives_text, scoreboard.lives_corner)
    # Place green HUD line on the screen
    screen.blit(scoreboard.green_line, scoreboard.line_corner)

    # Place life icons on the screen
    for j in range(1, scoreboard.lives + 1):
        life_corner = life_icon.get_rect(center=(150 + j * 60, SCREEN_HEIGHT - 35))
        screen.blit(life_icon, life_corner)

    # Check whether there are any bricks left
    # Render End Game text - has to be the last to render, otherwise covered by other surfaces
    if alien_count == 0:
        # Play winning sound
        winning_sound.play()
        screen.blit(text_won, text_won_corner)
        pygame.display.update()
        # Wait for x milliseconds until closing the game
        pygame.time.delay(3000)
        game_on = False

    # Check whether player has any lives left
    # Render End Game text - has to be the last to render, otherwise covered by other surfaces
    if scoreboard.lives == 0:
        # Play losing sound
        winning_sound.play()
        screen.blit(text_lost, text_lost_corner)
        pygame.display.update()
        # Wait for x milliseconds until closing the game
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
