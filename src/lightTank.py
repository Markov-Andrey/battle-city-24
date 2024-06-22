import pygame

from src.tank import Tank

class LightTank(Tank):
    def __init__(self, x, y):
        image_paths = ['assets/tanks/light/tank1.png', 'assets/tanks/light/tank2.png']  # Пример пути к изображению
        super().__init__(x, y, image_paths, health=100, speed=5)
        self.is_player = True  # Устанавливаем флаг, что танк является игроком

    def update(self):
        keys = pygame.key.get_pressed()

        # Сохранение предыдущей позиции
        prev_x, prev_y = self.rect.x, self.rect.y

        # Проверка наличия нажатия клавиш перемещения
        if keys[pygame.K_LEFT]:
            self.move('left')
        elif keys[pygame.K_RIGHT]:
            self.move('right')
        elif keys[pygame.K_UP]:
            self.move('up')
        elif keys[pygame.K_DOWN]:
            self.move('down')

        # Переключение между изображениями для создания эффекта анимации
        if any(keys):
            self.is_moving = True
            self.image_index = (self.image_index + 1) % len(self.images)
            self.change_direction(self.direction)
        else:
            self.is_moving = False
