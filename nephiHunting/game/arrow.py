
import arcade
from game import constants

class Arrow(arcade.Sprite):

    def __init__(self, sprite, scale, x, y):
        arcade.Sprite.__init__(self, sprite, scale)
        self.change_y = constants.ARROW_SPEED
        self.center_x = x
        self.center_y = y
        self.shoot_sound = arcade.load_sound(constants.ARROW_SOUND)
        arcade.play_sound(self.shoot_sound)
