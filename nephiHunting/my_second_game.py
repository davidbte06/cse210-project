import arcade
import nephiHunting.arcade_constants as CONS
import random


class MyGame(arcade.Window):
    """Main aplication class.
    """
    def __init__(self):
        """Arguments of my game. Setting up the window.
        """
        super().__init__(CONS.SCREEN_WIDTH, CONS.SCREEN_HEIGHT, CONS.SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.deer_sprite = None

        # Separate variable that holds the player sprite
        self.arrow_sprite = None
        self.shoot_pressed = False
        self.can_shoot = False
        self.shoot_timer = 0
        self.shoot_sound = arcade.load_sound("nephiHunting/assets/sounds/arrow-whizz.wav")

        # Our physics engine
        self.physics_engine = None

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound("nephiHunting/assets/sounds/jump_deer.mp3")

        # To move the deer
        self.bounce = 0

        self.deer_auto_direction = CONS.PLAYER_MOVEMENT_SPEED

        # Background image
        self.background = None

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
        image_source = "nephiHunting/assets/images/new_deer.png"
        self.deer_sprite = arcade.Sprite(image_source, CONS.DEER_SCALING)
        self.deer_sprite.center_x = -50
        self.deer_sprite.center_y = 500


        self.scene.add_sprite("Deer", self.deer_sprite)
        

        # Set up character
        image_source = "nephiHunting/assets/images/my_avatar.png"
        self.player_sprite = arcade.Sprite(image_source, CONS.CHARACTER_SCALING)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 64


        self.scene.add_sprite("Player", self.player_sprite)

        # # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", CONS.TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        # Load the background image.
        self.background = arcade.load_texture("nephiHunting/assets/images/desert_background.png")

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("Walls"))
        self.deer_physics_engine = arcade.PhysicsEngineSimple(self.deer_sprite, self.scene.get_sprite_list("Invisible"))

        # Set up arrow
        self.can_shoot = True
        self.shoot_timer = 0
        self.scene.add_sprite_list(CONS.LAYER_NAME_ARROWS)


        self.scene.add_sprite("Arrow", self.arrow_sprite)

    def on_draw(self):
        """Render the screen"""

        arcade.start_render()
        # Code to draw the screen goes here.
        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0, CONS.SCREEN_WIDTH, CONS.SCREEN_HEIGHT, self.background)

        # Draw our sprites
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -CONS.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = CONS.PLAYER_MOVEMENT_SPEED
        if key == arcade.key.Q:
            self.shoot_pressed = True


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
        if key == arcade.key.Q:
            self.shoot_pressed = False

    def move(self):
        reference_num = 600

        self.deer_sprite.change_x = self.deer_auto_direction

        if self.deer_sprite.center_x == reference_num and self.bounce == 0:
            self.deer_auto_direction = -CONS.PLAYER_MOVEMENT_SPEED
            self.deer_sprite.change_x = self.deer_auto_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)
        
        if self.deer_sprite.center_x == reference_num - 300 and self.bounce == 1:
            self.deer_auto_direction = CONS.PLAYER_MOVEMENT_SPEED
            self.deer_sprite.change_x = self.deer_auto_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)

        if self.deer_sprite.center_x == reference_num + 300 and self.bounce == 2:
            self.deer_auto_direction = -CONS.PLAYER_MOVEMENT_SPEED
            self.deer_sprite.change_x = self.deer_auto_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)

        if self.deer_sprite.center_x == reference_num and self.bounce == 3:
            self.deer_auto_direction = CONS.PLAYER_MOVEMENT_SPEED
            self.deer_sprite.change_x = self.deer_auto_direction
            self.bounce += 1
            arcade.play_sound(self.jump_sound)

        if self.deer_sprite.center_x > CONS.SCREEN_WIDTH + 50 and self.bounce == 4:
            self.deer_sprite.center_x = -50
            self.bounce = 0
            arcade.play_sound(self.jump_sound)

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.move()
        self.physics_engine.update()
        self.deer_physics_engine.update()
        
        # Determines if player shoot
        if self.can_shoot:
            if self.shoot_pressed:
                arcade.play_sound(self.shoot_sound)
                arrow = arcade.Sprite(
                    "nephiHunting/assets/images/pixel_arrow.png",
                    CONS.SPRITE_SCALING_LASER,
                )
                
                arrow.change_y = CONS.BULLET_SPEED


                arrow.center_x = self.player_sprite.center_x
                arrow.center_y = self.player_sprite.center_y

                self.scene.add_sprite(CONS.LAYER_NAME_ARROWS, arrow)

                self.can_shoot = False
        else:
            self.shoot_timer += 1
            if self.shoot_timer == CONS.SHOOT_SPEED:
                self.can_shoot = True
                self.shoot_timer = 0

        self.scene.update(
            [CONS.LAYER_NAME_ARROWS]
        )
