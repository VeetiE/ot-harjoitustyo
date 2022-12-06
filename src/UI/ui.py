from tkinter import Tk, ttk
from LoginView import LoginView


class UI:
    def __init__(self, root):
        self.root = root

    def start(self):
        self._current_view = LoginView(self.root)


window = Tk()
window.title("Bugdet app")

ui = UI(window)
ui.start()

window.mainloop()
