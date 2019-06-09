from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP, color_pair
from random import randint

# Configuration
HEIGHT = 20
WIDTH = 35
MAX_Y = HEIGHT - 2
MAX_X = WIDTH - 2
TIMEOUT = 100
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
REV_DIR_MAP = {KEY_RIGHT: KEY_LEFT,
               KEY_LEFT: KEY_RIGHT,
               KEY_DOWN: KEY_UP,
               KEY_UP: KEY_DOWN}


class Food:
    def __init__(self, window):
        self.coor = (randint(1, MAX_X), randint(1, MAX_Y))
        self.window = window

    def render(self):
        self.window.addstr(*self.coor, "█", color_pair(3))

    def renew(self):
        self.coor = (randint(1, MAX_X), randint(1, MAX_Y))


class Body:
    def __init__(self, x, y, window):
        self.window = window
        self.body_list = []

        self.last_head_coor = (x, y)
        self.head_x = x
        self.head_y = y

    def render(self):
        self.window.addstr(self.head_x, self.head_y, '█', color_pair(2))  # Head
        for body in self.body_list:
            self.window.addstr(*body, '█', color_pair(1))  # Body

    def add_body(self, x, y):
        self.body_list.append([x, y])


class Snake(Body):
    def __init__(self, x, y, window):
        super().__init__(x, y, window)
        self.direction = KEY_RIGHT
        self.timeout = TIMEOUT
        self.hit_score = 0

        for i in range(SNAKE_LENGTH, 0, -1):
            self.add_body(x - i, y)
        self.add_body(x, y)
