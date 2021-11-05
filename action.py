from dataclasses import dataclass


@dataclass
class Action:
    data: str

    def get_type(self) -> str:
        pass


class Attack:
    damage_power: int

    def __init__(self, data):
        self.damage_power = int(data)


# ცალცალკე ტიპების შექმნა შემეძლო მაგრამ არგავაკეთე იმიტომ რომ
# იგივე ჯენერიქობას მივიღებდი, აწი თუ მოუნდება დამატება ვინმეს კონსტანტებში ჩაამატებს და ვსო
class Move:
    move: str
    requires_stamina: int
    uses_stamina: int
    speed: int

    def __init__(self, data):
        self.requires_stamina = data["requires_stamina"]
        self.uses_stamina = data["uses_stamina"]
        self.speed = data["speed"]
        self.move = data["move"]
