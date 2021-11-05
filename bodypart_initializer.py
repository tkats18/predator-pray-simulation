import typing
from abc import abstractmethod
from typing import Protocol

from attacker import Claws, Teeth
from bodypart_generator import BodyPart, BodyPartGenerator
from constants import body_part_type
from movable import Legs, Wings


class BodyPartsInitializer(Protocol):
    def initialize_body_parts(self) -> typing.Dict[str, typing.List[BodyPart]]:
        pass


class BasePartsInitializer:
    @abstractmethod
    def initialize_body_parts(self) -> typing.Dict[str, typing.List[BodyPart]]:
        return {}

    def __call__(self) -> typing.Dict[str, typing.List[BodyPart]]:
        return self.initialize_body_parts()


# შეგვიძლია დავამატოთ ახალი ტიპის ფლეიერი (მაგ ფეხებით და კბილებით მარტო)
# ისე რო მშობელს არც ეცოდინება უბლოდ ინიციალაიზერს შევცვლით და ვსო


class WingedLeggedClawedTeethedInitializer(BasePartsInitializer):
    def initialize_body_parts(self) -> typing.Dict[str, typing.List[BodyPart]]:
        result: typing.Dict[str, typing.List[BodyPart]] = {}

        for i in body_part_type.keys():
            result[body_part_type[i]] = []

        claws = Claws(BodyPartGenerator())
        legs = Legs(BodyPartGenerator())
        teeth = Teeth(BodyPartGenerator())
        wings = Wings(BodyPartGenerator())

        result[claws.get_type()].append(claws)
        result[legs.get_type()].append(legs)
        result[teeth.get_type()].append(teeth)
        result[wings.get_type()].append(wings)

        return result
