from player import Player
from envitem import EnvItem
from update_player import UpdatePlayer
import pyray
import constants
from collision import Collision

player_1_color = constants.RED
player_2_color = constants.BLACK


pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

pyray.init_window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                  'Super Smash Blocks - Raylib')

def main():
    collision = Collision()
    # Main intialization
    player = Player(pyray.Vector2(400, 280), 0, False)
    player2 = Player(pyray.Vector2(1200,280), 0, False)
    env_items = (
        #I don't think this one does anything
        #EnvItem(pyray.Rectangle(0, 0, 1000, 400), 0, LIGHTGRAY),
        EnvItem(pyray.Rectangle(200, 600, 1200, 200), 1, constants.GRAY),
        EnvItem(pyray.Rectangle(550, 400, 500, 10), 1, constants.GRAY),
        EnvItem(pyray.Rectangle(450, 500, 300, 10), 1, constants.GRAY),
        EnvItem(pyray.Rectangle(850, 500, 300, 10), 1, constants.GRAY),
    )

    while not pyray.window_should_close():  # Detect window close button or ESC key
        # Update
        delta_time = pyray.get_frame_time()

        pyray.begin_drawing()
        keys_1 = [pyray.KEY_A, pyray.KEY_D, pyray.KEY_W, pyray.KEY_S, pyray.KEY_Q, pyray.KEY_E]
        keys_2 = [pyray.KEY_J, pyray.KEY_L, pyray.KEY_I, pyray.KEY_K, pyray.KEY_U, pyray.KEY_O]

        game = UpdatePlayer(player)
        game2 = UpdatePlayer(player2)
        game.update_player(player, env_items, delta_time, keys_1, player_1_color)
        game2.update_player(player2, env_items, delta_time, keys_2, player_2_color)
        punching = game.get_punching()
        punching2 = game2.get_punching()
        collision.check_punch_collision(player, player2, punching)
        collision.check_punch_collision(player2, player, punching2)

        laser_active = not player.get_can_shoot()
        laser_active2 = not player2.get_can_shoot()
        collision.check_laser_collision(player, player2, laser_active)
        collision.check_laser_collision(player2, player, laser_active2)

        collision.check_bounds(player, player2)
    # player.direction = "right"
        #restarts the game
        if pyray.is_key_pressed(pyray.KEY_R):
            player.position = pyray.Vector2(400, 280)
            player.set_damage(0)
            player2.position = pyray.Vector2(1200, 280)
            player2.set_damage(0)

    # Draw
        pyray.clear_background(constants.LIGHTGRAY)

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
        pyray.draw_text((str(player.get_damage()) + ' %'), 400, constants.SCREEN_HEIGHT - 100, constants.FONT_SIZE, player_1_color)
        pyray.draw_text((str(player2.get_damage()) + ' %'), 1200, constants.SCREEN_HEIGHT - 100, constants.FONT_SIZE, player_2_color)
    #  pyray.draw_rectangle_lines(400,280,10,10,RED)

        pyray.end_drawing()

    # De-Initialization
    pyray.close_window()  # Close window and OpenGL context


main()

#####    TO DO    #####
#ATTACKS - damage, ranged attack bug when moving/ facing right (FIXED BUG)
#SHIELD - negate damage, timer/ limit movement
#COLLISION DETECTION FOR OTHER PLAYER
#SCREEN BOUNDS - edge death detection     - not an immediate priority (DONE)
#SEPARATE INTO CLASSES (MOSTLY DONE)
#The check_laser_collision uses the y position of the character, not the laser
#The shield cannot die
#Cooldown on laser might be nice