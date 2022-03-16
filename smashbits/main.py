from math import sqrt
from player import Player
from envitem import EnvItem
from update_player import update_player
import pyray

from raylib.colors import (
    DARKGRAY,
    RED,
    BLACK,
    GRAY,
    LIGHTGRAY,
)

player_1_color = RED
player_2_color = BLACK

# Initialization
G = 2000
PLAYER_JUMP_SPD = 800.0
PLAYER_HOR_SPD = 200.0

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                  'Super Smash Blocks - Raylib')

# Main intialization
player = Player(pyray.Vector2(400, 280), 0, False)
player2 = Player(pyray.Vector2(600,280), 0, False)
env_items = (
    #I don't think this one does anything
    #EnvItem(pyray.Rectangle(0, 0, 1000, 400), 0, LIGHTGRAY),
    EnvItem(pyray.Rectangle(200, 600, 1200, 200), 1, GRAY),
    EnvItem(pyray.Rectangle(550, 400, 500, 10), 1, GRAY),
    EnvItem(pyray.Rectangle(450, 500, 300, 10), 1, GRAY),
    EnvItem(pyray.Rectangle(850, 500, 300, 10), 1, GRAY),
)


while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    delta_time = pyray.get_frame_time()

    pyray.begin_drawing()
    keys_1 = [pyray.KEY_A, pyray.KEY_D, pyray.KEY_W, pyray.KEY_S, pyray.KEY_Q, pyray.KEY_E]
    keys_2 = [pyray.KEY_J, pyray.KEY_L, pyray.KEY_I, pyray.KEY_K, pyray.KEY_U, pyray.KEY_O]
    update_player(player, env_items, delta_time, keys_1, player_1_color)
    update_player(player2, env_items, delta_time, keys_2, player_2_color)

   # player.direction = "right"
    #restarts the game
    if pyray.is_key_pressed(pyray.KEY_R):
        player.position = pyray.Vector2(400, 280)
        player2.position = pyray.Vector2(400, 280)

    # Draw
    pyray.clear_background(LIGHTGRAY)

    for env_item in env_items:
        pyray.draw_rectangle_rec(env_item.rect, env_item.color)

    player_rect = pyray.Rectangle(
        int(player.position.x) - 20, 
        int(player.position.y) - 40,
        40, 40
    )

    player_rect2 = pyray.Rectangle(
        int(player2.position.x) - 20,
        int(player2.position.y) - 40,
        40, 40)

    pyray.draw_rectangle_rec(player_rect, player_1_color)
    pyray.draw_rectangle_rec(player_rect2, player_2_color)
  #  pyray.draw_rectangle_lines(400,280,10,10,RED)

    pyray.end_drawing()

# De-Initialization
pyray.close_window()  # Close window and OpenGL context

#TO DO
#CAMERA CENTERED SHOW PLATFORM EDGES 
#ATTACKS
#SHIELD
#COLLISION DETECTION FOR OTHER PLAYER
#SCREEN BOUNDS
#SEPARATE INTO CLASSES