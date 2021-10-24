""" Game director
    Contains the director class, which has direct control over
    the game loop and event handling.
"""

import arcade
import random

from arcade import scene
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
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        Background (variable): An empty variable.
        Scene (variable): An empty variable.
        Nephi (variable): An empty variable.
        Deer (variable): An empty variable.
        Shoot_pressed (boolean): Whether the key is pressed or not.
        Can_shoot (boolean): Wether the player will be able to shoot or not.
        Shoot_timer (Int): The time between shots.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

        self.background = None
        self.scene = None
        self.nephi = None
        self.deer = None

        self.shoot_pressed = False
        self.can_shoot = True
        self.shoot_timer = 0
        

        # Our physics engine
        self.physics_engine = None

        self.hit_sound = arcade.load_sound(constants.HIT)
        # Initialize the game state
        self.current_state = GameState.MENU

        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 650

        self.score = 0
        self.arrows = 10

    def setup(self):
        """Set up the game here. Call this function to restart the game.
        """
        # Initialize Scene
        self.scene = arcade.Scene()

        # Create the Sprite lists
        self.scene.add_sprite_list("Deer")
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Invisible")
        self.scene.add_sprite_list(constants.LAYER_NAME_ARROWS)

        # Set up deer
        self.deer = Deer(constants.DEER_SPRITE, constants.DEER_SCALING, -50, 450, constants.PLAYER_MOVEMENT_SPEED)
        self.scene.add_sprite("Deer", self.deer)

        self.deer2 = Deer(constants.DEER_SPRITE, constants.DEER_SCALING, 1050, 300, -constants.PLAYER_MOVEMENT_SPEED)
        self.scene.add_sprite("Deer", self.deer2)
        
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

        # Physics engines
        self.physics_engine = arcade.PhysicsEngineSimple(self.nephi, self.scene.get_sprite_list("Walls"))
        self.deer_physics_engine = arcade.PhysicsEngineSimple(self.deer, self.scene.get_sprite_list("Invisible"))
        self.deer2_physics_engine = arcade.PhysicsEngineSimple(self.deer2, self.scene.get_sprite_list("Invisible"))

        # Set up arrow
        self.can_shoot = True
        self.shoot_timer = 0
        self.scene.add_sprite_list(constants.LAYER_NAME_ARROWS)

        #Menu
        self.background_menu = arcade.load_texture("nephiHunting/assets/images/bg.jpg")

        # self.scene.add_sprite("Arrow", self.arrow_sprite)

    def draw_menu(self):
        arcade.draw_texture_rectangle(
            self.SCREEN_WIDTH // 2,
            self.SCREEN_HEIGHT // 2,
            self.SCREEN_WIDTH,
            self.SCREEN_HEIGHT,
            self.background_menu
        )
 
        #Draw Logo
        self.logo_list = arcade.SpriteList()
        self.logo = arcade.Sprite("nephiHunting/assets/images/new_menu_proto.png", 1)
        self.logo.center_x = self.SCREEN_WIDTH * 0.5
        self.logo.center_y = self.SCREEN_HEIGHT * 0.6
        self.logo_list.append(self.logo)
        self.logo_list.draw()

        output = ""
        arcade.draw_text(output, 300, 125, arcade.color.WHITE, 24,) 

    def draw_game_over(self):
        
        arcade.draw_texture_rectangle(
            self.SCREEN_WIDTH // 2, 
            self.SCREEN_HEIGHT // 2,
            self.SCREEN_WIDTH, 
            self.SCREEN_HEIGHT, 
            self.background_menu)
        
        self.gameover_list = arcade.SpriteList()
        self.gameover = arcade.Sprite("nephiHunting/assets/images/gameover.png")
        self.gameover.center_x = self.SCREEN_WIDTH * 0.5
        self.gameover.center_y = self.SCREEN_HEIGHT * 0.6
        self.gameover_list.append(self.gameover)
        self.gameover_list.draw()
        output = ""
        arcade.draw_text(output, 300, 125, arcade.color.BLACK, 24,) 
        


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
        elif self.current_state == GameState.GAME_RUNNING:
            self.on_draw
        else:
            self.draw_game_over()

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18,)

        arrow_text = f"Arrows: {self.arrows}"
        arcade.draw_text(arrow_text, 700, 10, arcade.csscolor.WHITE, 18,)

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
        self.scene.get_sprite_list("Deer").update()
        self.scene.get_sprite_list("Player").update()

        self.deer.move(600, 300, 900, 600)
        self.deer2.move(500, 700, 250, 400)

        self.physics_engine.update()
        self.deer_physics_engine.update()
        self.manage_shoot_interval()

        #updates the scene.
        self.scene.update()
        self.deer2_physics_engine.update()
        
        arrows = arcade.check_for_collision_with_list(self.deer, self.scene.get_sprite_list(constants.LAYER_NAME_ARROWS))


        for arrow in arrows:
            
            # self.deer.center_x = - 50
            self.deer.reset()
            arcade.play_sound(self.hit_sound, 0.05)
            self.score += 1

        arrows = arcade.check_for_collision_with_list(self.deer2, self.scene.get_sprite_list(constants.LAYER_NAME_ARROWS))

        for arrow in arrows:
            
            # self.deer2.center_x = - 50
            self.deer2.reset()
            arcade.play_sound(self.hit_sound, 0.05)
            self.score += 1

        if self.score == 3:
            self.trigger_game_over()

    def manage_shoot_interval(self):
        """Manages the interval between shots"""

        # An instance of Arrow class
        arrow = Arrow()       
        if self.can_shoot:
            if self.shoot_pressed:
                arrow.shoot(self.nephi.center_x, self.nephi.center_y, self.scene)
                self.can_shoot = False
        else:
            self.shoot_timer += 1
            if self.shoot_timer == constants.SHOOT_SPEED:
                self.can_shoot = True
                self.shoot_timer = 0

    def trigger_game_over(self):
        # time.sleep(delay)
        self.current_state = GameState.GAME_OVER
