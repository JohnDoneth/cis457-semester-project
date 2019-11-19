import curses
import sys
import os

from menu import CursesMenu
from screen import SCREEN_MANAGER, ScreenManager
from screens.connect import ConnectScreen

if __name__ == "__main__":

    stdscr = curses.initscr()

    # init curses and curses input
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.curs_set(0)  # Hide cursor
    # screen.keypad(1)

    # set up color pair for highlighted option
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    hilite_color = curses.color_pair(1)
    normal_color = curses.A_NORMAL

    # stdscr.addstr("Pretty text", curses.color_pair(1))
    # stdscr.refresh()

    SCREEN_MANAGER = ScreenManager(stdscr)
    SCREEN_MANAGER.push(ConnectScreen())

    input_key = stdscr.getch()
    while input_key != 27:
        SCREEN_MANAGER.handle_event(input_key)

        input_key = stdscr.getch()
        pass

    menu = {"title": "Semester Project", "type": "menu", "subtitle": "Select an action"}

    option_1 = {
        "title": "Connect to matchmaking server",
        "type": "command",
        "command": "echo Hello World!",
    }

    menu["options"] = [option_1]

    # m = CursesMenu(menu)
    # selected_action = m.display()

    # if selected_action["type"] != "exitmenu":
    #    os.system(selected_action["command"])
