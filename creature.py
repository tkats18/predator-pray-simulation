from dataclasses import dataclass

from action import Attack, Move


@dataclass
class Creature:
    position: int
    power: int = 1
    health: int = 100
    stamina: int = 100

    def apply_attack(self, attack: Attack) -> None:
        self.health = self.health - attack.damage_power

    def move(self, move: Move) -> None:
        self.position = self.position + move.speed
        self.stamina = self.stamina - move.uses_stamina
