import pytest
from game.deer import Deer
from game import constants
from game import constants

deer = Deer("assets/images/new_deer.png", constants.DEER_SCALING, 500, 600, constants.PLAYER_MOVEMENT_SPEED)
deer.jump_sound = "assets/sounds/jump_deer.mp3"


def test_position():
    assert deer._get_center_x == 500


pytest.main(["-v", "--tb=line", "-rN", "tests/deer_test.py"])
