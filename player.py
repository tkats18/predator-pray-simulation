# class
import typing

from action import Attack, Move
from body import BodyPartsInitializer, PlayerBody
from bodypart_initializer import WingedLeggedClawedTeethedInitializer
from creature import Creature
from fight_strategy import FightingStrategy
from initializer_strategy import PlayerInitializer
from walking_strategy import WalkingStrategy


class IRTSPlayer:
    def move(self) -> bool:
        pass

    def fight(self) -> Attack:
        pass

    def get_position(self) -> int:
        pass

    def get_stamina(self) -> int:
        pass

    def apply_attack(self, attack: Attack):
        pass


class DevelopedPlayer:
    def __init__(self, position: int, body_parts_initializer: BodyPartsInitializer):
        self.body = PlayerBody(body_parts_initializer)
        self.creature = Creature(position)

    def move(self, move: Move):
        self.creature.move(move)

    def apply_attack(self, attack: Attack):
        self.creature.apply_attack(attack)

    def get_possible_moves(self) -> typing.List[Move]:
        result: typing.List[Move] = []
        all_moves = self.body.get_all_player_moves()
        for i in all_moves:
            if i.requires_stamina < self.creature.stamina:
                result.append(i)

        return result

    def get_possible_attacks(self) -> typing.List[Attack]:
        return self.body.get_all_player_attacks()

    def get_position(self) -> int:
        return self.creature.position

    def get_stamina(self):
        return self.creature.stamina


class RTSPlayer(IRTSPlayer):
    def __init__(
        self,
        initializer: PlayerInitializer,
        walking_strategy: WalkingStrategy,
        fighting_strategy: FightingStrategy,
    ):
        self.developed_player = DevelopedPlayer(
            initializer.next_position(), WingedLeggedClawedTeethedInitializer()
        )
        self.walking_strategy = walking_strategy
        self.fighting_strategy = fighting_strategy

    def move(self) -> bool:
        move = self.walking_strategy.choose_move(
            self.developed_player.get_possible_moves()
        )

        if move is None:
            return False

        self.developed_player.move(move)
        return True

    def fight(self) -> Attack:
        return self.fighting_strategy.choose_attack(
            self.developed_player.get_possible_attacks()
        )

    def get_position(self) -> int:
        return self.developed_player.get_position()

    def get_stamina(self) -> int:
        return self.developed_player.get_stamina()

    def apply_attack(self, attack: Attack):
        self.developed_player.apply_attack(attack)
