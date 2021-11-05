from dataclasses import dataclass


@dataclass
class Creature:
    position: int
    power: int = 1
    health: int = 100
    stamina: int = 100

    def apply_attack(self, attack):
        self.stamina = self.stamina - attack.damage_power

    def move(self, move):
        self.position = self.position + move.speed
