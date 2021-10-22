
import arcade

from game import constants

class Nephi(arcade.Sprite):

    def update(self):
        if self.center_x >= constants.SCREEN_WIDTH: self.center_x = constants.SCREEN_WIDTH
        if self.center_x <= 0: self.center_x = 0

