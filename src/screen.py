import curses
from curses.panel import new_panel, update_panels


class Screen:
    manager = None
    window = None

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def on_event(self, event):
        pass

    def on_draw(self):
        pass


class ScreenManager:

    screens = []
    stdscr = None

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def push(self, screen: Screen):

        self.stdscr.erase()

        if self.current():
            current = self.current()
            current.on_exit()

        screen.manager = self
        screen.window = self.stdscr

        self.screens.append(screen)
        self.current().on_enter()
        self.current().on_draw()

        self.stdscr.refresh()

    def handle_resize(self):
        self.stdscr.erase()

        self.current().on_draw()
        self.stdscr.refresh()

    def pop(self):
        self.screens.pop()

    def current(self):
        if len(self.screens) == 0:
            return None
        else:
            return self.screens[-1]

    def handle_event(self, event):
        self.current().on_event(event)
