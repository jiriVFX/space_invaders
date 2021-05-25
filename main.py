import pygame
from constants import *
from spaceship import SpaceShip
from alien import Alien
from shot import Shot
from alien_shot import AlienShot
from scoreboard import Scoreboard
from wall import Wall
from helper_functions import *
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
text_won = font.render("YOU WON!", True, RED)
text_won_corner = text_won.get_rect(center=((SCREEN_WIDTH) / 2, SCREEN_HEIGHT / 2 - 300))
text_lost = font.render("GAME OVER", True, RED)
text_lost_corner = text_won.get_rect(center=((SCREEN_WIDTH) / 2, SCREEN_HEIGHT / 2 - 300))

# Sounds
collision_sound = pygame.mixer.Sound("static/sound/hit1.mp3")
winning_sound = pygame.mixer.Sound("static/sound/chime.mp3")

# Gaming area surface
game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
game_surface.fill(DARK_GREY)
# rect = game_space.get_rect()

# Create wall groups
#wall_group = pygame.sprite.Group()
wall_group_list = []

for group in range(WALLS):
    wall_group_list.append(pygame.sprite.Group())

# Create walls, pixel by pixel
build_wall(wall_group_list)

# Create spaceship
spaceship = SpaceShip(SPACESHIP_PATH)

# Create shot group
shots = pygame.sprite.Group()

# Create alien shot group
alien_shots = pygame.sprite.Group()

# Create alien fleet
fleet_group = []
alien_count = 0

# Create fleet of aliens
alien_count = create_alien_fleet(fleet_group)

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
out_of_screen = False
alien_rows = [False for _ in range(ROWS)]
turned_counter = 0
out_of_bounds = True

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
        if shot.destruct_start_time is None:
            shot.move()
            hit = shot.collision_detect(fleet_group, wall_group_list, alien_shots, scoreboard)
            # when alien is hit, decrease alien count
            if hit:
                alien_count -= 1
        else:
            shot.update_destroyed()

    # Pressed down keys boolean list - 0 for keys not pressed and 1 for keys pressed
    pressed_keys = pygame.key.get_pressed()

    # Control spaceship - create shots
    if spaceship.control(pressed_keys):
        shots.add(Shot(position=spaceship.corner))

    # Update destroyed spaceship
    if spaceship.destruct_start_time is not None:
        spaceship.update_destroyed()

    # Aliens movement and shooting -------------------------------------------------------------------------------------
    # TODO - aliens have move in wider lines, if all aliens on either side have been destroyed
    # TODO - make the "boss" alien spaceship appear
    # TODO - Add sounds

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
            # random_alien_pos = random_alien.row * COLUMNS + random_alien.column
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

        alien_shots.add(AlienShot(ALIEN_SHOT_PATHS, random_alien.corner))

    # Collision detection and movement of existing alien shots
    for alien_shot in alien_shots:
        if alien_shot.destruct_start_time is None:
            alien_shot.move()
            alien_shot.collision_detect(wall_group_list, scoreboard.green_line, spaceship, scoreboard)
        else:
            alien_shot.update_destroyed()

    # move aliens in intervals
    if time.time() - movement_time > movement_delay:
        movement_time = time.time()
        increase_speed = None

        # recalculate alien movement speed based on number of aliens on each side
        # find first position on the right and on the left
        # max_left = None
        # max_right = None
        # for alien in fleet_group:
        #     if alien is not None:
        #         if max_left is None or max_left > alien.column:
        #             max_left = alien.column
        #         if max_right is None or max_right < alien.column:
        #             max_right = alien.column

        # # calculate number of empty columns
        # missing_columns = COLUMNS - ((max_right - max_left) + 1)
        # # Number of movements to each side increases with each missing column
        # movements_num = MOVEMENTS_NUM + (MOVEMENTS_NUM * missing_columns)

        #print(missing_columns)
        #print(movements_num)

        # find out what rows have crossed the boundaries
        if turned_counter == 0:
            for alien in fleet_group:
                if alien is not None and (alien.corner.left <= 40 or alien.corner.right >= SCREEN_WIDTH - 40):
                    for j in range(ROWS):
                        if alien.row == j:
                            alien_rows[j] = True

            # Check whether any row has not crossed the boundaries yet
            out_of_bounds = True
            for row in alien_rows:
                if row is False:
                    out_of_bounds = False
                    break
            print(alien_rows)
            print(out_of_bounds)

        # move only one row each time
        for alien in fleet_group:
            if alien is not None:
                # move starting from the last row
                if alien.row == ROWS - i:
                    # if all the rows crossed boundaries, turn aliens around and step down
                    if out_of_bounds and turned_counter <= ROWS:
                        alien.direction *= -1
                        alien.step_down()

                    increase_speed = alien.move()

                    # alien and wall collision detection
                    alien.collision_detection(wall_group_list)
                    # check whether alien crossed the bottom part of the screen
                    out_of_screen = alien.out_of_screen()

        # keep track of number of turned around rows
        if out_of_bounds and turned_counter <= ROWS:
            turned_counter += 1
            print(f"turned_counter = {turned_counter}")
        else:
            # reset counter and alien_rows when all the rows turned around
            turned_counter = 0
            alien_rows = [False for _ in range(ROWS)]
            print("Counter reset")

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
        if alien is not None:
            screen.blit(alien.surface, alien.corner)

    # Place the ship on the screen
    # Places ship in the middle + spaceship corner(rect) position (changes when paddle moves)
    if spaceship.surface is not None:
        screen.blit(spaceship.surface, spaceship.corner)

    # Place the wall on the screen
    for wall_group in wall_group_list:
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
    for pixel in scoreboard.green_line:
        if pixel is not None:
            screen.blit(pixel["pixel"], pixel["corner"])

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
    # Check whether aliens crossed the bottom of the screen
    # Render End Game text - has to be the last to render, otherwise covered by other surfaces
    if scoreboard.lives == 0 or out_of_screen:
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
