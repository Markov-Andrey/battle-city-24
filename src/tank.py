import pygame
import sys

class Tank(pygame.sprite.Sprite):
    block_size = 50  # Размер блока

    def __init__(self, x, y, image_paths, health, speed):
        super().__init__()
        self.image_paths = image_paths
        self.images = None
        self.image_index = 0
        self.image = self.images[self.image_index] if self.images else None
        self.rect = self.image.get_rect() if self.image else pygame.Rect(x, y, self.block_size, self.block_size)
        self.rect.topleft = (x, y)
        self.speed = speed  # Одна скорость для всех направлений
        self.grid_width = 13  # Размеры сетки по умолчанию
        self.grid_height = 13
        self.direction = 'up'
        self.is_moving = False
        self.health = health

    def load_images(self):
        # Загрузка изображений по указанным путям
        self.images = [pygame.transform.scale(pygame.image.load(path).convert_alpha(),
                                             (self.block_size, self.block_size)) for path in self.image_paths]

    def update(self):
        keys = pygame.key.get_pressed()

        # Сохранение предыдущей позиции
        prev_x, prev_y = self.rect.x, self.rect.y

        # Проверка наличия нажатия клавиш перемещения
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            self.is_moving = True
        else:
            self.is_moving = False

        # Переключение между изображениями для создания эффекта анимации, только если танк двигается
        if self.is_moving:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]

        # Управление движением танка с учетом ограничений карты
        if keys[pygame.K_LEFT]:
            self.direction = 'left'
            new_x = self.rect.x - self.speed
            if new_x >= 0:
                self.rect.x = new_x
        elif keys[pygame.K_RIGHT]:
            self.direction = 'right'
            new_x = self.rect.x + self.speed
            if new_x < self.grid_width * self.block_size - self.rect.width:  # учитываем ширину танка
                self.rect.x = new_x
        elif keys[pygame.K_UP]:
            self.direction = 'up'
            new_y = self.rect.y - self.speed
            if new_y >= 0:
                self.rect.y = new_y
        elif keys[pygame.K_DOWN]:
            self.direction = 'down'
            new_y = self.rect.y + self.speed
            if new_y < self.grid_height * self.block_size - self.rect.height:  # учитываем высоту танка
                self.rect.y = new_y

        # Поворот изображения в зависимости от направления
        if self.direction == 'left':
            self.image = pygame.transform.rotate(self.images[self.image_index], 90)
        elif self.direction == 'right':
            self.image = pygame.transform.rotate(self.images[self.image_index], -90)
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(self.images[self.image_index], 180)
        else:  # 'up'
            self.image = self.images[self.image_index]
