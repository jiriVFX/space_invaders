# Colours
BLACK = (255, 255, 255)
DARK_GREY = (42, 42, 42)
GREEN = (0, 255, 0)
RED = (180, 0, 0)
WHITE = (230, 230, 230)

# High score file path
HI_SCORE_PATH = "high_score.json"

# Screen
SCREEN_WIDTH = 920
SCREEN_HEIGHT = 1010

# game window icon
WINDOW_ICON = "static/img/icon.png"

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
# spaceship movement speed
SPACESHIP_MOVEMENT_SPEED = 5
# spaceship destruction time in milliseconds
SPACESHIP_DESTRUCTION_TIME = 900
# time before displaying new spaceship sprite after sprite removal when explosion is done
SPACESHIP_DOWNTIME = 400
# spaceship explosion time in milliseconds
SPACESHIP_EXPLOSION_TIME = 50
# player shot penetration - how many pieces of wall shot destroys before its own destruction
PLAYER_SHOT_PENETRATION = 4
# Shot
SHOT_SPEED = 15
# Shot delay in seconds
SHOT_DELAY = 1

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

# HUD line height
GREEN_LINE_SIZE = 4

# game over text
GAME_OVER = ("static/img/game_over/g.png", "static/img/game_over/a.png", "static/img/game_over/m.png",
             "static/img/game_over/e.png", "static/img/game_over/o.png", "static/img/game_over/v.png",
             "static/img/game_over/e.png", "static/img/game_over/r.png")
# hi-score text
HI_SCORE = ("static/img/game_over/n.png", "static/img/game_over/e.png", "static/img/game_over/w.png",
            "static/img/game_over/h.png", "static/img/game_over/i.png", "static/img/game_over/dash.png",
            "static/img/game_over/s.png", "static/img/game_over/c.png", "static/img/game_over/o.png",
            "static/img/game_over/r.png", "static/img/game_over/e.png")
# space between letter corner (rects)
LETTER_SPACING = 29
HALF_GAMEOVER_SIZE = 115
HALF_HISCORE_SIZE = 160
WORD_SPACE = 28
CHAR_INTERVAL = 100

# Sounds
MOVEMENT_SOUND_DELAY = 0.75
ALIEN_EXPLOSION_SOUND = "static/sound/alien_explosion.wav"
ALIEN_MOVEMENT_SOUND_1 = "static/sound/alien_movement_1.wav"
ALIEN_MOVEMENT_SOUND_2 = "static/sound/alien_movement_2.wav"
ALIEN_MOVEMENT_SOUND_3 = "static/sound/alien_movement_3.wav"
ALIEN_MOVEMENT_SOUND_4 = "static/sound/alien_movement_4.wav"
BOSS_SOUND = "static/sound/boss.wav"
BOSS_EXPLOSION_SOUND = "static/sound/boss_explosion.wav"
SHOOT_SOUND = "static/sound/shoot.wav"
PLAYER_EXPLOSION_SOUND = "static/sound/player_explosion.wav"

# end screen time
END_SCREEN_TIME = 5000
