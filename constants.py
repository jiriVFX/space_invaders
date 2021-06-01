# Colours
BLACK = (255, 255, 255)
DARK_GREY = (42, 42, 42)
GREEN = (0, 255, 0)
RED = (180, 0, 0)
WHITE = (230, 230, 230)

# Screen
SCREEN_WIDTH = 920
SCREEN_HEIGHT = 1010

# Spaceship
SPACESHIP_WIDTH = 44
SPACESHIP_HEIGHT = 10
SPACESHIP_PATH = "static/img/spaceship.png"
PLAYER_SHOT_EXPLOSION = "static/img/player_shot_explosion.png"
PLAYER_SHOT_EXPLOSION_RED = "static/img/player_shot_explosion_red.png"
SHOT_EXPLOSION_WIDTH = 32
SPACESHIP_EXPLOSION_1 = "static/img/spaceship_explosion_1.png"
SPACESHIP_EXPLOSION_2 = "static/img/spaceship_explosion_2.png"
LIVES = 3
# spaceship destruction time in milliseconds
SPACESHIP_DESTRUCTION_TIME = 900
# spaceship explosion time in milliseconds
SPACESHIP_EXPLOSION_TIME = 50
# player shot penetration - how many pieces of wall shot destroys before its own destruction
PLAYER_SHOT_PENETRATION = 4

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
ALIEN_BOSS_WIDTH = 60
ALIEN_BOSS_Y_POS = 100
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

# distance of the first alien row from the top of the screen
ALIEN_TOP_OFFSET = 120
# speed of animation of the alien shots, lower is faster
ALIEN_SHOT_UPDATE_SPEED = 8
POINTS_10 = ("static/img/10_points_1.png", "static/img/10_points_2.png")
POINTS_20 = ("static/img/20_points_1.png", "static/img/20_points_2.png")
POINTS_30 = ("static/img/30_points_1.png", "static/img/30_points_2.png")
POINTS_100 = "static/img/100_points_1.png"
ALIEN_10_POINTS = 10
ALIEN_20_POINTS = 20
ALIEN_30_POINTS = 30
ALIENS_BOSS_POINTS = 100
ALIEN_EXPLOSION = "static/img/alien_explosion.png"
ALIEN_BOSS_EXPLOSIONS = ("static/img/alien_boss_explosion_1.png", "static/img/alien_boss_explosion_2.png")
ALIEN_SHOT_EXPLOSION = "static/img/alien_shot_explosion.png"
ALIEN_SHOT_EXPLOSION_GREEN = "static/img/alien_shot_explosion_green.png"
ALIEN_SHOT_EXPLOSION_HEIGHT = 32
MOVEMENT_DELAY = 0.20
ALIEN_MOVEMENT = 10
BOSS_MOVEMENT = 2
BOSS_APPEARANCE_DELAY = 25
ALIEN_SHOOT_DELAY = 1
ALIEN_SHOT_SPEED = 5
# shot penetration - how many pieces of wall shot destroys before its own destruction
ALIEN_SHOT_PENETRATION = 6
# alien destruction time in milliseconds
DESTRUCTION_TIME = 250
BOSS_DESTRUCTION_TIME = 1200

# Shot
SHOT_SPEED = 10
# Shot delay in seconds
SHOT_DELAY = 0.5

# HUD line height
GREEN_LINE_SIZE = 4

# Sounds
HIT_SOUND_1 = "static/sound/hit1.mp3"
HIT_SOUND_2 = "static/sound/hit2.mp3"