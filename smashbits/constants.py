"""
Purpose: hold some base values used throughout the program such as colors, gravity, jump and movement speed, font information,
        screen information, base damage of attacks, the knockback multiplyer

"""
from raylib.colors import (
    DARKGRAY,
    RED,
    BLACK,
    GRAY,
    LIGHTGRAY,
)
G = 2000
PLAYER_JUMP_SPD = 800.0
PLAYER_HOR_SPD = 200.0

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

FONT_SIZE = 30

LASER_LENGTH = 200

PUNCH_DAMAGE = 20
LASER_DAMAGE = 10
KNOCKBACK = 3