class Player:
    """
    Purpose: create a player object and variables
    
    """
    def __init__(self, position, speed, can_jump):
        """
        Purpose: create the base attributes and variables used within the class
        Parameters:
            self - an instance of the attributes of the player class
            position - the players loacation (x, y coordinates)
            speed - the x movement of the player
            can_jump - a true or false if the player is able to jump
        Return: 
            none
        """ 
        self.position = position
        self.center = self.position.x
        self.speed = speed
        self.can_jump = can_jump
        self.can_shoot = True
        self._shield_health = 100
        self._damage = 0
        self._direction = "left"
        self.end_x = 100
        self.change = 10
        self.shield = False
        self.lives = 3
        self.laser_y = 0
    
    def get_lives(self):
        """
        Purpose: return the current lives of the player
        Parameters:
            self - an instance of the attributes of the player class
        Return: 
            amount of lives
        """
        return self.lives

    def set_lives(self, lives):
        """
        Purpose: set the lives to a set value
        Parameters:
            self - an instance of the attributes of the player class
            lives - an int of the number of lives 
        Return: 
            none
        """    
        self.lives = lives

    def get_direction(self):
        """
        Purpose: return the direction that the player is facing
        Parameters:
            self - an instance of the attributes of the player class
        Return: 
            the direction (left, right)
        """   
        return self._direction

    def set_direction(self, direction):
        """
        Purpose: set the direction that the player is facing
        Parameters:
            self - an instance of the attributes of the player class
            direction - a string of the set facing value
        Return: 
            none
        """
        self._direction = direction

    def get_shield_health(self):
        """
        Purpose: gets the current sheilds health 
        Parameters:
            self - an instance of the attributes of the player class
        Return: 
            sheild health (int)
        """   
        return self._shield_health

    def set_shield_health(self, health):
        """
        Purpose: set the sheild health to a value
        Parameters:
            self - an instance of the attributes of the player class
            health - int of the value the shield health is set to
        Return: 
            none
        """   
        self._shield_health = health

    def get_shield(self):
        """
        Purpose: to get a true or false value if the player can sheild
        Parameters:
            self - an instance of the attributes of the player class
        Return: 
            shield as a true or false boolian variable
        """    
        return self.shield
        
    def set_shield(self, shield):
        """
        Purpose: set the players ability to activate their sheild
        Parameters:
            self - an instance of the attributes of the player class
            shield - true or false variable
        Return: 
            none
        """    
        self.shield = shield
    
    def shield_damage(self, damage):
        """
        Purpose: to update the health of the shield if any damage is taken
        Parameters:
            self - an instance of the attributes of the player class
            damage - int of the damage taken from the attack
        Return: 
            none
        """    
        self._shield_health = self._shield_health - damage

    def get_damage(self):
        """
        Purpose: gets the damage done (int)
        Parameters:
            self - an instance of the attributes of the player class
        Return: 
            damage 
        """    
        return self._damage

    def set_damage(self, damage):
        """
        Purpose: set the damage variable to the given value
        Parameters:
            self - an instance of the attributes of the player class
            damage - an int of the new value of damage
        Return: 
            none
        """    
        self._damage = damage

    def add_damage(self, damage):
        """
        Purpose: add damage taken to the damage value
        Parameters:
            self - an instance of the attributes of the player class
            damage - the amount of damage taken
        Return:
            none 
        """    
        self._damage = self._damage + damage

    def get_can_shoot(self):
        """
        Purpose: return a true or false if the player can currently shoot their range attack
        Parameters:
            self - an instance of the attributes of the player class
        Return:
            can shoot - true or false boolian variable
        """   
        return self.can_shoot
