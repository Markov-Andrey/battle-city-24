import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, block_size, grid_width, grid_height):
        super().__init__()
        # Загрузка изображений для анимации
        self.images = [
            pygame.transform.scale(pygame.image.load('assets/tanks/basic/tank1.png').convert_alpha(), (block_size, block_size)),
            pygame.transform.scale(pygame.image.load('assets/tanks/basic/tank2.png').convert_alpha(), (block_size, block_size))
        ]
        self.image_index = 0  # Индекс текущего изображения анимации
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = block_size // 10  # Уменьшение скорости для плавного движения
        self.block_size = block_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.direction = 'up'  # Начальное направление танка
        self.is_moving = False  # Флаг, указывающий на движение танка

    def update(self):
        keys = pygame.key.get_pressed()

        # Проверка наличия нажатия клавиш перемещения
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            self.is_moving = True
        else:
            self.is_moving = False

        # Переключение между изображениями для создания эффекта анимации, только если танк двигается
        if self.is_moving:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]

        # Управление движением танка
        if keys[pygame.K_LEFT]:
            self.direction = 'left'
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.direction = 'right'
            self.rect.x += self.speed
        elif keys[pygame.K_UP]:
            self.direction = 'up'
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.direction = 'down'
            self.rect.y += self.speed

        # Поворот изображения в зависимости от направления
        if self.direction == 'left':
            self.image = pygame.transform.rotate(self.images[self.image_index], 90)
        elif self.direction == 'right':
            self.image = pygame.transform.rotate(self.images[self.image_index], -90)
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(self.images[self.image_index], 180)

        # Ограничение движений танка в пределах карты (блоков)
        self.rect.x = max(0, min(self.rect.x, (self.grid_width - 1) * self.block_size))
        self.rect.y = max(0, min(self.rect.y, (self.grid_height - 1) * self.block_size))
