from screen import Screen
import curses

from enum import IntEnum


class GameType(IntEnum):
    TicTacToe = 0
    RockPaperScissors = 1


class ConnectScreen(Screen):
    """
    Connect screen
    """

    game_type = None

    def __init__(self, game_type: GameType):
        self.game_type = game_type

    def on_enter(self):
        # print("screen entered")

        self.window.addstr("Pretty text", curses.color_pair(1))
        self.window.refresh()

    def on_exit(self):
        pass
        # print("screen exited")

    def on_event(self, event):
        # self.window.addstr(f"{event}", curses.color_pair(1))
        # self.window.refresh()

        pass
        # print(f"event {event}")
