import typing
from abc import abstractmethod
from typing import Protocol

from action import Move


class WalkingStrategy(Protocol):
    def choose_move(self, moves: typing.List[Move]) -> Move:
        pass


class BaseWalkingStrategy:
    @abstractmethod
    def choose_move(self, moves: typing.List[Move]) -> Move:
        pass

    def __call__(self, moves: typing.List[Move]):
        self.choose_move(moves)


class FastestWalkingStrategy(BaseWalkingStrategy):
    def choose_move(self, moves: typing.List[Move]) -> Move:
        res = None

        for i in moves:
            if res is None:
                res = i
            elif res.speed < i.speed:
                res = i
        return res
