
import arcade

from game import constants

class Nephi(arcade.Sprite):

    def __init__(self, sprite, scale):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        arcade.Sprite.__init__(self, sprite, scale)

        self.textures = []

        self. facing = 0

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture("nephiHunting/assets/images/nephi_shooting.png")
        self.textures.append(texture)
        texture = arcade.load_texture("nephiHunting/assets/images/nephi_shooting.png", flipped_horizontally=True)
        self.textures.append(texture)
        texture = arcade.load_texture("nephiHunting/assets/images/nephi_shooting_up.png")
        self.textures.append(texture)
        texture = arcade.load_texture("nephiHunting/assets/images/nephi_shooting_up.png", flipped_horizontally=True)
        self.textures.append(texture)

        # By default, face right.
        self.texture = self.textures[0]

    def update(self):
        if self.center_x >= constants.SCREEN_WIDTH: self.center_x = constants.SCREEN_WIDTH
        if self.center_x <= 0: self.center_x = 0

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[1]
            self.facing = 1
        elif self.change_x > 0:
            self.texture = self.textures[0]
            self.facing = 0

    def shooting_up(self):
        if self.facing == 0:
            self.texture = self.textures[2]

        if self.facing == 1:
            self.texture = self.textures[3]
