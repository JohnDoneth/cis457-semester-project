import curses
from curses.panel import new_panel, update_panels


class Screen:
    window = None
    panel = None

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def on_event(self, event):
        pass


class ScreenManager:

    screens = []
    stdscr = None

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def push(self, screen: Screen):
        if self.current():
            self.current().on_exit()

        height, width = self.stdscr.getmaxyx()

        screen.window = curses.newwin(height, width)
        screen.panel = new_panel(screen.window)
        screen.panel.top()
        update_panels()

        self.screens.append(screen)
        self.current().on_enter()

    def pop(self):
        self.screens.pop()

    def current(self):
        if len(self.screens) == 0:
            return None
        else:
            return self.screens[-1]

    def handle_event(self, event):
        self.current().on_event(event)


# Global
SCREEN_MANAGER = None
