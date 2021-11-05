import typing

from action import Attack, Move
from bodypart_initializer import BodyPartsInitializer
from constants import ATTACKER, MOVABLE


class PlayerBody:
    def __init__(self, body_parts_initializer: BodyPartsInitializer):
        self.body_parts = body_parts_initializer.initialize_body_parts()

    def get_all_player_moves(self) -> typing.List[Move]:
        result: typing.List[Move] = []
        for i in self.body_parts.get(MOVABLE):
            for j in i.get_actions():
                result.append(Move(data=j.data))
        return result

    def get_all_player_attacks(self) -> typing.List[Attack]:
        result: typing.List[Attack] = []
        for i in self.body_parts.get(ATTACKER):
            for j in i.get_actions():
                result.append(Attack(j.data))
        return result
