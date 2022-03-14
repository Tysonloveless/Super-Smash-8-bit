import pyray

G = 2000
PLAYER_JUMP_SPD = 800.0
PLAYER_HOR_SPD = 200.0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450


def update_player(player, env_items, delta, keys, player_color):
    #left (a and j)
    if pyray.is_key_down(keys[0]):
        player.position.x -= PLAYER_HOR_SPD * delta
        player.set_direction("left")

    #right (d and l)
    if pyray.is_key_down(keys[1]):
        player.position.x += PLAYER_HOR_SPD * delta
        player.set_direction("right")
        
    #jump (w and i)
    if pyray.is_key_down(keys[2]) and player.can_jump:
        player.speed = -PLAYER_JUMP_SPD
        player.can_jump = False
    
    #s and k (shield)
    if pyray.is_key_down(keys[3]):
        pyray.draw_rectangle_lines(int(player.position.x)-25, int(player.position.y)-45,50,50,player_color)
        
    #q and u (ranged attack)
    if pyray.is_key_down(keys[4]):
        if player.get_direction() == "left":
            end_x = 0
        else:
            end_x = SCREEN_WIDTH
        
        pyray.draw_line(int(player.position.x), int(player.position.y) - 20, end_x, int(player.position.y) - 20, player_color)
        

    #e and o (punch attack)
    if pyray.is_key_down(keys[5]):
        if player.get_direction() == "left":
            start_x = int(player.position.x) - 40
        else:
            start_x = int(player.position.x) + 20
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
        player.speed += G * delta
        player.can_jump = False
    else:
        player.can_jump = True
