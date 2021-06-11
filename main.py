import pygame
from constants import *
from spaceship import SpaceShip
from shot import Shot
from alien_shot import AlienShot
from scoreboard import Scoreboard
from boss import Boss
from helper_functions import *
import time
from random import choice

# Initialize pygame
pygame.init()

# ======================================================================================================================

# Create screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Space Invaders")
# Set background colour
screen.fill(WHITE)

# Scoreboard
scoreboard = Scoreboard()

# Load window icon
icon = pygame.image.load(WINDOW_ICON)
pygame.display.set_icon(icon)

# Font
pygame.font.init()
font = pygame.font.SysFont("Consolas", 40, bold=True)
text_hiscore = font.render(f"{scoreboard.hi_score} POINTS!", True, RED)
text_hiscore_corner = text_hiscore.get_rect(center=((SCREEN_WIDTH) / 2, SCREEN_HEIGHT / 2 - 120))

# Sounds
game_over_sound = pygame.mixer.Sound("static/sound/space_tunnel.mp3")
alien_move_sounds = (pygame.mixer.Sound(ALIEN_MOVEMENT_SOUND_1), pygame.mixer.Sound(ALIEN_MOVEMENT_SOUND_2),
                     pygame.mixer.Sound(ALIEN_MOVEMENT_SOUND_3), pygame.mixer.Sound(ALIEN_MOVEMENT_SOUND_4))

# Gaming area surface
game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
game_surface.fill(DARK_GREY)

# Signature
signature = pygame.image.load("static/img/signature.png").convert_alpha()
signature.set_colorkey(BLACK, pygame.RLEACCEL)
signature_corner = signature.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))

# Game over text
game_over = create_game_over_text()

# Create New hi-score text
hi_score = create_hiscore_text()

# Create wall groups
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

# Create boss - boss is randomly created during gameplay
boss_group = pygame.sprite.Group()

# ======================================================================================================================

# Game loop
clock = pygame.time.Clock()
game_on = True
boss_time = time.time()
movement_time = time.time()
movement_sound_time = time.time()
shoot_time = time.time()
movement_delay = MOVEMENT_DELAY
movement_sound_delay = movement_delay + MOVEMENT_SOUND_DELAY
movement_sound_counter = 0
i = 0
life_icon = pygame.image.load(SPACESHIP_PATH).convert_alpha()
life_icon.set_colorkey(BLACK, pygame.RLEACCEL)
out_of_screen = False
alien_rows = [False for _ in range(ROWS)]
turned_counter = 0
out_of_bounds = False
last_char_time = None
# end text iterator
end_iter = 0
# new hi-score text iterator
hi_score_iter = 0

