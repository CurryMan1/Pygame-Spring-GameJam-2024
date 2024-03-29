WIDTH, HEIGHT = WIN_SIZE = 1920, 1080

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (18, 18, 19)
BLUE = (111, 111, 255)
GOLD = (164, 158, 23)

GRAVITY = 100


BLOCK_PROPERTIES = {
    #(accel, friction, max_speed)
    'stone': (10.0, 7.5, 2.0),
    'wood': (10.0, 7.5, 2.0),
    'ice': (5.0, 1.0, 3.5),
    'water': (0, 0, 0), #TODO
    'lava': (0, 0, 0) #TODO
}
