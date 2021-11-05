import typing
from dataclasses import dataclass


@dataclass
class Action:
    data: typing.Dict[str, int]


class Attack:
    damage_power: int

    def __init__(self, data: typing.Dict[str, int]) -> None:
        self.damage_power = int(data["damage"])


# ცალცალკე ტიპების შექმნა შემეძლო მაგრამ არგავაკეთე იმიტომ რომ
# იგივე ჯენერიქობას მივიღებდი, აწი თუ მოუნდება დამატება ვინმეს კონსტანტებში ჩაამატებს და ვსო
class Move:
    move: str
    requires_stamina: int
    uses_stamina: int
    speed: int

    def __init__(self, data: typing.Dict[str, int]) -> None:
        self.requires_stamina = data["requires_stamina"]
        self.uses_stamina = data["uses_stamina"]
        self.speed = data["speed"]
        self.move = str(data["move"])
