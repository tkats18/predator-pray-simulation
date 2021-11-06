import pytest

from attacker import Teeth
from body import PlayerBody
from bodypart_generator import BodyPartGenerator
from bodypart_initializer import WingedLeggedClawedTeethedInitializer
from constants import ATTACKER, MOVABLE
from movable import Legs, Wings


@pytest.fixture()
def body() -> PlayerBody:
    return PlayerBody(WingedLeggedClawedTeethedInitializer())


def test_body_init(body: PlayerBody) -> None:
    assert body.get_all_player_moves().__len__() != 0
    assert body.get_all_player_attacks().__len__() != 0


# რადგან რანდომია იყოს ესეც
def test_body_init_multiple(body: PlayerBody) -> None:
    for i in range(50):
        assert body.get_all_player_moves().__len__() != 0
        assert body.get_all_player_attacks().__len__() != 0


def test_body_parts_init(body: PlayerBody) -> None:
    assert body.body_parts[MOVABLE].__len__() == 2
    assert body.body_parts[ATTACKER].__len__() == 2


def test_movement_action_init(body: PlayerBody) -> None:
    assert body.body_parts[MOVABLE].__getitem__(0).get_actions().__len__() != 0
    assert body.body_parts[ATTACKER].__getitem__(0).get_actions().__len__() != 0


def test_legs(body: PlayerBody) -> None:
    legs = Legs(BodyPartGenerator())
    assert 0 <= legs.num_legs <= 2

    if legs.num_legs == 0:
        assert legs.get_actions().__len__() == 1

    if legs.num_legs == 1:
        assert legs.get_actions().__len__() == 2

    if legs.num_legs == 2:
        assert legs.get_actions().__len__() == 3 or legs.get_actions().__len__() == 4


def test_wings(body: PlayerBody) -> None:
    wings = Wings(BodyPartGenerator())
    assert 0 <= wings.num_wings <= 3

    if wings.num_wings == 0:
        assert wings.get_actions().__len__() == 0

    if wings.num_wings == 1:
        assert wings.get_actions().__len__() == 0

    if wings.num_wings == 2:
        assert wings.get_actions().__len__() == 1


def test_teeth(body: PlayerBody) -> None:
    teeth = Teeth(BodyPartGenerator())

    assert (
        teeth.sharpness == "low"
        or teeth.sharpness == "medium"
        or teeth.sharpness == "high"
    )
    assert teeth.get_actions().__len__() == 1
