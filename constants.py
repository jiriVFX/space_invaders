# Colours
BLUE = (0, 184, 255)
BLACK = (255, 255, 255)
DARK_GREY = (42, 42, 42)
GREEN = (0, 255, 0)
ORANGE = (255, 90, 0)
RED = (180, 0, 0)
WHITE = (230, 230, 230)
YELLOW = (255, 210, 0)

# Screen
SCREEN_WIDTH = 920
SCREEN_HEIGHT = 1000
BORDER = 5

# Spaceship
SPACESHIP_WIDTH = 44
SPACESHIP_HEIGHT = 10
SPACESHIP_PATH = "static/img/spaceship.png"
PLAYER_SHOT_EXPLOSION = "static/img/player_shot_explosion.png"
SPACESHIP_EXPLOSION_1 = "static/img/spaceship_explosion_1.png"
SPACESHIP_EXPLOSION_2 = "static/img/spaceship_explosion_2.png"
LIVES = 3
# spaceship destruction time in milliseconds
SPACESHIP_DESTRUCTION_TIME = 500
# spaceship explosion time in milliseconds
SPACESHIP_EXPLOSION_TIME = 50

# Walls
WALLS = 4
WALL_WIDTH = 24
WALL_HEIGHT = 22
WALL_PIX_SIZE = 4
WALL_OFFSET = 200
WALL_OFFSET_DIV = 8

# Aliens
COLUMNS = 11
ROWS = 6
ALIEN_HEIGHT = 32
ALIEN_WIDTH = 48
ALIEN_SHOT_PATHS = (
    "static/img/alien_shot/alien_shot_1.png",
    "static/img/alien_shot/alien_shot_2.png",
    "static/img/alien_shot/alien_shot_3.png",
    "static/img/alien_shot/alien_shot_4.png",
)
ALIEN_SHOT_2_PATHS = (
    "static/img/alien_shot_2/alien_shot_2_1.png",
    "static/img/alien_shot_2/alien_shot_2_2.png",
    "static/img/alien_shot_2/alien_shot_2_3.png",
    "static/img/alien_shot_2/alien_shot_2_4.png",
)
ALIEN_SHOT_3_PATHS = (
    "static/img/alien_shot_3/alien_shot_3_1.png",
    "static/img/alien_shot_3/alien_shot_3_2.png",
    "static/img/alien_shot_3/alien_shot_3_3.png",
    "static/img/alien_shot_3/alien_shot_3_4.png",
    "static/img/alien_shot_3/alien_shot_3_5.png",
    "static/img/alien_shot_3/alien_shot_3_6.png",
)
# speed of animation of the alien shots, lower is faster
ALIEN_SHOT_UPDATE_SPEED = 8
POINTS_10 = ("static/img/10_points_1.png", "static/img/10_points_2.png")
POINTS_20 = ("static/img/20_points_1.png", "static/img/20_points_2.png")
POINTS_30 = ("static/img/30_points_1.png", "static/img/30_points_2.png")
POINTS_100 = "static/img/30_points_1.png"
ALIEN_10_POINTS = 10
ALIEN_20_POINTS = 20
ALIEN_30_POINTS = 30
ALIENS_BOSS_POINTS = 100
ALIEN_EXPLOSION = "static/img/alien_explosion.png"
ALIEN_SHOT_EXPLOSION = "static/img/alien_shot_explosion.png"
MOVEMENT_DELAY = 0.25
ALIEN_MOVEMENT = 10
MOVEMENTS_NUM = 4
ALIEN_SHOOT_DELAY = 1
ALIEN_SHOT_SPEED = 5
# shot penetration - how many pieces of wall shot destroys before its own destruction
ALIEN_SHOT_PENETRATION = 5
# alien destruction time in milliseconds
DESTRUCTION_TIME = 250

# Shot
SHOT_SPEED = 10
# Shot delay in seconds
SHOT_DELAY = 0.5

# Collision sounds
HIT_SOUND_1 = "static/sound/hit1.mp3"
HIT_SOUND_2 = "static/sound/hit2.mp3"

# HUD line height
GREEN_LINE_SIZE = 4

