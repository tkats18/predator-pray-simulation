import typing
from abc import abstractmethod, ABC

from action import Action
from bodypart_generator import MaxTwoLimbGenerator
from bodypart_initializer import BodyPart
from constants import (
    wing_action_mapping,
    leg_action_mapping,
    names,
    body_part_type,
    movement_type,
)


class Movable(BodyPart):
    @abstractmethod
    def get_type(self) -> str:
        return body_part_type["movable_name"]


class Wings(Movable, ABC):
    def __init__(self, generator: MaxTwoLimbGenerator):
        self.num_wings = generator.generate_max_two()

    def get_actions(self) -> typing.Iterable[Action]:
        return pack_movement_data(
            num_limbs=self.num_wings, action_mapping=wing_action_mapping
        )

    def get_name(self) -> str:
        return names["wing_name"]


class Legs(Movable, ABC):
    def __init__(self, generator: MaxTwoLimbGenerator):
        self.num_legs = generator.generate_max_two()

    def get_actions(self) -> typing.Iterable[Action]:
        return pack_movement_data(
            num_limbs=self.num_legs, action_mapping=leg_action_mapping
        )

    def get_name(self) -> str:
        return names["leg_name"]


def pack_movement_data(num_limbs: int, action_mapping) -> typing.Iterable[Action]:
    result = []
    for i in range(num_limbs):
        possible_moves = action_mapping[i]
        for j in possible_moves:
            data = movement_type[j]
            data["move"] = j
            result.append(Action(data))
    return [*result]
