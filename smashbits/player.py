class Player:

    def __init__(self, position, speed, can_jump):
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
    
    def get_lives(self):
        return self.lives

    def set_lives(self, lives):
        self.lives = lives

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

    def get_shield_health(self):
        return self._shield_health

    def set_shield_health(self, health):
        self._shield_health = health

    def get_shield(self):
        return self.shield
        
    def set_shield(self, shield):
        self.shield = shield
    
    def shield_damage(self, damage):
        self.shield_health = self._shield_health - damage
        print((self.shield_health - damage))

    def get_damage(self):
        return self._damage

    def set_damage(self, damage):
        self._damage = damage

    def add_damage(self, damage):
        self._damage = self._damage + damage

    def get_can_shoot(self):
        return self.can_shoot
