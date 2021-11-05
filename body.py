import typing

from action import Attack, Move
from bodypart_initializer import BodyPartsInitializer
from constants import ATTACKER, MOVABLE


class PlayerBody:
    def __init__(self, body_parts_initializer: BodyPartsInitializer):
        self.body_parts = body_parts_initializer.initialize_body_parts()

    def get_all_player_moves(self) -> typing.List[Move]:
        result: typing.List[Move] = []
        parts = self.body_parts.get(MOVABLE)
        if parts is not None:
            for i in parts:
                for j in i.get_actions():
                    result.append(Move(data=j.data))
        return result

    def get_all_player_attacks(self) -> typing.List[Attack]:
        result: typing.List[Attack] = []
        parts = self.body_parts.get(ATTACKER)
        if parts is not None:
            for i in parts:
                for j in i.get_actions():
                    result.append(Attack(j.data))
        return result

    def to_representation(self) -> typing.Dict[str, typing.List[str]]:
        data: typing.Dict[str, typing.List[str]] = {MOVABLE: [], ATTACKER: []}
        parts_attacker = self.body_parts.get(ATTACKER)
        parts_movable = self.body_parts.get(MOVABLE)

        if parts_movable is not None:
            for i in parts_movable:
                data[MOVABLE].append(i.to_representation())

        if parts_attacker is not None:
            for i in parts_attacker:
                data[ATTACKER].append(i.to_representation())

        return data
