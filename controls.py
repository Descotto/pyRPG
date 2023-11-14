import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.rect = self.image.get_rect(bottomleft = pos)

        # graphic
        full_path = './assets/chrono/buttons/{pos}'
        self.image = pygame.image.load(full_path).convert_alpha()

