from config import BUDGET_APPS_FILE_PATH
from db_connection import get_database_connection


class BudgetRepository:
    def __init__(self, file_path):
        self._file_path = file_path


budget_repository = BudgetRepository(get_database_connection())