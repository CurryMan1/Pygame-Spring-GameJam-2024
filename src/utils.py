import pygame
from os import listdir
from src.tile import Tile


def load_img(path, transparent=False, scale=None, rotate=None):
    img = pygame.image.load(f'assets/img/{path}')

    if scale:
        img = pygame.transform.scale_by(img, scale)

    if rotate:
        img = pygame.transform.rotate(img, rotate)

    if transparent:
        img = img.convert_alpha()
    else:
        img = img.convert()

    return img


def load_imgs(path, transparent=False, scale=None, rotate=None):
    images = []

    for file in listdir(f'assets/img/{path}'):
        img = load_img(f'{path}/{file}', transparent, scale, rotate)
        images.append(img)

    return images


def load_tmx_objects(data, tags: list) -> list[Tile, ...]:
    tiles = []
    for obj in data.objects:
        if obj.tag in tags:
            for x, y, surface in obj.tiles():
                pos = (obj.x, obj.y)
                tiles.append(Tile(pos, surface, obj.tag))
    return tiles
