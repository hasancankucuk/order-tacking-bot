import os
import sqlite3
from dotenv import load_dotenv  # type: ignore
from faker import Faker  # type: ignore
import datetime
from helpers.get_db_path import get_db_path

fake = Faker()
load_dotenv(dotenv_path="backend/.env")


def create_connection(db_path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        print(f"Connection to SQLite DB successful: {db_path}")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return conn


def execute_query(conn, query, params=None):
    try:
        cur = conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        conn.commit()
        return cur
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


def fetch_data(conn, query, params=None):
    try:
        cur = conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


# TODO: This function should be moved to methods.py and should be seperated to queries!!!
def create_db():
    db_name = os.getenv("DB_NAME")
    if not db_name:
        raise ValueError("DB_NAME environment variable is not set.")

    db_path = get_db_path(db_name)

    if os.path.exists(db_path):
        os.remove(db_path)

    conn = create_connection(db_path)
    if conn is None:
        return

    sql_scripts = """
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        address TEXT
    );

    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        price REAL,
        quantity INTEGER,
        category TEXT,
        image TEXT
    );

    CREATE TABLE IF NOT EXISTS shipping_methods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );

    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        shipping_method_id INTEGER,
        total REAL,
        status TEXT DEFAULT 'pending',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        changed_at TEXT,
        cancellation_fee REAL DEFAULT 0,
        shipping_address TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE CASCADE,
        FOREIGN KEY(shipping_method_id) REFERENCES shipping_methods(id)
    );

    CREATE TABLE IF NOT EXISTS order_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        product_id INTEGER,
        price REAL,
        FOREIGN KEY(order_id) REFERENCES orders(id) ON DELETE CASCADE,
        FOREIGN KEY(product_id) REFERENCES products(id)
    );

    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        email TEXT UNIQUE,
        role TEXT DEFAULT 'user'
    );
    """

    try:
        cur = conn.cursor()
        cur.executescript(sql_scripts)
        conn.commit()
        print("Database tables created successfully")
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        print("Created tables:", tables)
        cur.close()
        conn.close()
        print("Database setup completed")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
        if conn:
            conn.rollback()
            conn.close()
        return
