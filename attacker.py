import typing
from abc import ABC, abstractmethod

from action import Action
from bodypart_generator import BodyPart, ThreeLevelPartGenerator
from constants import (body_part_type, claws_attacking_power_multiplier, names,
                       teeth_attacking_power_additive)


class Attacking(BodyPart):
    attacking_power = 1

    def get_actions(self) -> typing.List[Action]:
        return [Action(str(self.attacking_power))]

    @abstractmethod
    def get_type(self) -> str:
        return body_part_type["attacker_name"]


class Teeth(Attacking, ABC):
    sharpness: str

    def __init__(self, generator: ThreeLevelPartGenerator):
        self.sharpness = generator.generate_tree_level_part()

    def get_actions(self) -> typing.List[Action]:
        cur_power = (
                self.attacking_power + teeth_attacking_power_additive[self.sharpness]
        )
        return [Action(str(cur_power))]

    def get_name(self) -> str:
        return names["teeth_name"]

    def to_representation(self) -> str:
        return self.get_name() + "  " + str(self.attacking_power)


class Claws(Attacking, ABC):
    size: str

    def __init__(self, generator: ThreeLevelPartGenerator):
        self.size = generator.generate_tree_level_part()

    def get_actions(self) -> typing.List[Action]:
        cur_power = self.attacking_power * claws_attacking_power_multiplier[self.size]
        return [Action(str(cur_power))]

    def get_name(self) -> str:
        return names["claw_name"]

    def to_representation(self) -> str:
        return self.get_name() + "  " + str(self.attacking_power)
