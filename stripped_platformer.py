from math import sqrt

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
global g_evening_out, g_even_out_target
g_evening_out = False

G = 2000
PLAYER_JUMP_SPD = 800.0
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
        self._damage = 0
        self._direction = "left"
    
    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

class EnvItem:

    def __init__(self, rect, blocking, color):
        self.rect = rect
        self.blocking = blocking
        self.color = color

def update_player(player, env_items, delta, keys, player_color):
    #left (a and j)
    if pyray.is_key_down(keys[0]):
        player.position.x -= PLAYER_HOR_SPD * delta
        player.set_direction("left")

    #right (d and l)
    if pyray.is_key_down(keys[1]):
        player.position.x += PLAYER_HOR_SPD * delta
        player.set_direction("right")
        
    #jump (w and i)
    if pyray.is_key_down(keys[2]) and player.can_jump:
        player.speed = -PLAYER_JUMP_SPD
        player.can_jump = False
    
    #s and k (shield)
    if pyray.is_key_down(keys[3]):
        pyray.draw_rectangle_lines(int(player.position.x)-25, int(player.position.y)-45,50,50,player_color)
        
    #q and u (ranged attack)
    if pyray.is_key_down(keys[4]):
        if player.get_direction() == "left":
            end_x = 0
        else:
            end_x = SCREEN_WIDTH
        
        pyray.draw_line(int(player.position.x), int(player.position.y) - 20, end_x, int(player.position.y) - 20, player_color)
        

    #e and o (punch attack)
    if pyray.is_key_down(keys[5]):
        if player.get_direction() == "left":
            start_x = int(player.position.x) - 40
        else:
            start_x = int(player.position.x) + 20
        pyray.draw_rectangle(start_x, int(player.position.y)-30,20,20,player_color)
    
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
player2 = Player(pyray.Vector2(400,280), 0, False)
env_items = (
    #I don't think this one does anything
    #EnvItem(pyray.Rectangle(0, 0, 1000, 400), 0, LIGHTGRAY),
    EnvItem(pyray.Rectangle(0, 400, 1000, 200), 1, GRAY),
    EnvItem(pyray.Rectangle(300, 200, 400, 10), 1, GRAY),
    EnvItem(pyray.Rectangle(250, 300, 100, 10), 1, GRAY),
    EnvItem(pyray.Rectangle(650, 300, 100, 10), 1, GRAY),
)

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

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