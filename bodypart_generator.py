import random
import typing
from typing import Protocol

from action import Action
from constants import power_mapping


class BodyPart:
    def get_name(self) -> str:
        pass

    def get_actions(self) -> typing.List[Action]:
        pass

    def to_representation(self) -> str:
        pass


class BodyPartGenerator:
    @staticmethod
    def generate_max_two() -> int:
        return random.Random().randrange(0, 3)

    @staticmethod
    def generate_tree_level_part() -> str:
        return power_mapping[random.Random().randrange(0, 3)]


class MaxTwoLimbGenerator(Protocol):
    def generate_max_two(self) -> int:
        pass


class ThreeLevelPartGenerator(Protocol):
    def generate_tree_level_part(self) -> str:
        pass
