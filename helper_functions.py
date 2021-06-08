import pygame
from constants import *
from wall import Wall
from alien import Alien


def build_wall(wall_group_list):
    """
    Builds protective barrier walls with Wall class objects.
    :param wall_group_list: list[]
    :return:
    """
    for w in range(4):
        # columns
        for i in range(24):
            # rows
            if i < 5:
                for j in range(22):
                    if (i == 0 and j < 5) or (i == 1 and j < 4) or (i == 2 and j < 3) or (i == 3 and j < 2) or (
                            i == 4 and j < 1):
                        pass
                    else:
                        wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                          (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                        wall_group_list[w].add(wall_piece)
            elif i == 5:
                for j in range(20):
                    wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                      (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group_list[w].add(wall_piece)
            elif i == 6:
                for j in range(19):
                    wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                      (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group_list[w].add(wall_piece)
            elif i == 7:
                for j in range(18):
                    wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                      (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group_list[w].add(wall_piece)
            elif i == 8:
                for j in range(17):
                    wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                      (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group_list[w].add(wall_piece)
            elif 8 < i < 15:
                for j in range(16):
                    wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                      (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group_list[w].add(wall_piece)
            elif i == 15:
                for j in range(17):
                    wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                      (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group_list[w].add(wall_piece)
            elif i == 16:
                for j in range(18):
                    wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                      (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group_list[w].add(wall_piece)
            elif i == 17:
                for j in range(19):
                    wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                      (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group_list[w].add(wall_piece)
            elif i == 18:
                for j in range(20):
                    wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                      (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                    wall_group_list[w].add(wall_piece)
            elif i == 19:
                for j in range(22):
                    if j < 1:
                        pass
                    else:
                        wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                          (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                        wall_group_list[w].add(wall_piece)
            elif i == 20:
                for j in range(22):
                    if j < 2:
                        pass
                    else:
                        wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                          (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                        wall_group_list[w].add(wall_piece)
            elif i == 21:
                for j in range(22):
                    if j < 3:
                        pass
                    else:
                        wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                          (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                        wall_group_list[w].add(wall_piece)
            elif i == 22:
                for j in range(22):
                    if j < 4:
                        pass
                    else:
                        wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                          (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                        wall_group_list[w].add(wall_piece)
            elif i == 23:
                for j in range(22):
                    if j < 5:
                        pass
                    else:
                        wall_piece = Wall((w * WALL_OFFSET) + (SCREEN_WIDTH // WALL_OFFSET_DIV + i * WALL_PIX_SIZE),
                                          (1 + j * WALL_PIX_SIZE) + SCREEN_HEIGHT - 250)
                        wall_group_list[w].add(wall_piece)


def create_alien_fleet(fleet_group):
    """
    Creates a fleet of aliens from Alien class objects
    :param fleet_group: list[int]
    :return: int
    """
    alien_count = 0

    for i in range(ROWS):
        if i == 0:
            alien_path = POINTS_30
            points = ALIEN_30_POINTS
        elif i == 1:
            alien_path = POINTS_30
            points = ALIEN_30_POINTS
        elif i == 2:
            alien_path = POINTS_20
            points = ALIEN_20_POINTS
        elif i == 3:
            alien_path = POINTS_20
            points = ALIEN_20_POINTS
        elif i == 4:
            alien_path = POINTS_10
            points = ALIEN_10_POINTS
        else:
            alien_path = POINTS_10
            points = 10
        # Create one row of aliens
        for j in range(COLUMNS):
            # Each brick's starting position is
            # x = (j * width of the alien + half the size of the alien + offset from the left)
            # y = i * (height of the alien + space between lines) + offset from the top
            new_alien = Alien((j * 1.5 * ALIEN_WIDTH + SCREEN_WIDTH // 9), i * (2 * ALIEN_HEIGHT) + ALIEN_TOP_OFFSET,
                              i, j, alien_path, points)
            # add alien to fleet group
            fleet_group.append(new_alien)
            # increase alien_count
            alien_count += 1

    return alien_count


def create_game_over_text():
    """
    Builds and returns a list of lists with GAME OVER chars and their rectangles (positions)
    :return: list[[pygame.image, pygame.image.get_rect]]
    """
    game_over = []
    for i in range(len(GAME_OVER)):
        char = pygame.image.load(GAME_OVER[i]).convert_alpha()
        char.set_colorkey(BLACK, pygame.RLEACCEL)
        if i < 4:
            char_corner = char.get_rect(center=((SCREEN_WIDTH / 2) - HALF_GAMEOVER_SIZE + (i * LETTER_SPACING),
                                                SCREEN_HEIGHT / 2 - 300))
        else:
            char_corner = char.get_rect(
                center=((SCREEN_WIDTH / 2) - HALF_GAMEOVER_SIZE + (i * LETTER_SPACING) + WORD_SPACE,
                        SCREEN_HEIGHT / 2 - 300))
        game_over.append([char, char_corner])
    return game_over


def write_game_over(end_iter, game_over, last_char_time, screen):
    """
    Renders game over text on the screen.
    :param end_iter: int
    :param game_over: list[pygame.image]
    :param last_char_time: int
    :param screen: pygame.display
    :return:
    """
    # write game over text
    while end_iter < len(game_over):
        if last_char_time is None or pygame.time.get_ticks() - last_char_time > CHAR_INTERVAL:
            last_char_time = pygame.time.get_ticks()
            screen.blit(game_over[end_iter][0], game_over[end_iter][1])
            end_iter += 1
        # update to show the rendered text
        pygame.display.update()


def create_hiscore_text():
    """
    Builds and returns a list of lists with NEW HI-SCORE chars and their rectangles (positions)
    :return: list[[pygame.image, pygame.image.get_rect]]
    """
    hi_score = []
    for i in range(len(HI_SCORE)):
        char = pygame.image.load(HI_SCORE[i]).convert_alpha()
        char.set_colorkey(BLACK, pygame.RLEACCEL)
        if i < 3:
            char_corner = char.get_rect(center=((SCREEN_WIDTH / 2) - HALF_HISCORE_SIZE + (i * LETTER_SPACING),
                                                SCREEN_HEIGHT / 2 - 200))
        else:
            char_corner = char.get_rect(
                center=((SCREEN_WIDTH / 2) - HALF_HISCORE_SIZE + (i * LETTER_SPACING) + WORD_SPACE,
                        SCREEN_HEIGHT / 2 - 200))
        hi_score.append([char, char_corner])

    return hi_score


def write_new_hiscore(scoreboard, hi_score, hi_score_iter, last_char_time, text_hiscore, font, screen):
    """
    Renders new hi-score text on the screen.
    :param scoreboard: scoreboard.Scoreboard
    :param hi_score: list[pygame.image]
    :param hi_score_iter: int
    :param last_char_time: int
    :param text_hiscore: font.render
    :param font: pygame.font.SysFont
    :param screen: pygame.display
    :return:
    """
    # Write high score
    if scoreboard.score > scoreboard.hi_score:
        scoreboard.write_hi_score()
    # Write new hi-score text
    while hi_score_iter < len(hi_score):
        if last_char_time is None or pygame.time.get_ticks() - last_char_time > CHAR_INTERVAL:
            last_char_time = pygame.time.get_ticks()
            screen.blit(hi_score[hi_score_iter][0], hi_score[hi_score_iter][1])
            hi_score_iter += 1
        pygame.display.update()
