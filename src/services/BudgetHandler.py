from entities.budget import Budget
from entities.user import User


class InvalidCredentialsError(Exception):
    pass


class BudgetHandler:
    def __init__(self):
        pass

    def create_buget(self, name, user, amount, beginning_date, ending_date, current_date):
        new_budget = Budget(name, user, amount,
                            beginning_date, ending_date, current_date)
        return new_budget

    def list_budgets(self):
        pass
