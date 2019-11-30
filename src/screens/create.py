from screen import Screen
import curses

from screens.connect import ConnectScreen, GameType


class CreateScreen(Screen):
    """
    Create screen
    """

    selection = 0

    options = ["Tic-Tac-Toe", "Rock-Paper-Scissors"]

    def _draw_option(self, option_number, style):
        self.window.addstr(
            5 + option_number,
            4,
            "{:2} - {}".format(option_number + 1, self.options[option_number]),
            style,
        )

    def on_enter(self):
        self.hilite_color = curses.color_pair(1)
        self.normal_color = curses.A_NORMAL

    def on_draw(self):
        self.window.addstr(1, 2, "Connected to 127.0.0.1 - Creating Game")

        option_count = len(self.options)

        self.window.border(0)
        for option in range(option_count):
            if self.selection == option:
                self._draw_option(option, self.hilite_color)
            else:
                self._draw_option(option, self.normal_color)

    def on_exit(self):
        pass

    def on_event(self, event):

        input_key = event

        down_keys = [curses.KEY_DOWN, ord("j")]
        up_keys = [curses.KEY_UP, ord("k")]

        option_count = len(self.options) - 1

        ENTER_KEY = ord("\n")
        if input_key == ENTER_KEY:

            if self.selection == 0:
                self.manager.push(ConnectScreen(GameType.RockPaperScissors))
            elif self.selection == 1:
                self.manager.push(ConnectScreen(GameType.TicTacToe))
            else:
                pass

            pass

        if input_key in down_keys:
            if self.selection < option_count:
                self.selection += 1
            else:
                self.selection = 0

        if input_key in up_keys:
            if self.selection > 0:
                self.selection -= 1
            else:
                self.selection = option_count

        self.window.erase()
        self.on_draw()
        # print(f"event {event}")
