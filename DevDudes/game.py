import pygame

# Initializing pygame
pygame.init()

# Game Class
class Game:
    def __init__(self, width, height, title):
        # Setups
        self.SIZE = self.WIDTH, self.HEIGHT = width, height
        self.title = title
        self.clock = pygame.time.Clock()
        self.fps = 100
        self.running = False

        # Window creation
        self.window = pygame.display.set_mode(self.SIZE, flags=pygame.HIDDEN)
        pygame.display.set_caption(self.title)

    def run(self):
        # Showing the window
        self.window = pygame.display.set_mode(self.SIZE, flags=pygame.SHOWN)
        self.running = True

        # Game Loop
        while self.running:

            # Listening for pygame events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # Updating the display and ticking the clock
            pygame.display.update()
            self.clock.tick(self.fps)

        # Uninitializing pygame
        pygame.quit()
