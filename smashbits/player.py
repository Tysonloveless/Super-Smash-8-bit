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
    
    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

    def get_shield_health(self):
        return self._shield_health

    def  set_shield_health(self, health):
        self._shield_health = health