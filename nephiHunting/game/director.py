import arcade
import random
from game import constants
from game.nephi import Nephi
from game.deer import Deer
from game.arrow import Arrow

from enum import Enum

class GameState(Enum):
    
    MENU = 1
    GAME_RUNNING = 2
    TARGET_DEFEATED = 3
    GAME_OVER = 4

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

        # Initialize the game state
        self.current_state = GameState.MENU

        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 650



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

        #Menu
        self.background_gameover = arcade.load_texture("nephiHunting/assets/images/bg2.png")
        # self.logo = arcade.load_texture("nephiHunting/assets/images/logo.jpg")
        # self.scene.add_sprite("Arrow", self.arrow_sprite)

    def draw_menu(self):
        arcade.draw_texture_rectangle(
            self.SCREEN_WIDTH // 2,
            self.SCREEN_HEIGHT // 2,
            self.SCREEN_WIDTH,
            self.SCREEN_HEIGHT,
            self.background_gameover
        )

        #Draw Logo
        self.logo_list = arcade.SpriteList()
        self.logo = arcade.Sprite("nephiHunting/assets/images/logo.jpg", 0.5)
        self.logo.center_x = self.SCREEN_WIDTH * 0.5
        self.logo.center_y = self.SCREEN_HEIGHT * 0.6
        self.logo_list.append(self.logo)
        self.logo_list.draw()

        output = "Press <ENTER> To Start"
        arcade.draw_text(output, 300, 125, arcade.color.WHITE, 24,) 

    def on_draw(self):
        """Render the screen"""

        arcade.start_render()
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)

        # Draw our sprites
        self.scene.draw()

        # Draw menu
        if self.current_state == GameState.MENU:
            self.draw_menu()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.nephi.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.nephi.change_x = constants.PLAYER_MOVEMENT_SPEED
        if key == arcade.key.Q:
            self.shoot_pressed = True

        # Restart game
        if (
            key == arcade.key.ENTER and 
            (
                self.current_state == GameState.GAME_OVER or
                self.current_state == GameState.MENU
            )   
        ):
            self.setup()
            self.current_state = GameState.GAME_RUNNING


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
