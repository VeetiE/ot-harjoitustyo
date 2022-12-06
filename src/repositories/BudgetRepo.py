from db_connection import get_database_connection
from entities.budget import Budget
from repositories.UserRepo import UserRepository


class BudgetRepository:
    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor()

#Retrieves all budgets from database
    def get_all_budgets(self):
        self._cursor.execute("SELECT * from budgets")

        rows = self._cursor.fetchall()
        return map(rows)

#Retrieves all budget from db by username
    def find_by_username(self, username):
        pass


budget_repository = BudgetRepository(get_database_connection())
