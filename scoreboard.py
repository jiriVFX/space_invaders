from constants import *
import pygame
import json


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hi_score = 0
        # load hi-score
        self.load_hi_score()
        self.score = 0
        self.lives = LIVES
        self.font = pygame.font.SysFont("Consolas", 25, bold=False)
        # score text
        self.score_text = self.font.render(f"SCORE: {self.score}", True, WHITE)
        self.score_corner = self.score_text.get_rect(topleft=(40, 40))
        # hi-score text
        self.hi_score_text = self.font.render(f"HI-SCORE: {self.hi_score}", True, WHITE)
        self.hi_score_corner = self.score_text.get_rect(topright=(SCREEN_WIDTH - 120, 40))
        # lives text
        self.lives_text = self.font.render(f"LIVES: {self.lives}", True, WHITE)
        self.lives_corner = self.lives_text.get_rect(topleft=(40, SCREEN_HEIGHT - 45))
        # create hud line
        self.green_line = []
        self.build_hud_line()
        # self.green_line = pygame.Surface((SCREEN_WIDTH, GREEN_LINE_HEIGHT))
        # self.green_line.fill(GREEN)
        # self.line_corner = self.lives_text.get_rect(topleft=(0, SCREEN_HEIGHT - 70))

    def load_hi_score(self):
        try:
            with open(HI_SCORE_PATH, "r") as file:
                data = json.load(file)
            self.hi_score = data["hi-score"]
            print(data["hi-score"])
        except FileNotFoundError:
            print("No previous hi-score found.")

    def write_hi_score(self):
        # update hi_score first
        self.update_hiscore()
        # write new hiscore
        data = {
            "hi-score": self.hi_score
        }
        with open(HI_SCORE_PATH, "w") as file:
            json.dump(data, file)
        print("New hi-score saved.")

    def update_hiscore(self):
        if self.score > self.hi_score:
            self.hi_score = self.score

    def build_hud_line(self):
        """Builds a green line from separate pygame.Surface objects on the bottom of the screen."""
        for i in range(SCREEN_WIDTH // GREEN_LINE_SIZE + 1):
            pixel = pygame.Surface((GREEN_LINE_SIZE, GREEN_LINE_SIZE))
            pixel.fill(GREEN)
            corner = pixel.get_rect(center=(i * GREEN_LINE_SIZE, SCREEN_HEIGHT - 70))
            dictionary = {
                "pixel": pixel,
                "corner": corner
            }
            self.green_line.append(dictionary)

    def update_score(self):
        self.score_text = self.font.render(f"SCORE: {self.score}", True, WHITE)
        # if self.score > self.hi_score:
        #     self.hi_score = self.score
        self.hi_score_text = self.font.render(f"HI-SCORE: {self.hi_score}", True, WHITE)
        self.lives_text = self.font.render(f"LIVES: {self.lives}", True, WHITE)

    def increase(self, alien):
        self.score += alien.points
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
