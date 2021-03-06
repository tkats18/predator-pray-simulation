import typing
from abc import abstractmethod

from action import Attack


class FightingStrategy(typing.Protocol):
    def choose_attack(self, attacks: typing.List[Attack]) -> typing.Optional[Attack]:
        pass


class BaseFightingStrategy:
    @abstractmethod
    def choose_attack(self, attacks: typing.List[Attack]) -> typing.Optional[Attack]:
        pass

    def __call__(self, attacks: typing.List[Attack]) -> typing.Optional[Attack]:
        return self.choose_attack(attacks)


class StrongestFightingStrategy(BaseFightingStrategy):
    def choose_attack(self, attacks: typing.List[Attack]) -> typing.Optional[Attack]:
        res = None
        for i in attacks:
            if res is None:
                res = i
            elif i.damage_power > res.damage_power:
                res = i
        return res