while game_on:
    # Quit the game when X is clicked or Esc pressed to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False

    # Player Shot collision detection and spaceship movement ===========================================================

    # Collision detection and movement of existing player shots
    for shot in shots:
        if shot.destruct_start_time is None:
            shot.move()
            hit = shot.collision_detect(fleet_group, wall_group_list, alien_shots, boss_group, scoreboard)
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

    # Aliens movement and shooting =====================================================================================

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

    # Collision detection and movement of existing alien shots ---------------------------------------------------------
    for alien_shot in alien_shots:
        if alien_shot.destruct_start_time is None:
            alien_shot.move()
            alien_shot.collision_detect(wall_group_list, scoreboard.green_line, spaceship, scoreboard)
        else:
            alien_shot.update_destroyed()

    # play alien movement sounds in intervals --------------------------------------------------------------------------
    # sounds in the original game are not played synchronously with the movement
    # so we have to make a separate timer to play movement sounds
    if time.time() - movement_sound_time > movement_sound_delay:
        movement_sound_time = time.time()
        # play alien movement sound
        alien_move_sounds[movement_sound_counter].play()
        # increment or reset sound counter
        if movement_sound_counter < len(alien_move_sounds) - 1:
            movement_sound_counter += 1
        else:
            movement_sound_counter = 0

    # move aliens in intervals -----------------------------------------------------------------------------------------
    if time.time() - movement_time > movement_delay:
        movement_time = time.time()

        # find out if any column has crossed the boundaries
        if turned_counter == 0:
            out_of_bounds = False
            for alien in fleet_group:
                # update aliens being destroyed
                # updating even here to reduce glitches when explosion is not displayed
                if alien is not None:
                    alien.update_destroyed()

                # check whether any alien crossed the boundaries
                if alien is not None and (alien.corner.left <= 40 or alien.corner.right >= SCREEN_WIDTH - 40):
                    column_crossed = alien.column
                    out_of_bounds = True
                    # find all aliens in the same column and check if they crossed the boundaries too
                    # not very efficient, but the only working solution from those tested so far
                    for another_alien in fleet_group:
                        if another_alien is not None and another_alien.column == column_crossed:
                            if another_alien.corner.left > 40 and another_alien.corner.right < SCREEN_WIDTH - 40:
                                out_of_bounds = False
                                break
                    break

        # move only one row each time
        for alien in fleet_group:
            if alien is not None:
                # move starting from the last row
                if alien.row == ROWS - i:
                    # if all aliens in the column crossed boundaries, turn aliens around and step down
                    if out_of_bounds and turned_counter <= ROWS:
                        alien.direction *= -1
                        alien.step_down()
                        # print("Turning around")
                    alien.move()
                    # alien and wall collision detection
                    alien.collision_detection(wall_group_list)
                    # check whether alien crossed the bottom part of the screen
                    out_of_screen = alien.out_of_screen()

        # keep track of number of turned around rows
        # print(out_of_bounds)
        if out_of_bounds and turned_counter <= ROWS:
            turned_counter += 1
        else:
            # reset counter and alien_rows when all the rows turned around
            turned_counter = 0

        # increase speed based on number of missing side columns -------------------------------------------------------
        existing_columns = [0 for _ in range(COLUMNS)]
        for alien in fleet_group:
            # record missing columns
            for j in range(COLUMNS):
                if alien is not None and alien.column == j:
                    existing_columns[j] = 1

        missing_columns = 0
        start = 0
        # iterate from the start until finding column (1)
        while start != len(existing_columns) - 1:
            if existing_columns[start] == 0:
                missing_columns += 1
            else:
                break
            start += 1

        # prevent from iterating if whole list was already iterated over
        if start != len(existing_columns) - 1:
            end = len(existing_columns) - 1
            # iterate from the end until finding column (1)
            while end != 0:
                if existing_columns[end] == 0:
                    missing_columns += 1
                else:
                    break
                end -= 1

        # recalculate speed --------------------------------------------------------------------------------------------
        movement_delay = MOVEMENT_DELAY - (missing_columns * (MOVEMENT_DELAY / (COLUMNS - 1)))
        # further increase speed if only one column is left
        if COLUMNS - missing_columns == 2:
            for alien in fleet_group:
                if alien is not None:
                    alien.alien_movement = int(1.5 * ALIEN_MOVEMENT)
        elif COLUMNS - missing_columns <= 1:
            print(COLUMNS - missing_columns)
            for alien in fleet_group:
                if alien is not None:
                    alien.alien_movement = 2 * ALIEN_MOVEMENT

        movement_sound_delay = MOVEMENT_SOUND_DELAY - (missing_columns * (MOVEMENT_SOUND_DELAY / 1.1 / (COLUMNS - 1)))

        if movement_delay <= 0:
            movement_delay = 0.000000001
        if movement_sound_delay <= 0:
            movement_delay = 0.000000001

        # increment row ------------------------------------------------------------------------------------------------
        if i < ROWS:
            i += 1
        else:
            i = 0
    else:
        # do not move, but update anyway - for aliens that are being destroyed
        for alien in fleet_group:
            if alien is not None:
                alien.update_destroyed()

    # Creation, movement and out of screen detection of alien boss -----------------------------------------------------
    if time.time() - boss_time > BOSS_APPEARANCE_DELAY:
        boss_time = time.time()
        # create a boss if BOSS_APPEARANCE_DELAY has passed
        boss_group.add(Boss())
        # 50% chance of boss creation
        # random_num = random.randint(0, 1)
        # if random_num == 0:
        #     boss = Boss()
    for boss in boss_group:
        if boss is not None:
            if boss.destruct_start_time is None:
                boss.move()
                boss.out_of_screen()
            else:
                boss.update_destroyed()

    # Rendering ========================================================================================================

    # Place the gaming area on the screen
    screen.blit(game_surface, (0, 0))

    # Place signature on the screen
    screen.blit(signature, signature_corner)

    # Render all aliens in the fleet
    for alien in fleet_group:
        if alien is not None:
            screen.blit(alien.surface, alien.corner)

    # Place Boss on the screen
    for boss in boss_group:
        if boss is not None:
            screen.blit(boss.surface, boss.corner)

    # Place the ship on the screen
    # Places spaceship in the middle + spaceship corner(rect) position (changes when spaceship moves)
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

    # Render end screen text -------------------------------------------------------------------------------------------
    # Check whether player has any lives left
    # Check whether aliens crossed the bottom of the screen
    # Render End Game text - has to be the last to render, otherwise covered by other surfaces
    if scoreboard.lives == 0 or out_of_screen or alien_count == 0:
        # stop playing any alien boss sounds
        for boss in boss_group:
            boss.stop_sound()

        # Play game over sound
        game_over_sound.play()

        # Write game over text
        write_game_over(end_iter, game_over, last_char_time, screen)

        if scoreboard.score > scoreboard.hi_score:
            # Write new hi-score text
            write_new_hiscore(scoreboard, hi_score, hi_score_iter, last_char_time, text_hiscore, font, screen)
            # update to show the rendered text
            text_hiscore = font.render(f"{scoreboard.hi_score} POINTS!", True, RED)
            # place text on the screen
            screen.blit(text_hiscore, text_hiscore_corner)
            # update to show the rendered text
            pygame.display.update()
        # Wait for x milliseconds until closing the game
        pygame.time.delay(END_SCREEN_TIME)
        game_on = False

    # Refresh display
    pygame.display.flip()

    # Set refresh rate to 60 times per second (60Hz/FPS)
    clock.tick(60)

# Quit all the sounds and the game =====================================================================================
pygame.mixer.quit()
pygame.quit()
