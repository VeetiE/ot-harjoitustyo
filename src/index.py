from tkinter import Tk
from UI.ui import UI
from UI.LoginView import LoginView


def main():
    window = Tk()
    window.title('Budget App')

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == '__main__':
    main()
