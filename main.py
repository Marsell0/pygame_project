import pygame


class Game:
    def __init__(self):
        self.weight = 800
        self.height = 650
        self.fps = 60
        self.win = pygame.display.set_mode((self.weight, self.height))
        pygame.display.set_caption('Pixel Defense')
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        self.win.fill(pygame.Color('black'))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            self.clock.tick(self.fps)
        pygame.quit()


if __name__ == '__main__':
    Game().run()