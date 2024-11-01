from enum import Enum


class Anchor(Enum):
    NONE = 1
    CENTER = 2
    
    TOP = 3
    BOTTOM = 4
    LEFT = 5
    RIGHT = 6
    
    TOPLEFT = 7
    TOPRIGHT = 8
    BOTTOMLEFT = 9
    BOTTOMRIGHT = 10


class Sizing(Enum):
    FILL = 1
    COVER = 2


class Order(Enum):
    VERTICAL = 1
    HORIZONTAL = 2
