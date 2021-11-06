import typing
from dataclasses import dataclass


@dataclass
class Action:
    data: typing.Dict[str, typing.Any]


class Attack:
    damage_power: int

    def __init__(self, data: typing.Dict[str, typing.Any]) -> None:
        self.damage_power = int(data["damage"])


# ცალცალკე ტიპების შექმნა შემეძლო მაგრამ არგავაკეთე იმიტომ რომ
# იგივე ჯენერიქობას მივიღებდი, აწი თუ მოუნდება დამატება ვინმეს კონსტანტებში ჩაამატებს და ვსო
class Move:
    move: str
    requires_stamina: int
    uses_stamina: int
    speed: int

    def __init__(self, data: typing.Dict[str, typing.Any]) -> None:
        self.requires_stamina = int(data["requires_stamina"])
        self.uses_stamina = int(data["uses_stamina"])
        self.speed = int(data["speed"])
        self.move = str(data["move"])
