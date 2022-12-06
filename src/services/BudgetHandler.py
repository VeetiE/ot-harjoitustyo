from entities.budget import Budget
from entities.user import User
from repositories.UserRepo import UserRepository
from repositories.BudgetRepo import BudgetRepository


class InvalidCredentialsError(Exception):
    pass


class BudgetHandler:
    def __init__(self, UR=UserRepository(), BR=BudgetRepository):
        self._user = None
        self._UR = UR
        self._BR = BR

    #Creates new budget
    def create_buget(self, name, user, amount, beginning_date, ending_date, current_date):
        new_budget = Budget(name, user, amount,
                            beginning_date, ending_date, current_date)
        return new_budget

    #Lists budgets
    def list_budgets(self):
        pass

    #Handles login
    def login(self, username):

        user = self._UR.find_by_username(username)
        if user is None:
            # User does not exist, display error message
            raise InvalidCredentialsError("incorrect username or password")
        else:
            self._user = user
            return user
