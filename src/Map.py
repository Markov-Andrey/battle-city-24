import pygame
from src.Block import Block  # Импортируем класс Block для создания блоков

class Map:
    def __init__(self, block_size):
        self.block_size = block_size
        self.blocks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def generate_blocks(self):
        # Пример данных карты (двумерный список)
        map_data = [
            [1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1],
        ]

        for row in range(len(map_data)):
            for col in range(len(map_data[row])):
                if map_data[row][col] == 1:
                    x = col * self.block_size  # Вычисляем координаты блока на основе индекса
                    y = row * self.block_size
                    block = Block(x, y, 50, 50)  # Создаем блок с физическим размером 50x50
                    self.blocks.add(block)
                    self.all_sprites.add(block)  # Добавляем блок в общую группу спрайтов

        return self.blocks, self.all_sprites
