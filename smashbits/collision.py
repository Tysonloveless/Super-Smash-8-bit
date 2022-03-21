import constants
import pyray

class Collision:

    def __init__(self):
        self.filler_space = 0

    def check_collision(player, player2):
        player_position = {'x': int(player.position.x) - 20, 'y':
            int(player.position.y) - 40, 'width': 40, 'height': 40}
        player2_position = {'x': int(player2.position.x) - 20, 'y':
            int(player2.position.y) - 40, 'width':40, 'height': 40}

        if player_position['x'] < player2_position['x'] + player2_position['width'] and player_position['x'] + player_position['width'] > player2_position['x'] and player_position['y'] + player2_position['height'] and player_position['y'] + player_position['height'] > player2_position['y']:
            print('collision detected')

    def check_bounds(player, player2):
        if player.position.x > constants.SCREEN_WIDTH:
            player.position = pyray.Vector2(400, 280)
        if player.position.x < 0:
            player.position = pyray.Vector2(400, 280)
        if player.position.y > constants.SCREEN_HEIGHT:
            player.position = pyray.Vector2(400, 280)
        if player2.position.x > constants.SCREEN_WIDTH:
            player2.position = pyray.Vector2(1200, 280)
        if player2.position.x < 0:
            player2.position = pyray.Vector2(1200, 280)
        if player2.position.y > constants.SCREEN_HEIGHT:
            player2.position = pyray.Vector2(1200, 280)