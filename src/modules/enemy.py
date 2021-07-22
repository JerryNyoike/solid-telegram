import pygame


class Alien:
    def __init__(self, game, x, y):
        self.y = y
        self.x = x
        self.game = game
        self.size = 30

    def draw(self):
        pygame.draw.rect(self.game.screen, (81, 43, 88), pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05

    def check_collision(self, game, agent=None):
        for rocket in game.rockets:
            collided = self.collision(rocket)
            if self.collision(rocket):
                game.rockets.remove(rocket)
                game.aliens.remove(self)
            
                if agent != None:
                    reward = agent.set_reward(game.ship, collided, game.lost)

    def collision(self, rocket):
        return rocket.x < self.x + self.size and rocket.x > self.x - self.size and rocket.y < self.y + self.size and rocket.y > self.y - self.size

    def x_cordinates(self):
        return self.x, self.x + size


class AlienGenerator:
    margin = 30
    width = 50

    def generate(self, game):
        for x in range(self.margin, game.width - self.margin, self.width):
            for y in range(self.margin, int(game.height / 2), self.width):
                game.aliens.append(Alien(game, x, y))
