from dataclasses import dataclass

from fight_strategy import StrongestFightingStrategy
from initializer_strategy import PlayerInitializer, SequentialPositionInitializer
from player import IRTSPlayer, RTSPlayer
from walking_strategy import FastestWalkingStrategy


class Game:
    def init_game(self) -> None:
        pass

    def play(self) -> None:
        pass


@dataclass
class RTSGameManager:
    @staticmethod
    def walk(prey: IRTSPlayer, predator: IRTSPlayer) -> bool:
        while prey.get_position() < predator.get_position():
            if not prey.move():
                print("Pray ran into infinity")
                return True
            if not predator.move():
                print("Predator ran into infinity")
                return True
        return False

    @staticmethod
    def fight(prey: IRTSPlayer, predator: IRTSPlayer) -> bool:

        while True:
            if predator.get_health() < 0:
                print("Predator lost in fight")
                return False

            cur_attack = predator.fight()
            if cur_attack is None:
                return False

            prey.apply_attack(cur_attack)
            if prey.get_health() < 0:
                print("Prey lost in fight")
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

    def init_game(self) -> None:
        self.player_initializer = SequentialPositionInitializer(100)
        print("INITIALIZING PREDATOR")
        self.predator = RTSPlayer(
            self.player_initializer,
            FastestWalkingStrategy(),
            StrongestFightingStrategy(),
            "Predator ",
        )

        print("INITIALIZING PREY")
        self.pray = RTSPlayer(
            self.player_initializer,
            FastestWalkingStrategy(),
            StrongestFightingStrategy(),
            "Prey ",
        )
        self.game_manager = RTSGameManager()

    def play(self) -> None:
        if not self.game_manager.walk(self.pray, self.predator):
            self.game_manager.fight(self.pray, self.predator)
