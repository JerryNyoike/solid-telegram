import pygame

from .spaceship import Spaceship
from .enemy import AlienGenerator
from .rocket import Rocket
# from .DQN import DQNAgent


class Game:
    screen = None
    aliens = []
    rockets = []
    lost = False

    def __init__(self, width, height):
        pygame.init()
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        ship = Spaceship(self, width / 2, height - 20)
        alien_generator = AlienGenerator()
        print(alien_generator.width)

        # Generate enemies
        alien_generator.generate(self)
        rocket = None

        while not done:
            if len(self.aliens) == 0:
                self.display_text("Victory achieved!")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                ship.x -= 2 if ship.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                ship.x += 2 if ship.x < width - 20 else 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, ship.x, ship.y))

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            # Draw the aliens
            for alien in self.aliens:
                alien.draw()
                if (alien.y - 32) > height:
                    self.lost = True
                    self.display_text("Mission FAILED!")
                alien.check_collision(self)

            # Draw rockets
            for rocket in self.rockets:
                rocket.draw()

            if not self.lost:
                ship.draw()

    def display_text(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.screen.blit(textsurface, (110, 160))
