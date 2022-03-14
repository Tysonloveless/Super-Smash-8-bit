class Player:

    def __init__(self, position, speed, can_jump):
        self.position = position
        self.speed = speed
        self.can_jump = can_jump
        self._damage = 0
        self._direction = "left"
    
    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction