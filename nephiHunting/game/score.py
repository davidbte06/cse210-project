import arcade
import random


def __init__(self):
    # Set up the game score
    self.score = 0
    self.stage = 1
    self.score_text = None
    self.initial_arrow_count = None
    self.arrow_count = None


def setup(self):
    # Set up the game score and knife count
    self.knife_count = random.randrange(
        self.MIN_ARROW_COUNT, self.MAX_ARROW_COUNT)
    self.initial_knife_count = self.knife_count


def draw_game_over(self):
    """ Draw game over menu across the screen. """

    # Reset the score and stage number
    self.score = 0
    self.stage = 1


def draw_game(self):
    # Display score
    output = f"Press <space> to shoot"
    arcade.draw_text(
        output, self.SCREEN_WIDTH*0.5, self.SCREEN_HEIGHT *
        0.05, (255, 255, 255), 12,
        align="center", anchor_x="center", anchor_y="center",
    )

    # Display score
    output = f"{self.score}"
    arcade.draw_text(
        output, self.SCREEN_WIDTH*0.1, self.SCREEN_HEIGHT *
        0.95, (239, 182, 90), 28,
        align="center", anchor_x="center", anchor_y="center",
    )


def update(self):
    # Check if knife collided with the target.
    target_hit_list = arcade.check_for_collision_with_list(
        self.arrow, self.target_collider_list)
    if not self.arrow.target_hitted and not self.arrow.arrow_hitted:
        for collided_object in target_hit_list:
            # Add 1 to the score when knife successfully hit the target
            self.score += 1
