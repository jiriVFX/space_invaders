from constants import *
import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.font = pygame.font.SysFont("Consolas", 20, bold=True)
        # score text
        self.score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.corner = self.score_text.get_rect(center=(80, 40))
        # lives text
        self.lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        self.lives_corner = self.lives_text.get_rect(center=(80, SCREEN_HEIGHT - 40))

    def update_score(self):
        self.score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)

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
