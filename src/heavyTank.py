import pygame
from src.tank import Tank  # Подключаем базовый класс Tank
import random

class EnemyTank(Tank):
    def __init__(self, x, y):
        image_paths = ['assets/tanks/heavy/tank1.png', 'assets/tanks/heavy/tank2.png']  # Пример пути к изображению
        super().__init__(x, y, image_paths, health=200, speed=3)
        self.is_player = False  # Устанавливаем флаг, что танк не является игроком
        self.current_direction = 'up'  # Начальное направление движения

    def update(self):
        # Добавьте специфическую логику для поведения вражеского танка
        self.move_in_current_direction()
        self.update_animation()

    def move_in_current_direction(self):
        # Метод для движения вражеского танка в текущем направлении
        if self.can_move_in_direction(self.current_direction):
            self.move(self.current_direction)
        else:
            # Если не можем двигаться в текущем направлении, выбираем новое направление
            self.choose_new_direction()

    def can_move_in_direction(self, direction):
        # Метод для проверки возможности движения в заданном направлении
        if direction == 'left':
            new_x = self.rect.x - self.speed
            return new_x >= 0
        elif direction == 'right':
            new_x = self.rect.x + self.speed
            return new_x + self.rect.width <= self.grid_width * self.block_size
        elif direction == 'up':
            new_y = self.rect.y - self.speed
            return new_y >= 0
        elif direction == 'down':
            new_y = self.rect.y + self.speed
            return new_y + self.rect.height <= self.grid_height * self.block_size
        return False

    def choose_new_direction(self):
        # Метод для выбора нового направления движения, когда текущее направление заблокировано
        directions = ['left', 'right', 'up', 'down']
        directions.remove(self.current_direction)  # Удаляем текущее направление из списка возможных
        random.shuffle(directions)  # Перемешиваем оставшиеся направления случайным образом
        for direction in directions:
            if self.can_move_in_direction(direction):
                self.current_direction = direction
                return
        # Если не найдено подходящего направления, танк останется на месте или будет поворачиваться без движения

    def update_animation(self):
        # Метод для обновления анимации движения танка
        if self.is_moving:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.change_direction(self.current_direction)
        else:
            self.image_index = 0
            self.image = self.images[self.image_index]

        # Поворачиваем изображение в соответствии с текущим направлением
        self.image = self.images[self.image_index]
        self.change_direction(self.current_direction)

