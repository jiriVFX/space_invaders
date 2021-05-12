from constants import *
import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hi_score = 0
        self.score = 0
        self.lives = LIVES
        self.font = pygame.font.SysFont("Consolas", 25, bold=False)
        # score text
        self.score_text = self.font.render(f"SCORE: {self.score}", True, WHITE)
        self.score_corner = self.score_text.get_rect(topleft=(40, 40))
        # hi-score text
        self.hi_score_text = self.font.render(f"HI-SCORE: {self.hi_score}", True, WHITE)
        self.hi_score_corner = self.score_text.get_rect(topright=(SCREEN_WIDTH - 80, 40))
        # lives text
        self.lives_text = self.font.render(f"LIVES: {self.lives}", True, WHITE)
        self.lives_corner = self.lives_text.get_rect(topleft=(40, SCREEN_HEIGHT - 45))
        # hud line
        self.green_line = pygame.Surface((SCREEN_WIDTH, GREEN_LINE_HEIGHT))
        self.green_line.fill(GREEN)
        self.line_corner = self.lives_text.get_rect(topleft=(0, SCREEN_HEIGHT - 70))

        # for i in range(1, self.lives + 1):
        #     life_icon = pygame.image.load(SPACESHIP_PATH).convert_alpha()
        #     life_icon.set_colorkey(BLACK, pygame.RLEACCEL)
        #     life_corner = life_icon.get_rect(center=(150 + i * 60, SCREEN_HEIGHT - 35))

    def update_score(self):
        self.score_text = self.font.render(f"SCORE: {self.score}", True, WHITE)
        self.lives_text = self.font.render(f"LIVES: {self.lives}", True, WHITE)

    def increase(self):
        self.score += 1
        self.update_score()

    def decrease(self):
        if self.score >= 5:
            self.score -= 5
        else:
            self.score = 0
        self.update_score()

    def remove_life(self):
        if self.lives > 0:
            self.lives -= 1
            self.update_score()
        # print("life removed.")
        # print(f"Lives: {self.lives}")
