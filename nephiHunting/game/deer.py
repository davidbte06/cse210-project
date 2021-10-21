import arcade
from game import constants


class Deer(arcade.Sprite):

    def __init__(self, sprite, scale):
        arcade.Sprite.__init__(self, sprite, scale)
        self.center_x = -50
        self.center_y = 450
        self.deer_auto_direction = constants.PLAYER_MOVEMENT_SPEED
        self.bounce = 0
        self.jump_sound = arcade.load_sound(constants.JUMP)


    def move(self):
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

