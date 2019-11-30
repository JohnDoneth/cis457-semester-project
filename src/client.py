import curses
import sys
import os

from menu import CursesMenu
from screen import ScreenManager
from screens.connect import ConnectScreen
from screens.menu import MenuScreen

if __name__ == "__main__":
    stdscr = curses.initscr()

    # init curses and curses input
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.curs_set(0)  # Hide cursor
    stdscr.keypad(1)

    # set up color pair for highlighted option
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    hilite_color = curses.color_pair(1)
    normal_color = curses.A_NORMAL

    manager = ScreenManager(stdscr)
    manager.push(MenuScreen())

    try:
        while True:
            input_key = stdscr.getch()

            if input_key == curses.KEY_RESIZE:
                manager.handle_resize()

            if input_key == 27:
                break

            manager.handle_event(input_key)
            manager.handle_resize()

    except KeyboardInterrupt:
        pass

    # shutdown code
    curses.nocbreak()
    stdscr.clear()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()
    print("Thanks for playing!")
