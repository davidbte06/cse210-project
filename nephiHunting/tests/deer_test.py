import pytest
from game.deer import Deer
from game import constants
from nephiHunting.game import constants

deer = Deer(constants.DEER_SPRITE, constants.DEER_SCALING, 500, 600, constants.PLAYER_MOVEMENT_SPEED)

def test_position():
    assert deer._get_center_x == 500


pytest.main(["-v", "--tb=line", "-rN", "tests/deer_test.py"])
