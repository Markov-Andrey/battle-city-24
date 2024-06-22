import pygame
import sys
from src.tank import Tank

# Инициализация Pygame
pygame.init()

# Настройка окна
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 50  # Размер блока
GRID_WIDTH, GRID_HEIGHT = 13, 13
MAP_WIDTH, MAP_HEIGHT = GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle City")

# Создание объекта танка
player_tank = Tank(1 * BLOCK_SIZE, 1 * BLOCK_SIZE, BLOCK_SIZE, GRID_WIDTH, GRID_HEIGHT)
all_sprites = pygame.sprite.Group()
all_sprites.add(player_tank)

# Основной игровой цикл
clock = pygame.time.Clock()

# Смещение карты для отображения прокрутки
camera_x, camera_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление игровых объектов
    all_sprites.update()

    # Обновление смещения камеры
    camera_x = player_tank.rect.x - WIDTH // 2
    camera_y = player_tank.rect.y - HEIGHT // 2

    # Ограничение смещения камеры в пределах игровой области
    camera_x = max(0, min(camera_x, MAP_WIDTH - WIDTH))
    camera_y = max(0, min(camera_y, MAP_HEIGHT - HEIGHT))

    # Обновление экрана
    screen.fill((0, 0, 0))  # Закрашивание экрана черным цветом

    # Отрисовка всех спрайтов с учетом смещения камеры
    for sprite in all_sprites:
        screen.blit(sprite.image, (sprite.rect.x - camera_x, sprite.rect.y - camera_y))

    pygame.display.flip()  # Обновление экрана
    clock.tick(60)  # Ограничение FPS до 60
