from constants import *
import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.font = pygame.font.SysFont("Consolas", 20, bold=True)
        self.score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.corner = self.score_text.get_rect(center=(SCREEN_WIDTH - 80, 40))

    def update_score(self):
        self.score_text = self.font.render(f"Score: {self.score}", True, WHITE)

    def increase(self):
        self.score += 1
        self.update_score()

    def decrease(self):
        if self.score >= 5:
            self.score -= 5
        else:
            self.score = 0
        self.update_score()
