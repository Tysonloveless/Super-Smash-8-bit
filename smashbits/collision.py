import constants
import pyray

class Collision:

    def __init__(self):
        self.filler_space = 0
        self.difference = 20

    def check_punch_collision(self, player, player2, punching):
        player_position = {'x': int(player.position.x) - 20, 'y':
            int(player.position.y) - 40, 'width': 40, 'height': 40}
        player2_position = {'x': int(player2.position.x) - 20, 'y':
            int(player2.position.y) - 40, 'width':40, 'height': 40}

        '''  if player_position['x'] < player2_position['x'] + player2_position['width']:
            print('collision detected1')
        if player_position['x'] + player_position['width'] > player2_position['x']:
            print("collision detected2")
        if  player2_position['y'] + player2_position['height'] > player_position['y']:
            print("collision detected3")
        if player_position['y'] + player_position['height'] > player2_position['y']:
            print("collision detected4")  '''
        if player._direction == 'left':
            self.difference = -40

        if player._direction == 'right':
            self.difference = 40

        if punching:
            if player_position['y'] < player2_position['y']  + (player2_position['height'] / 2) and player_position['y'] > player2_position['y']  - (player2_position['height'] / 2):
                if (player_position['x'] + self.difference) > player2_position['x'] - (player2_position['width']/2) and (player_position['x'] + self.difference) < player2_position['x'] + (player2_position['width']/2):
                    if not player2.get_shield():
                        player2.add_damage(constants.PUNCH_DAMAGE)
                        player2.position.x = player2.position.x + ((self.difference / player_position['width']) * player2.get_damage() * constants.KNOCKBACK)
                    else:
                        print('punch shield')
                        player2.shield_damage(constants.PUNCH_DAMAGE)
                        print(player2.get_shield_health())

    def check_laser_collision(self, player, player2, laser_active):

        if laser_active:
            if player.position.y < player2.position.y  + 20 and player.position.y > player2.position.y  - 20:
                if player.center < player2.position.x + 20 and player.end_x > player2.position.x - 20:
                    if not player2.get_shield():
                        player2.add_damage(constants.LASER_DAMAGE)
                        player2.position.x = player2.position.x + ((player.change / 10) * player2.get_damage() * constants.KNOCKBACK)
                    else:
                        print('laser shield')
                        player2.shield_damage(constants.LASER_DAMAGE)
                    player.can_shoot = True
                
        

    def check_bounds(self, player, player2):
        if player.position.x > constants.SCREEN_WIDTH:
            player.position = pyray.Vector2(400, 280)
            player._damage = 0
        if player.position.x < 0:
            player.position = pyray.Vector2(400, 280)
            player._damage = 0
        if player.position.y > constants.SCREEN_HEIGHT:
            player.position = pyray.Vector2(400, 280)
            player._damage = 0
        if player2.position.x > constants.SCREEN_WIDTH:
            player2.position = pyray.Vector2(1200, 280)
            player2._damage = 0
        if player2.position.x < 0:
            player2.position = pyray.Vector2(1200, 280)
            player2._damage = 0
        if player2.position.y > constants.SCREEN_HEIGHT:
            player2.position = pyray.Vector2(1200, 280)
            player2._damage = 0