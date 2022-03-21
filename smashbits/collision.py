from pickle import FALSE


class Collision:

    def __init__(self):
        self.hit_obstacle = FALSE

    def check_collision(player, player2):
        player_position = {'x': int(player.position.x) - 20, 'y':
            int(player.position.y) - 40, 'width': 40, 'height': 40}
        player2_position = {'x': int(player2.position.x) - 20, 'y':
            int(player2.position.y) - 40, 'width':40, 'height': 40}

        if player_position['x'] < player2_position['x'] + player2_position['width'] and player_position['x'] + player_position['width'] > player2_position['x'] and player_position['y'] + player2_position['height'] and player_position['y'] + player_position['height'] > player2_position['y']:
            print('collision detected')
