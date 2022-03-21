import constants
import pyray

class Collision:

    def __init__(self):
        filller = 0

    def check_collision(player, player2):
        if player.position.x < player2.position.x - 1:
            print("collision detected")

    def check_bounds(player, player2):
        if player.position.x > constants.SCREEN_WIDTH:
            player.position = pyray.Vector2(400, 280)
        if player.position.x < 0:
            player.position = pyray.Vector2(400, 280)
        if player.position.y > constants.SCREEN_HEIGHT:
            player.position = pyray.Vector2(400, 280)
        if player2.position.x > constants.SCREEN_WIDTH:
            player2.position = pyray.Vector2(1200, 280)
        if player2.position.x < 0:
            player2.position = pyray.Vector2(1200, 280)
        if player2.position.y > constants.SCREEN_HEIGHT:
            player2.position = pyray.Vector2(1200, 280)
        