import pygame
from src.tank import Tank


class HeavyTank(Tank):
    def __init__(self, x, y, player):
        speed = 2
        health = 100
        image_paths = [
            'assets/tanks/heavy/tank1.png',
            'assets/tanks/heavy/tank2.png'
        ]
        super().__init__(x, y, image_paths, health, speed)
        self.load_images()
