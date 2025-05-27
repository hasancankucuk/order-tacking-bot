import os

def get_db_path(db_name: str = None) -> str:
    if not db_name:
        db_name = os.getenv("DB_NAME")
    backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_path = os.path.abspath(os.path.join(backend_dir, db_name))
    return db_path