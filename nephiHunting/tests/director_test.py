import pytest
import arcade
from game.director import Director
from game.director import GameState
from game.deer import Deer
from game import constants


@pytest.fixture()
def director_preset():    
    """
    """
    director = Director()
    director.deer = Deer(constants.DEER_SPRITE, constants.DEER_SCALING, -50, 450, constants.PLAYER_MOVEMENT_SPEED)
    director.deer2 = Deer(constants.DEER_SPRITE, constants.DEER_SCALING, 1050, 300, -constants.PLAYER_MOVEMENT_SPEED)

    return director



def test_trigger_game_over__should_change_game_state(director_preset):
    """
        Tests that arrow shoots.
    """
    assert director_preset.current_state != GameState.GAME_OVER
    director_preset.trigger_game_over()
    assert director_preset.current_state == GameState.GAME_OVER


pytest.main(["-v", "--tb=line", "-rN", "tests/arrow_test.py"])