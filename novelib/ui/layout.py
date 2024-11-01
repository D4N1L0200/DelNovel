from enum import Enum


class Anchor(Enum):
    CENTER = 1

    TOP = 2
    BOTTOM = 3
    LEFT = 4
    RIGHT = 5

    TOPLEFT = 6
    TOPRIGHT = 7
    BOTTOMLEFT = 8
    BOTTOMRIGHT = 9


class Sizing(Enum):
    FILL = 1
    COVER = 2


class Order(Enum):
    VERTICAL = 1
    HORIZONTAL = 2
