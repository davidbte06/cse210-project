""" This class controls the actor Nephi."""
import arcade

from game import constants

class Nephi(arcade.Sprite):
    """This class creates and controls the Nephi actor.

    Stereotype:
        Information holder

    Attributes:
        textures (List): An empty List.
        facing (Int): An Integer.
    """
    def __init__(self, sprite, scale):
        """The class constructor.

        Args:
            self (Nephi): an instance of Nephi.
            sprite (an image): An image from Arcade library.
            scale (float): a number to determine positions.
        """
        arcade.Sprite.__init__(self, sprite, scale)

        self.textures = []

        self.facing = 0

        # Loads a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture("assets/images/nephi_shooting.png")
        self.textures.append(texture)
        texture = arcade.load_texture("assets/images/nephi_shooting.png", flipped_horizontally=True)
        self.textures.append(texture)
        texture = arcade.load_texture("assets/images/nephi_shooting_up.png")
        self.textures.append(texture)
        texture = arcade.load_texture("assets/images/nephi_shooting_up.png", flipped_horizontally=True)
        self.textures.append(texture)

        # By default, face right.
        self.texture = self.textures[0]

    def update(self):
        """ It updates the position of Nephi depending of the input.
        Args:
            self (Nephi): an instance of Nephi.
            
        """

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
        """It provides the direction of shooting up.
        Args:
            self (Nephi): an instance of Nephi.
                 
        """
        if self.facing == 0:
            self.texture = self.textures[2]

        if self.facing == 1:
            self.texture = self.textures[3]
