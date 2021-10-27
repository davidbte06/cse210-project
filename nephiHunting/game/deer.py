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

    def __init__(self, sprite, scale, x, y, direction):
        """The class constructor.
        
        Args:
            self (Deer): an instance of Deer.
            sprite (an image): An image from Arcade library.
            scale (float): a number to determine positions.
            x (Point): A point in the window.
            y (Point): A point in the window.
        """
        arcade.Sprite.__init__(self, sprite, scale)
        self.more_speed = 0
        self.initial_x = x
        self.center_x = self.initial_x

        self.center_y = y

        self.initial_direction = direction + self.more_speed
        self.deer_direction = self.initial_direction

        self.bounce = 0
        self.jump_sound = arcade.load_sound(constants.JUMP)

        # Animation
        self.textures = []

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture(constants.DEER_SPRITE)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.DEER_SPRITE, flipped_horizontally=True)
        self.textures.append(texture)

        # By default, face right.
        self.texture = self.textures[0]


    def move(self, b1, b2, b3, b4):
        """Control the movements of deers
        
        Args:
            self (Deer): and instance of deer.
            b1 (Point): A point to change direction.
            b2 (Point): A point to change direction.
            b3 (Point): A point to change direction.
            b4 (Point): A point to change direction.    
            """
        # reference_num = 600
        self.change_x = self.deer_direction

        if self.center_x == b1 and self.bounce == 0:
            self.deer_direction = self.deer_direction * -1
            self.change_x = self.deer_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound, 0.05)
        
        if self.center_x == b2 and self.bounce == 1:
            self.deer_direction = self.deer_direction * -1
            self.change_x = self.deer_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound, 0.05)

        if self.center_x == b3 and self.bounce == 2:
            self.deer_direction = self.deer_direction * -1
            self.change_x = self.deer_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound, 0.05)

        if self.center_x == b4 and self.bounce == 3:
            self.deer_direction = self.deer_direction * -1
            self.change_x = self.deer_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound, 0.05)

        if self.center_x > constants.SCREEN_WIDTH + 50 or self.center_x < constants.SCREEN_WIDTH -1050:
            self.center_x = self.initial_x
            self.deer_direction = self.initial_direction
            self.bounce = 0
            arcade.play_sound(self.jump_sound, 0.05)

    def reset(self):
        """This method resets the game.
        
        Args: 
            self (Deer): An instance of Deer."""
        self.center_x = self.initial_x
        self.deer_direction = self.initial_direction
        self.bounce = 0

    def update(self):
        """ Updates to right or left the direction

        Args: 
            self (Deer): An instance of Deer.
        """
        # Figure out if we should face left or right
        if self.deer_direction == 5:
            self.texture = self.textures[0]
        elif self.deer_direction == -5:
            self.texture = self.textures[1]

    def increase_speed(self):
        """ Increases the speed of the object.
        Args: 
            self (Deer): An instance of Deer."""
        self.more_speed += 100
