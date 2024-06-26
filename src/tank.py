# tank.py
import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, image_paths, health, speed):
        super().__init__()
        self.image_paths = image_paths
        self.images = self.load_images()  # Загружаем изображения танка
        self.image_index = 0
        self.image = self.images[self.image_index]  # Устанавливаем начальное изображение
        self.rect = self.image.get_rect(topleft=(x, y))  # Получаем прямоугольник изображения и устанавливаем его позицию
        self.speed = speed  # Скорость танка
        self.direction = 'up'  # Начальное направление танка
        self.is_moving = False  # Флаг движения
        self.health = health  # Здоровье танка

    def check_collision(self, blocks):
        block_collisions = pygame.sprite.spritecollide(self, blocks, False)
        for block in block_collisions:
            if pygame.sprite.collide_rect(self, block):
                if self.direction == 'left':
                    self.rect.left = block.rect.right
                elif self.direction == 'right':
                    self.rect.right = block.rect.left
                elif self.direction == 'up':
                    self.rect.top = block.rect.bottom
                elif self.direction == 'down':
                    self.rect.bottom = block.rect.top

                self.is_moving = False

    def load_images(self):
        return [pygame.transform.scale(pygame.image.load(path).convert_alpha(), (50, 50)) for path in self.image_paths]

    def update(self):
        if self.is_moving:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.change_direction(self.direction)  # Изменяем направление изображения в соответствии с направлением танка

    def move(self, direction):
        original_rect = self.rect.copy()  # Создаем копию текущего прямоугольника танка

        if direction == 'left':
            new_x = self.rect.x - self.speed
            if new_x >= 0:
                self.rect.x = new_x
        elif direction == 'right':
            new_x = self.rect.x + self.speed
            if new_x + self.rect.width <= 800:
                self.rect.x = new_x
        elif direction == 'up':
            new_y = self.rect.y - self.speed
            if new_y >= 0:
                self.rect.y = new_y
        elif direction == 'down':
            new_y = self.rect.y + self.speed
            if new_y + self.rect.height <= 800:
                self.rect.y = new_y

        self.is_moving = True
        self.direction = direction

    def change_direction(self, direction):
        if direction == 'left':
            self.image = pygame.transform.rotate(self.images[self.image_index], 90)
        elif direction == 'right':
            self.image = pygame.transform.rotate(self.images[self.image_index], -90)
        elif direction == 'down':
            self.image = pygame.transform.rotate(self.images[self.image_index], 180)
        else:  # 'up'
            self.image = self.images[self.image_index]