from src.tank import Tank


class LightTank(Tank):
    def __init__(self, x, y, player):
        speed = 3
        health = 50
        image_paths = [
            'assets/tanks/light/tank1.png',
            'assets/tanks/light/tank2.png'
        ]
        super().__init__(x, y, image_paths, health, speed)
        self.load_images()
