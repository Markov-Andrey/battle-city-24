import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        # Загрузка изображения блока
        image_path = "assets/blocks/block1.png"
        loaded_image = pygame.image.load(image_path).convert_alpha()

        # Масштабирование изображения до указанных размеров
        self.image = pygame.transform.scale(loaded_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
