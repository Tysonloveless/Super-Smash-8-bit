#Import statements for use in the main function
from player import Player
from envitem import EnvItem
from update_player import UpdatePlayer
import pyray
import constants
from collision import Collision

#sets the players colors 
player_1_color = constants.RED
player_2_color = constants.BLACK

# Set our game to run at 60 frames-per-second
pyray.set_target_fps(60)

#initializes a window with the specified width, height, and title
pyray.init_window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                  'Super Smash Bits - Raylib')


def main():
    """Runs the main game functions
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        none
    """

    #initializes the audio to prepare it to play music
    pyray.init_audio_device()

    #saves the music file into the variable temp1
    temp1 = pyray.load_sound('test.wav')
    
    #plays the music file temp1
    pyray.play_sound(temp1)

    #takes the collision class and sets it to the variable collision
    collision = Collision()

    #main intialization of players onto the screen
    player = Player(pyray.Vector2(400, 280), 0, False)
    player2 = Player(pyray.Vector2(1200,280), 0, False)
    #main initialization of enviroment objects onto the screen
    env_items = (
        EnvItem(pyray.Rectangle(200, 600, 1200, 200), 1, constants.GRAY),
        EnvItem(pyray.Rectangle(550, 400, 500, 10), 1, constants.GRAY),
        EnvItem(pyray.Rectangle(450, 500, 300, 10), 1, constants.GRAY),
        EnvItem(pyray.Rectangle(850, 500, 300, 10), 1, constants.GRAY),
    )

    #main game loop - will continuously run until the screen is closed or a player loses all lives
    while not pyray.window_should_close() and player.lives > 0 and player2.lives > 0:  # Detect window close button or ESC key
        
        # Update the frames
        delta_time = pyray.get_frame_time()

        #sets the canvas (window) to begin drawing (movement, attack, etc.)
        pyray.begin_drawing()

        #sets the seperate player keys into a their own lists
        keys_1 = [pyray.KEY_A, pyray.KEY_D, pyray.KEY_W, pyray.KEY_S, pyray.KEY_Q, pyray.KEY_E]
        keys_2 = [pyray.KEY_J, pyray.KEY_L, pyray.KEY_I, pyray.KEY_K, pyray.KEY_U, pyray.KEY_O]

        #set the class updateplayer as variables
        game = UpdatePlayer(player)
        game2 = UpdatePlayer(player2)

        #update the players using their location, keys being pressed, etc
        game.update_player(player, env_items, delta_time, keys_1, player_1_color, 1)
        game2.update_player(player2, env_items, delta_time, keys_2, player_2_color, 2)

        #check to see if player is punching
        punching = game.get_punching()
        punching2 = game2.get_punching()

        #check collision of punch attack 
        collision.check_punch_collision(player, player2, punching)
        collision.check_punch_collision(player2, player, punching2)

        #check collision between players
        collision.check_player_collision(player, player2)

        #check to see if there is a lazer currently on screen
        laser_active = not player.get_can_shoot()
        laser_active2 = not player2.get_can_shoot()

        #check collision of the lazer on screen
        collision.check_laser_collision(player, player2, laser_active)
        collision.check_laser_collision(player2, player, laser_active2)

        #check collision with the screen boundries 
        collision.check_bounds(player, player2)

    # player.direction = "right"
        #restarts the game
        if pyray.is_key_pressed(pyray.KEY_R):
            player.position = pyray.Vector2(400, 280)
            player.set_damage(0)
            player.set_lives(3)
            player2.position = pyray.Vector2(1200, 280)
            player2.set_damage(0)
            player2.set_lives(3)

    # Draw
        #sets the background color
        pyray.clear_background(constants.LIGHTGRAY)

        #draw the enviroment items on screen
        for env_item in env_items:
            pyray.draw_rectangle_rec(env_item.rect, env_item.color)

        #set player position values
        player_rect = pyray.Rectangle(
            int(player.position.x) - 20, 
            int(player.position.y) - 40,
            40, 40
        )

        #set player2 position values
        player_rect2 = pyray.Rectangle(
            int(player2.position.x) - 20,
            int(player2.position.y) - 40,
            40, 40)

        #draw the players on screen
        pyray.draw_rectangle_rec(player_rect, player_1_color)
        pyray.draw_rectangle_rec(player_rect2, player_2_color)

        #draw the different texts on screen
        pyray.draw_text((str(player.get_damage()) + ' %'), 400, constants.SCREEN_HEIGHT - 100, constants.FONT_SIZE, player_1_color)
        pyray.draw_text((str(player2.get_damage()) + ' %'), 1200, constants.SCREEN_HEIGHT - 100, constants.FONT_SIZE, player_2_color)
        pyray.draw_text((str(player.get_lives()) + ' lives'), 400, constants.SCREEN_HEIGHT - 50, constants.FONT_SIZE, player_1_color)
        pyray.draw_text((str(player2.get_lives()) + ' lives'), 1200, constants.SCREEN_HEIGHT - 50, constants.FONT_SIZE, player_2_color)

        #end the drawing sequence
        pyray.end_drawing()
        
    # De-Initialization
    pyray.close_audio_device()

    # Close window
    pyray.close_window()


#run the main file
main()