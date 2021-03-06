import pyray
import constants
class UpdatePlayer:
    """
    Purpose: create a class which can be utilized to update the player 
        
    """
    def __init__(self, player):
        """
        Purpose: create the base attributes and variables used within the class
        Parameters:
            self - an instance of the attributes of the player class
            player - str used in the main file to help know which player is linked to which variable
        Return:
            none 
        """
        self.y = 0
        self.punching  = False

    def update_player(self, player, env_items, delta, keys, player_color):
        """
        Purpose: update the player based upon actions and keys pressed during the game
        Parameters:
            self - an instance of the attributes of the player class
            player - str containing the player class for player 1 or for player 2
            env items - list of the enviroment items (the platforms)
            delta - the frame time of the game (time)
            keys - a list of the keys that the player can press
            player color - the color of the player
        Return:
            none 
        """

        #left (a and j)
        if pyray.is_key_down(keys[0]) :
            player.position.x -= constants.PLAYER_HOR_SPD * delta
            player.set_direction("left")

        #right (d and l)
        if pyray.is_key_down(keys[1]) :
            player.position.x += constants.PLAYER_HOR_SPD * delta
            player.set_direction("right")
            
        #jump (w and i)
        if pyray.is_key_down(keys[2]) and player.can_jump and not pyray.is_key_down(keys[3]):
            player.speed = -constants.PLAYER_JUMP_SPD
            player.can_jump = False
        
        #sheild (s and k)
        player.set_shield(False)
        if pyray.is_key_down(keys[3]):
            if player.position.y < 590:
                player.position.y = player.position.y + 1
            if player.get_shield_health() > 0:
                player.set_shield(True)
                pyray.draw_rectangle_lines(int(player.position.x)-25, int(player.position.y)-45,50,50,player_color)
                
        #ranged attack (q and u)
        if pyray.is_key_down(keys[4]) and player.can_shoot and not pyray.is_key_down(keys[3]) :
            player.center = player.position.x
            if player.get_direction() == "left":
                player.change = -10
                player.end_x = player.center
                player.center = player.center - constants.LASER_LENGTH
            else:
                player.change = 10
                player.end_x = player.center + constants.LASER_LENGTH
            player.laser_y = player.position.y
            player.can_shoot = False
            

        #meelee attack (e and o)
        self.punching = False
        if pyray.is_key_down(keys[5]) and not pyray.is_key_down(keys[3]):
            if player.get_direction() == "left":
                start_x = int(player.position.x) - 40
            else:
                start_x = int(player.position.x) + 20
            self.punching = True
            pyray.draw_rectangle(start_x, int(player.position.y)-30,20,20,player_color)
        
        #checks to see if the player is currently touching any of the platforms
        #if so the hit obstacle is switched to true and gravity isnt applied
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

        #if a player is not touching a platform they will fall until they do or hit the collision borders
        #it also disables a players ability to jump while falling
        if not hit_obstacle:
            player.position.y += player.speed * delta
            player.speed += constants.G * delta
            player.can_jump = False
        else:
            player.can_jump = True

        
        #draws the lazer(ranged attack) line across the screen from where the player fired it
        if (not player.can_shoot) and player.center > 0 and player.center < constants.SCREEN_WIDTH:
            pyray.draw_line(int(player.center), int(player.laser_y) - 20, int(player.end_x), int(player.laser_y) - 20, player_color)
            player.center = player.center + player.change
            player.end_x = player.end_x + player.change
            player.end_x = player.center + constants.LASER_LENGTH
            
        if player.center <= 0 or player.center >= constants.SCREEN_WIDTH:
            player.center = player.position.x
            player.can_shoot = True

    def get_punching(self):
        """
        Purpose: return a true or false variable if the player is punching or not
        Parameters:
            self - an instance of the attributes of the player class
        Return:
            punching - true or false variable
        """
        return self.punching