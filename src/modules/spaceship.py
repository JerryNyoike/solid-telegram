import pygame

class Spaceship:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen, (210, 250, 251), pygame.Rect(self.x, self.y, 8, 5))
