from constants import *
from wall import Wall
from alien import Alien


def build_wall(wall_group_list):
    """
    Builds protective barrier walls with Wall class objects.
    :param wall_group_list: pygame.sprite.Group()
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
            new_alien = Alien((j * 1.5 * ALIEN_WIDTH + SCREEN_WIDTH // 9), i * (2 * ALIEN_HEIGHT) + 160, i, j,
                              alien_path)
            # add alien to fleet group
            fleet_group.append(new_alien)
            # increase alien_count
            alien_count += 1

    return alien_count
