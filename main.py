# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
from game import RTSGame

if __name__ == "__main__":
    game = RTSGame()
    for i in range(100):
        print("///////////////////////GAME " + str(i) + "///////////////////////")
        game.init_game()
        game.play()
