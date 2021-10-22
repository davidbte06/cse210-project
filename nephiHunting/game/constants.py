"""Creates the constants of the game."""

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Nephi Hunting"

# Constants used to scale our sprites from their original size
NEPHI_SCALING = 1
CHARACTER_SCALING = 1
DEER_SCALING = 0.16
TILE_SCALING = 0.5
COIN_SCALING = 0.5
ARROW_SCALING = 0.1

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5

# Arrow constants
RIGHT_FACING = 0
LEFT_FACING = 1
ARROW_SPEED = 12
LAYER_NAME_ARROWS = "Arrows"
SHOOT_SPEED = 10

# Image Sources
NEPHI_SPRITE = "nephiHunting/assets/images/nephi_shooting.png"
DEER_SPRITE = "nephiHunting/assets/images/new_deer.png"
BACKGROUND = "nephiHunting/assets/images/desert_background.png"
ARROW = "nephiHunting/assets/images/pixel_arrow.png"

#Sounds
ARROW_SOUND = "nephiHunting/assets/sounds/arrow-whizz.wav"
JUMP = "nephiHunting/assets/sounds/jump_deer.mp3"
COIN = ":resources:sounds/coin1.wav"
GRASS = ":resources:images/tiles/grassMid.png"
HIT = "nephiHunting/assets/sounds/mixkit-player-jumping-in-a-video-game-2043.wav"