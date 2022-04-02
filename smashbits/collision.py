import constants
import pyray

class Collision:
    """
    Purpose: to check different collisions between players, boundries, and attacks

    """

    def __init__(self):
        """
        Purpose: create the base attributes and variables used in the class
        Parameters:
            self - an instance of the attributes of the player class 
        Return: 
            none
        """
        self.filler_space = 0
        self.difference = 20

    def check_punch_collision(self, player, player2, punching):
        """
        Purpose: check to see if a meelee attack collides with the opposite player
        Parameters:
            self - an instance of the attributes of the player class 
            player - information about player 1
            player2 - information about player 2
            punching - true or false if the player is punching or not
        Return: 
            none
        """
        #create a dictionary with the players location and size
        player_position = {'x': int(player.position.x) - 20, 'y':
            int(player.position.y) - 40, 'width': 40, 'height': 40}
        player2_position = {'x': int(player2.position.x) - 20, 'y':
            int(player2.position.y) - 40, 'width':40, 'height': 40}

        #gets the fists distance from player depending on which direction they face
        if player._direction == 'left':
            self.difference = -40

        if player._direction == 'right':
            self.difference = 40

        #if the player is punching check to see if it collides with the other player and if so apply that damage
        #to that player and knock them back depending on the damage theyve taken or apply that damage to their sheild if they are currently sheilding
        if punching:
            if player_position['y'] < player2_position['y']  + (player2_position['height'] / 2) and player_position['y'] > player2_position['y']  - (player2_position['height'] / 2):
                if (player_position['x'] + self.difference) > player2_position['x'] - (player2_position['width']/2) and (player_position['x'] + self.difference) < player2_position['x'] + (player2_position['width']/2):
                    if not player2.get_shield():
                        player2.add_damage(constants.PUNCH_DAMAGE)
                        player2.position.x = player2.position.x + ((self.difference / player_position['width']) * player2.get_damage() * constants.KNOCKBACK)
                    else:
                        player2.shield_damage(constants.PUNCH_DAMAGE)

    def check_laser_collision(self, player, player2, laser_active):
        """
        Purpose: to check the collision of a laser with a player
        Parameters:
            self - an instance of the attributes of the player class 
            player - information about player 1
            player2 -  information about player 2
            laser active - a true or false variable if a laser is currently active on screen
        Return: 
            none
        """
        #if a laser is active check to see if it collides with a player
        #if it does collide with a player then apply the damage to that player and knock them back
        #or apply that damge to their sheild if they are currently sheilding
        if laser_active:
            if player.laser_y < player2.position.y  + 20 and player.laser_y > player2.position.y  - 20:
                if player.center < player2.position.x + 20 and player.end_x > player2.position.x - 20:
                    if not player2.get_shield():
                        player2.add_damage(constants.LASER_DAMAGE)
                        player2.position.x = player2.position.x + ((player.change / 10) * player2.get_damage() * constants.KNOCKBACK)
                    else:
                        player2.shield_damage(constants.LASER_DAMAGE)
                    player.can_shoot = True
                
    def check_player_collision(self, player, player2):
        """
        Purpose: to check if two players are colliding into one another in which case they will be pushed
        Parameters:
            self - an instance of the attributes of the player class 
            player - info on player 1
            player2 - info on player 2
        Return: 
            none
        """
        #the distance change if the player is pushed
        change = 1

        #dicitonaries with the players position and size
        player_position = {'x': int(player.position.x) - 20, 'y':
            int(player.position.y) - 40, 'width': 40, 'height': 40}
        player2_position = {'x': int(player2.position.x) - 20, 'y':
            int(player2.position.y) - 40, 'width':40, 'height': 40}
        
        #differnce depending on the direction that the player faces 
        #used for when a player falls onto another player
        if player._direction == 'left':
            self.difference = -4

        if player._direction == 'right':
            self.difference = 4
        
        #if player is being pushed from the right then switch the change variable to negative
        if player.position.x < player2.position.x:
            change = -1
        
        #check if the players are colliding and apply any differences depending on facing directions and the correct push change variable
        x = player_position['width']
        if player_position['x'] < player2_position['x'] + player2_position['width'] and player_position['x'] + player_position['width'] > player2_position['x']:
            if player_position['y'] < player2_position['y'] + player2_position['height'] and player_position['y'] + player_position['height'] > player2_position['y']:
            
                if player._direction != player2._direction:
                    player.position.x = player.position.x - self.difference
                    player2.position.x = player2.position.x + self.difference

                elif player._direction == player2._direction:
                    player.position.x = player2.position.x + player_position['width'] * change
                    player2.position.x = player.position.x - (player2_position['width'] + 1 ) * change
                    

    def check_bounds(self, player, player2):
        """
        Purpose: check collison between a player and the screen bounds
        Parameters:
            self - an instance of the attributes of the player class 
            player - information on player 1
            player2 - information on player 2
        Return: 
            none
        """

        #if player 1 collides with any of the screen bounds then take a life from the player,
        #reset their damage and sheild health, and respawn them
        if player.position.x > constants.SCREEN_WIDTH:
            player.position = pyray.Vector2(400, 280)
            player._damage = 0
            player.lives -= 1
            player.set_shield_health(100)
        if player.position.x < 0:
            player.position = pyray.Vector2(400, 280)
            player._damage = 0
            player.lives -= 1
            player.set_shield_health(100)
        if player.position.y > constants.SCREEN_HEIGHT+50:
            player.position = pyray.Vector2(400, 280)
            player._damage = 0
            player.lives -= 1
            player.set_shield_health(100)

        #if player 2 collides with any of the screen bounds then take a life from the player,
        #reset their damage and sheild health, and respawn them
        if player2.position.x > constants.SCREEN_WIDTH:
            player2.position = pyray.Vector2(1200, 280)
            player2._damage = 0
            player2.lives -= 1
            player2.set_shield_health(100)
        if player2.position.x < 0:
            player2.position = pyray.Vector2(1200, 280)
            player2._damage = 0
            player2.lives -= 1
            player2.set_shield_health(100)
        if player2.position.y > constants.SCREEN_HEIGHT+50:
            player2.position = pyray.Vector2(1200, 280)
            player2._damage = 0
            player2.lives -= 1
            player2.set_shield_health(100)