import os
from .get_db_path import get_db_path

def get_validated_db_path(dispatcher=None) -> bool:
    name = os.getenv("DB_NAME")
    if not name:
        name = "retail.db"
    db_path = get_db_path(name)
    if not os.path.exists(db_path):
        if dispatcher:
            dispatcher.utter_message(text=f"Database file not found at {db_path}.")
        return None
    return db_path


