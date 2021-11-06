import typing
from abc import ABC

from action import Action
from bodypart_generator import BodyPart, MaxTwoLimbGenerator
from constants import (
    body_part_type,
    leg_action_mapping,
    movement_type,
    names,
    wing_action_mapping,
)


class Movable(BodyPart):
    @staticmethod
    def get_type() -> str:
        return body_part_type["movable_name"]


class Wings(Movable, ABC):
    def __init__(self, generator: MaxTwoLimbGenerator):
        self.num_wings = generator.generate_max_two()

    def get_actions(self) -> typing.List[Action]:
        return pack_movement_data(num=self.num_wings, mapping=wing_action_mapping)

    def get_name(self) -> str:
        return names["wing_name"]

    def to_representation(self) -> str:
        return self.get_name() + "  " + str(self.num_wings)


class Legs(Movable, ABC):
    def __init__(self, generator: MaxTwoLimbGenerator):
        self.num_legs = generator.generate_max_two()

    def get_actions(self) -> typing.List[Action]:
        return pack_movement_data(num=self.num_legs, mapping=leg_action_mapping)

    def get_name(self) -> str:
        return names["leg_name"]

    def to_representation(self) -> str:
        return self.get_name() + "  " + str(self.num_legs)


def pack_movement_data(
    num: int, mapping: typing.Dict[int, typing.List[typing.Any]]
) -> typing.List[Action]:
    result = []
    for i in range(num + 1):
        possible_moves = mapping[i]
        for j in possible_moves:
            data = movement_type[j]
            data["move"] = j
            result.append(Action(data))
    return [*result]
