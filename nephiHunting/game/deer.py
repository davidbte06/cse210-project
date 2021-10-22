"""This class handles the Actor deer."""
import arcade
from game import constants


class Deer(arcade.Sprite):
    """A visible, moveable thing that participates in the game. The responsibility of Deer is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        center_x (Point): The actor's position in x.
        center_y (Point): The actor's position in y.
        deer_auto_direction (Point): The actor's position in 2d space.
        bounce (Point): The actor's speed and direction.
        jump_sound (Sound): A loaded sound for the deer.
    """

    def __init__(self, sprite, scale):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        arcade.Sprite.__init__(self, sprite, scale)
        self.center_x = -50
        self.center_y = 450
        self.deer_auto_direction = constants.PLAYER_MOVEMENT_SPEED
        self.bounce = 0
        self.jump_sound = arcade.load_sound(constants.JUMP)


    def move(self):
        """Controls the movement of the deer"""
        reference_num = 600
        self.change_x = self.deer_auto_direction

        if self.center_x == reference_num and self.bounce == 0:
            self.deer_auto_direction = -constants.PLAYER_MOVEMENT_SPEED
            self.change_x = self.deer_auto_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)
        
        if self.center_x == reference_num - 300 and self.bounce == 1:
            self.deer_auto_direction = constants.PLAYER_MOVEMENT_SPEED
            self.change_x = self.deer_auto_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)

        if self.center_x == reference_num + 300 and self.bounce == 2:
            self.deer_auto_direction = -constants.PLAYER_MOVEMENT_SPEED
            self.change_x = self.deer_auto_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)

        if self.center_x == reference_num and self.bounce == 3:
            self.deer_auto_direction = constants.PLAYER_MOVEMENT_SPEED
            self.change_x = self.deer_auto_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)

        if self.center_x > constants.SCREEN_WIDTH + 50 and self.bounce == 4:
            self.center_x = -50
            self.bounce = 0
            arcade.play_sound(self.jump_sound)