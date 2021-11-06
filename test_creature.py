import pytest

from action import Attack, Move
from creature import Creature


@pytest.fixture()
def creature() -> Creature:
    return Creature(position=0)


def test_creature_init(creature: Creature) -> None:
    assert creature.position == 0
    assert creature.health == 100
    assert creature.power == 1
    assert creature.stamina == 100


def test_creature_attack(creature: Creature) -> None:
    creature.apply_attack(Attack({"damage": 60}))
    assert creature.health == 40

    creature.apply_attack(Attack({"damage": 20}))
    assert creature.health == 20


def test_creature_move(creature: Creature) -> None:
    creature.move(Move({"uses_stamina": 20, "speed": 10, "move": "test", "requires_stamina": 40}))
    assert creature.stamina == 80
    assert creature.position == 10

    creature.move(Move({"uses_stamina": 30, "speed": 10,"move": "test", "requires_stamina": 40}))
    assert creature.stamina == 50
    assert creature.position == 20

    creature.move(Move({"uses_stamina": 50, "speed": 10,"move": "test", "requires_stamina": 50}))
    assert creature.stamina == 0
    assert creature.position == 30

    creature.move(Move({"uses_stamina": 0, "speed": 10,"move": "test", "requires_stamina": 1}))
    assert creature.stamina == 0
    assert creature.position == 30
