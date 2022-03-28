import pyray
import constants
class UpdatePlayer:
    def __init__(self, player):
        self.y = 0
        self.punching  = False

    def update_player(self, player, env_items, delta, keys, player_color):

        #left (a and j)
        if pyray.is_key_down(keys[0]) and not pyray.is_key_down(keys[3]):
            player.position.x -= constants.PLAYER_HOR_SPD * delta
            player.set_direction("left")

        #right (d and l)
        if pyray.is_key_down(keys[1]) and not pyray.is_key_down(keys[3]):
            player.position.x += constants.PLAYER_HOR_SPD * delta
            player.set_direction("right")
            
        #jump (w and i)
        if pyray.is_key_down(keys[2]) and player.can_jump:
            player.speed = -constants.PLAYER_JUMP_SPD
            player.can_jump = False
        
        #s and k (shield)
        player.set_shield(False)
        if pyray.is_key_down(keys[3]) and player.get_shield_health() > 0:
            if player.position.y < 590:
                player.position.y = player.position.y + 1
            player.set_shield(True)
            pyray.draw_rectangle_lines(int(player.position.x)-25, int(player.position.y)-45,50,50,player_color)
            constants.PLAYER_HOR_SPD = 0
            
        #q and u (ranged attack)

        #currently trying to have the laser fly out instead of always being centered on the player
        #if a bolt is flying, hopefully the player can't spawn another laser
        if pyray.is_key_down(keys[4]) and player.can_shoot:
            player.center = player.position.x
            if player.get_direction() == "left":
                player.change = -10
                player.end_x = player.center
                player.center = player.center - constants.LASER_LENGTH
                #end_x = 0
            else:
                player.change = 10
                player.end_x = player.center + constants.LASER_LENGTH
                #end_x = constants.SCREEN_WIDTH
            player.laser_y = player.position.y
            player.can_shoot = False
            

        #e and o (punch attack)
        self.punching = False
        if pyray.is_key_down(keys[5]) and player.get_shield_health() > 0:
            if player.get_direction() == "left":
                start_x = int(player.position.x) - 40
            else:
                start_x = int(player.position.x) + 20
            self.punching = True
            pyray.draw_rectangle(start_x, int(player.position.y)-30,20,20,player_color)
        
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

        if not hit_obstacle:
            player.position.y += player.speed * delta
            player.speed += constants.G * delta
            player.can_jump = False
        else:
            player.can_jump = True

        

        if (not player.can_shoot) and player.center > 0 and player.center < constants.SCREEN_WIDTH:
            pyray.draw_line(int(player.center), int(player.laser_y) - 20, int(player.end_x), int(player.laser_y) - 20, player_color)
            player.center = player.center + player.change
            player.end_x = player.end_x + player.change
            player.end_x = player.center + constants.LASER_LENGTH
            

        if player.center <= 0 or player.center >= constants.SCREEN_WIDTH:
            player.center = player.position.x
            player.can_shoot = True

    def get_punching(self):
        return self.punching

    def get_laser_y(self):
        return 20