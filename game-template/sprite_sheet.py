from . import pg_image, pg_transform
from engine import *
from engine.entity import Entity

class SpriteSheet:
    def __init__(self, image_path, sprites):
        self.image = pg_image.load(image_path)
        self.sprites = sprites

    def sprite(self, tile_id, size=None):
        image = self.image.subsurface(self.sprites[tile_id])
        if size is not None:
            image = pg_transform.scale(image, size)

        return image

    def animation_sprites(self, tile_id, size=None):
        images = []
        for rect in self.sprites[tile_id]:
            image = self.image.subsurface(rect)
            if size is not None:
                image = pg_transform.scale(image, size)

            images.append(image)
        return images

# Beeto (enemy) class
sprites = SpriteSheet('assets/images/beeto.png', {
    'idle': (2, 2, 26, 16),
    'walk': [(2 + 28 * i, 2, 26, 16) for i in range(4)],
    'flip': (2, 20, 26, 16),
})

animations = {
    'walk': Animation(sprites.animation_sprites('walk'), 1, repeat=True),
}

