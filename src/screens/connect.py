from screen import Screen
import curses


class ConnectScreen(Screen):
    def on_enter(self):
        # print("screen entered")

        self.window.addstr("Pretty text", curses.color_pair(1))
        self.window.refresh()

    def on_exit(self):
        pass
        # print("screen exited")

    def on_event(self, event):
        self.window.addstr(f"{event}", curses.color_pair(1))
        self.window.refresh()

        pass
        # print(f"event {event}")
