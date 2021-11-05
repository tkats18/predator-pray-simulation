from dataclasses import dataclass

from fight_strategy import StrongestFightingStrategy
from initializer_strategy import PlayerInitializer, SequentialPositionInitializer
from player import RTSPlayer, IRTSPlayer
from walking_strategy import FastestWalkingStrategy


class Game:
    def init_game(self):
        pass

    def play(self):
        pass

    def reset(self):
        pass


@dataclass
class RTSGameManager:
    @staticmethod
    def walk(prey: IRTSPlayer, predator: IRTSPlayer) -> bool:
        while prey.get_position() < predator.get_position():
            if not prey.move():
                return True
            if not predator.move():
                return True
        return False

    @staticmethod
    def fight(prey: IRTSPlayer, predator: IRTSPlayer) -> bool:

        while True:
            if predator.get_stamina() < 0:
                return False

            cur_attack = predator.fight()
            if cur_attack is None:
                return False

            prey.apply_attack(cur_attack)
            if prey.get_stamina() < 0:
                return False

            cur_attack = prey.fight()
            if cur_attack is None:
                return False

            predator.apply_attack(cur_attack)


class RTSGame(Game):
    pray: IRTSPlayer
    predator: IRTSPlayer
    player_initializer: PlayerInitializer
    game_manager: RTSGameManager

    def init_game(self):
        self.player_initializer = SequentialPositionInitializer(100)
        self.predator = RTSPlayer(
            self.player_initializer,
            FastestWalkingStrategy(),
            StrongestFightingStrategy(),
        )
        self.pray = RTSPlayer(
            self.player_initializer,
            FastestWalkingStrategy(),
            StrongestFightingStrategy(),
        )
        self.game_manager = RTSGameManager()

    def play(self):
        if self.game_manager.walk(self.pray, self.predator):
            self.game_manager.fight(self.pray, self.predator)

    def reset(self):
        pass
