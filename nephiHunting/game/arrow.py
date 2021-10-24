"""This class handles the actor Arrow"""

import arcade
from game import constants


class Arrow(arcade.Sprite):
    """A subclass of Sprite. The responsibility of 
    this class of objects is to control the arrows in the game.
    
    Stereotype:
        Information Holder

    Attributes:
        shoot_sound (variable): An with sound in it.
        
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        super().__init__(constants.ARROW, constants.ARROW_SCALING)
        self.shoot_sound = arcade.load_sound(constants.ARROW_SOUND)       

    def shoot(self, center_x, center_y, scene): 
        """The method shoot, creates the arrow, sets the arrow in a specific point,
            adds the sound and shoots the arrow.
        """       
        self.center_x = center_x
        self.center_y = center_y
        self.change_y = constants.ARROW_SPEED
        arcade.play_sound(self.shoot_sound, 0.05)
        scene.add_sprite(constants.LAYER_NAME_ARROWS, self)

