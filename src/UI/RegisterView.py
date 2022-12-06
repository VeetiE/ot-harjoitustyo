from tkinter import ttk, Tk, constants
from repositories.UserRepo import UserRepository
from entities.user import User


class CreateUserView:
    def __init__(self, root, UserRepository()):

        self._root = root
        self._frame = None
        self._initialize()

    def _initialize(self):
        label = ttk.Label(master=self._root, text="Create New User")
        username_label = ttk.Label(master=self._root, text="Username")
        self.username_entry = ttk.Entry(master=self._root)
        password_label = ttk.Label(master=self._root, text="Password")
        self.password_entry = ttk.Entry(master=self._root)
        password_label2 = ttk.Label(master=self._root, text="Retype password")
        self.password_entry2 = ttk.Entry(master=self._root)
        button = ttk.Button(master=self._root, text="Create User",
                            command=self._handle_button_click)

        label.grid(row=0, column=0, columnspan=1)
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self.username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=30, pady=5)
        password_label.grid(row=2, column=0, padx=5, pady=5)
        self.password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=30, pady=5)
        password_label2.grid(row=3, column=0, padx=5, pady=5)
        self.password_entry2.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=30, pady=5)
        button.grid(row=4, column=1, sticky=(
            constants.E, constants.W), padx=30)
        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(1, weight=1, minsize=400)

    def _handle_button_click(self):
        username_entry_value = self.username_entry.get()
        password_entry_value = self.password_entry.get()
        password_entry2_value = self.password_entry2.get()
        if password_entry_value != password_entry2_value:
            print("Error! Passwords don't match")

            label2 = ttk.Label(master=self._root,
                               text="Error! Passwords don't match")
            label2.grid(row=0, column=0, columnspan=1)

        else:
            print(f"Username is: {username_entry_value}")
            print(f"Password is: {password_entry_value}")
            username = username_entry_value
            password = password_entry_value
            user = self._UserRepo.create(User(username, password))
            return user


window = Tk()
window.title("Bugdet app")

ui = CreateUserView(window)

window.mainloop()
