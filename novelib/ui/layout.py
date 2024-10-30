from enum import Enum


class Anchor(Enum):
    DEFAULT = 1
    CENTER = 2
    BOT_LEFT = 3


class Sizing(Enum):
    DEFAULT = 1
    FILL = 2
    COVER = 3
    WRAP_CONTENT = 4
