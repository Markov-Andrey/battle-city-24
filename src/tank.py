import pygame

class Tank(pygame.sprite.Sprite):
    block_size = 50  # Размер блока

    def __init__(self, x, y, image_paths, health, speed):
        super().__init__()
        self.image_paths = image_paths
        self.images = None
        self.image_index = 0
        self.load_images()  # Загружаем изображения танка
        self.image = self.images[self.image_index]  # Устанавливаем начальное изображение
        self.rect = self.image.get_rect()  # Получаем прямоугольник изображения
        self.rect.topleft = (x, y)  # Устанавливаем начальное положение танка
        self.speed = speed  # Одна скорость для всех направлений
        self.grid_width = 13  # Размеры сетки по умолчанию
        self.grid_height = 13
        self.direction = 'up'  # Начальное направление танка
        self.is_moving = False  # Флаг движения
        self.health = health  # Здоровье танка
        self.is_player = False  # По умолчанию танк не является игроком

    def load_images(self):
        # Загрузка изображений по указанным путям
        self.images = [pygame.transform.scale(pygame.image.load(path).convert_alpha(),
                                             (self.block_size, self.block_size)) for path in self.image_paths]

    def update(self):
        # Метод обновления состояния танка
        if self.is_moving:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.change_direction(self.direction)  # Поворачиваем изображение в текущее направление
        else:
            self.image = self.images[0]

    def move(self, direction):
        # Метод для перемещения танка по заданному направлению
        if direction == 'left':
            new_x = self.rect.x - self.speed
            if new_x >= 0:
                self.rect.x = new_x
        elif direction == 'right':
            new_x = self.rect.x + self.speed
            if new_x < self.grid_width * self.block_size - self.rect.width:  # учитываем ширину танка
                self.rect.x = new_x
        elif direction == 'up':
            new_y = self.rect.y - self.speed
            if new_y >= 0:
                self.rect.y = new_y
        elif direction == 'down':
            new_y = self.rect.y + self.speed
            if new_y < self.grid_height * self.block_size - self.rect.height:  # учитываем высоту танка
                self.rect.y = new_y
        self.is_moving = True
        self.direction = direction  # Обновляем направление танка

    def change_direction(self, direction):
        # Метод для изменения направления и поворота изображения
        if direction == 'left':
            self.image = pygame.transform.rotate(self.images[self.image_index], 90)
        elif direction == 'right':
            self.image = pygame.transform.rotate(self.images[self.image_index], -90)
        elif direction == 'down':
            self.image = pygame.transform.rotate(self.images[self.image_index], 180)
        else:  # 'up'
            self.image = self.images[self.image_index]
