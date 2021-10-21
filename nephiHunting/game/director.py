import arcade
import random
from game import constants
from game.nephi import Nephi
from game.deer import Deer
from game.arrow import Arrow


class Director(arcade.Window):
    """Main aplication class.
    """
    def __init__(self):
        """Arguments of my game. Setting up the window.
        """
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

        self.background = None
        self.scene = None
        self.nephi = None
        self.deer = None

        self.arrow_sprite = None
        self.shoot_pressed = False
        self.can_shoot = False
        self.shoot_timer = 0

        # Our physics engine
        self.physics_engine = None


    def setup(self):
        """Set up the game here. Call this function to restart the game.
        """
        # Initialize Scene
        self.scene = arcade.Scene()

        # Create the Sprite lists
        self.scene.add_sprite_list("Deer")
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Invisible")
        self.scene.add_sprite_list("Arrow")

        # Set up deer
        self.deer = Deer(constants.DEER_SPRITE, constants.DEER_SCALING)
        self.scene.add_sprite("Deer", self.deer)
        
        # Set up character
        self.nephi = Nephi(constants.NEPHI_SPRITE, constants.NEPHI_SCALING)        
        self.nephi.center_x = 500
        self.nephi.center_y = 32
        self.scene.add_sprite("Player", self.nephi)

        # # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(constants.GRASS, constants.TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        # Load the background image.
        self.background = arcade.load_texture(constants.BACKGROUND)

        self.physics_engine = arcade.PhysicsEngineSimple(self.nephi, self.scene.get_sprite_list("Walls"))
        self.deer_physics_engine = arcade.PhysicsEngineSimple(self.deer, self.scene.get_sprite_list("Invisible"))

        # Set up arrow
        self.can_shoot = True
        self.shoot_timer = 0
        self.scene.add_sprite_list(constants.LAYER_NAME_ARROWS)


        # self.scene.add_sprite("Arrow", self.arrow_sprite)

    def on_draw(self):
        """Render the screen"""

        arcade.start_render()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)

        # Draw our sprites
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.nephi.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.nephi.change_x = constants.PLAYER_MOVEMENT_SPEED
        if key == arcade.key.Q:
            self.shoot_pressed = True


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.nephi.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.nephi.change_x = 0
        if key == arcade.key.Q:
            self.shoot_pressed = False


    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.deer.move()
        self.physics_engine.update()
        self.deer_physics_engine.update()
        
        # Determines if player shoot
        if self.can_shoot:
            if self.shoot_pressed:
                arrow = Arrow(constants.ARROW,constants.SPRITE_SCALING_LASER, self.nephi.center_x, self.nephi.center_y)
                self.scene.add_sprite(constants.LAYER_NAME_ARROWS, arrow)
                self.can_shoot = False
        else:
            self.shoot_timer += 1
            if self.shoot_timer == constants.SHOOT_SPEED:
                self.can_shoot = True
                self.shoot_timer = 0

        self.scene.update([constants.LAYER_NAME_ARROWS])
