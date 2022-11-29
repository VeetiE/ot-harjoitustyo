import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

BUDGET_APPS_FILENAME = os.getenv("BUDGET_APPS_FILENAME") or "budget.csv"
BUDGET_APPS_FILE_PATH = os.path.join(dirname, BUDGET_APPS_FILENAME)

DB_FILENAME = os.getenv("DB_FILENAME") or "db.sqlite"
DB_FILE_PATH = os.path.join(dirname, "..", "data", DB_FILENAME)
