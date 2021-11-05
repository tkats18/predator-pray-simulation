import random
from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol


# in case product owner makes us write another type
# of position initializer
@dataclass
class PlayerInitializer(Protocol):
    def next_position(self):
        pass


class BasePositionInitializer:
    @abstractmethod
    def next_position(self) -> int:
        pass

    def __call__(self):
        return self.next_position()


@dataclass
class SequentialPositionInitializer(BasePositionInitializer):
    last_position: int

    def next_position(self) -> int:
        res = random.randrange(0, self.last_position)
        self.last_position = res
        return res
