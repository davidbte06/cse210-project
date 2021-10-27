"""
This File tests the information held in different objects of Deer.
"""
import pytest
from game.deer import Deer
from game import constants

deer = Deer(constants.DEER_SPRITE, constants.DEER_SCALING, 500, 600, constants.PLAYER_MOVEMENT_SPEED)
deer2 = Deer(constants.DEER_SPRITE, constants.DEER_SCALING + 1, 400, 1000, constants.PLAYER_MOVEMENT_SPEED + 5)
deer3 = Deer(constants.DEER_SPRITE, constants.DEER_SCALING - 1, 50, 20, -constants.PLAYER_MOVEMENT_SPEED)

def test_position():
    """
    This function tests the Deers' objects position.
    """
    assert deer.center_x == 500
    assert deer.center_y == 600

    assert deer2.center_x == 400
    assert deer2.center_y == 1000

    assert deer3.center_x == 50
    assert deer3.center_y == 20

def test_speed():
    """
    This function tests the Deers' objects speed.
    """
    assert deer.initial_direction == 5
    assert deer2.initial_direction == 10
    assert deer3.initial_direction == -5

def test_scalin():
    """
    This function tests the Deers' objects scale.
    """
    assert deer.scale == 0.16
    assert deer2.scale == 1.16
    assert deer3.scale == -0.84


pytest.main(["-v", "--tb=line", "-rN", "tests/deer_test.py"])
