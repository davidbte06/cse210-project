import arcade
from game import constants


class Deer(arcade.Sprite):

    def __init__(self, sprite, scale, x, y, direction):
        arcade.Sprite.__init__(self, sprite, scale)
        self.initial_x = x
        self.center_x = self.initial_x

        self.center_y = y

        self.initial_direction = direction
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
        # reference_num = 600
        self.change_x = self.deer_direction

        if self.center_x == b1 and self.bounce == 0:
            self.deer_direction = self.deer_direction * -1
            self.change_x = self.deer_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)
        
        if self.center_x == b2 and self.bounce == 1:
            self.deer_direction = self.deer_direction * -1
            self.change_x = self.deer_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)

        if self.center_x == b3 and self.bounce == 2:
            self.deer_direction = self.deer_direction * -1
            self.change_x = self.deer_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)

        if self.center_x == b4 and self.bounce == 3:
            self.deer_direction = self.deer_direction * -1
            self.change_x = self.deer_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)

        if self.center_x > constants.SCREEN_WIDTH + 50 or self.center_x < constants.SCREEN_WIDTH -1050:
            self.center_x = self.initial_x
            self.deer_direction = self.initial_direction
            self.bounce = 0
            arcade.play_sound(self.jump_sound)

    def reset(self):
        self.center_x = self.initial_x
        self.deer_direction = self.initial_direction
        self.bounce = 0

    def update(self):

        # Figure out if we should face left or right
        if self.deer_direction == 5:
            self.texture = self.textures[0]
        elif self.deer_direction == -5:
            self.texture = self.textures[1]
