import pytest

from bodypart_initializer import WingedLeggedClawedTeethedInitializer
from constants import MOVABLE, ATTACKER
from fight_strategy import StrongestFightingStrategy
from game import RTSGameManager
from initializer_strategy import SequentialPositionInitializer
from player import DevelopedPlayer, RTSPlayer
from walking_strategy import FastestWalkingStrategy


@pytest.fixture()
def player() -> DevelopedPlayer:
    return DevelopedPlayer(0, WingedLeggedClawedTeethedInitializer())


def test_init(player: DevelopedPlayer):
    assert player.body is not None
    assert player.creature is not None


def test_correct_init(player: DevelopedPlayer):
    assert player.creature.health == 100
    assert player.creature.stamina == 100
    assert player.creature.position == 0
    assert player.creature.power == 1

    assert player.body.body_parts.get(MOVABLE).__len__() != 0
    assert player.body.body_parts.get(ATTACKER).__len__() != 0


def test_player_move(player: DevelopedPlayer):
    start_pos = player.get_position()
    moves = player.get_possible_moves()
    move = FastestWalkingStrategy().choose_move(moves)
    player.move(move)

    end_pos = player.get_position()

    assert end_pos - start_pos == move.speed


def test_player_attack(player: DevelopedPlayer):
    start_health = player.get_health()
    player_2 = DevelopedPlayer(0, WingedLeggedClawedTeethedInitializer())
    attacks = player_2.get_possible_attacks()
    attack = StrongestFightingStrategy().choose_attack(attacks)
    player.apply_attack(attack)

    end_health = player.get_health()
    assert start_health - end_health == attack.damage_power


def test_player_move_full(player: DevelopedPlayer):
    strategy = FastestWalkingStrategy()

    while True:
        move = strategy.choose_move(player.get_possible_moves())
        if move is None:
            break
        player.move(move)

    assert player.get_position() != 0
    assert player.creature.stamina == 0


def test_player_fight_full(player: DevelopedPlayer):
    player_initializer = SequentialPositionInitializer(100)
    predator = RTSPlayer(
        player_initializer,
        FastestWalkingStrategy(),
        StrongestFightingStrategy(),
        "Predator ",
    )

    pray = RTSPlayer(
        player_initializer,
        FastestWalkingStrategy(),
        StrongestFightingStrategy(),
        "Prey ",
    )

    RTSGameManager().fight(pray, predator)

    assert pray.get_health() < 0 or predator.get_health() < 0
