from math import sqrt

import pyray
from raylib.colors import (
    DARKGRAY,
    RED,
    BLACK,
    GRAY,
    LIGHTGRAY,
    BLUE
)



# Initialization
global g_evening_out, g_even_out_target
g_evening_out = False

G = 400
PLAYER_JUMP_SPD = 350.0
PLAYER_HOR_SPD = 200.0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                  'raylib [core] example - 2d camera')

class Player:

    def __init__(self, position, speed, can_jump):
        self.position = position
        self.speed = speed
        self.can_jump = can_jump


class EnvItem:

    def __init__(self, rect, blocking, color):
        self.rect = rect
        self.blocking = blocking
        self.color = color

def update_player(player, player2, env_items, delta):
    if pyray.is_key_down(pyray.KEY_LEFT):
        player.position.x -= PLAYER_HOR_SPD * delta
    if pyray.is_key_down(pyray.KEY_RIGHT):
        player.position.x += PLAYER_HOR_SPD * delta
    if pyray.is_key_down(pyray.KEY_UP) and player.can_jump:
        player.speed = -PLAYER_JUMP_SPD
        player.can_jump = False

    if pyray.is_key_down(pyray.KEY_A):
        player2.position.x -= PLAYER_HOR_SPD * delta
    if pyray.is_key_down(pyray.KEY_D):
        player2.position.x += PLAYER_HOR_SPD * delta
    if pyray.is_key_down(pyray.KEY_W) and player.can_jump:
        player2.speed = -PLAYER_JUMP_SPD
        player2.can_jump = False

    hit_obstacle = False
    for ei in env_items:
        p = player.position
        if (
            ei.blocking and
            ei.rect.x <= p.x and
            ei.rect.x + ei.rect.width >= p.x and
            ei.rect.y >= p.y and
            ei.rect.y < p.y + player.speed * delta
        ):
            hit_obstacle = True
            player.speed = 0.0
            p.y = ei.rect.y

    if not hit_obstacle:
        player.position.y += player.speed * delta
        player.speed += G * delta
        player.can_jump = False
    else:
        player.can_jump = True

# Main intialization
player = Player(pyray.Vector2(400, 280), 0, False)
player2 = Player(pyray.Vector2(400, 280), 0, False)
env_items = (
    EnvItem(pyray.Rectangle(0, 0, 1000, 400), 0, LIGHTGRAY),
    EnvItem(pyray.Rectangle(0, 400, 1000, 200), 1, GRAY),
    EnvItem(pyray.Rectangle(300, 200, 400, 10), 1, GRAY),
    EnvItem(pyray.Rectangle(250, 300, 100, 10), 1, GRAY),
    EnvItem(pyray.Rectangle(650, 300, 100, 10), 1, GRAY),
)

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    delta_time = pyray.get_frame_time()

    update_player(player, player2, env_items, delta_time)


    if pyray.is_key_pressed(pyray.KEY_R):
        player.position = pyray.Vector2(400, 280)
        player2.position = pyray.Vector2(200, 280)

    # Draw
    pyray.begin_drawing()
    pyray.clear_background(LIGHTGRAY)


    for env_item in env_items:
        pyray.draw_rectangle_rec(env_item.rect, env_item.color)

    player_rect = pyray.Rectangle(
        int(player.position.x) - 20,
        int(player.position.y) - 40,
        40, 40
    )

    player_rect2 = pyray.Rectangle(
        int(player2.position.x) - 80,
        int(player2.position.y) - 40,
        40, 40
    )
    pyray.draw_rectangle_rec(player_rect, RED)
    pyray.draw_rectangle_rec(player_rect2, BLUE)

    pyray.end_mode_2d()

    pyray.end_drawing()

# De-Initialization
pyray.close_window()  # Close window and OpenGL context