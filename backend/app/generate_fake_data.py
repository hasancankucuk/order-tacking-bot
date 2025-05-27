import os
import sqlite3
from faker import Faker
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

DATABASE_NAME = os.getenv("DB_NAME")

fake = Faker()


def create_connection(db_path=DATABASE_NAME):
    try:
        conn = sqlite3.connect(db_path)
        print(f"Connected to SQLite DB: {db_path}")
        return conn
    except sqlite3.Error as e:
        print(f"SQLite connection error: {e}")
        return None


def generate_fake_products(conn, number_of_products=100):
    cur = conn.cursor()
    for _ in range(number_of_products):
        product_name = fake.word().title()
        product_description = fake.text(max_nb_chars=200)
        product_price = round(
            fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2
        )
        product_quantity = fake.random_int(min=1, max=500)
        product_category = fake.word()
        cur.execute(
            "INSERT INTO products (name, description, price, quantity, category) VALUES (?, ?, ?, ?, ?)",
            (
                product_name,
                product_description,
                product_price,
                product_quantity,
                product_category,
            ),
        )
    conn.commit()


def generate_fake_customers(conn, number_of_customers=50):
    cur = conn.cursor()
    for _ in range(number_of_customers):
        customer_name = fake.name()
        customer_email = fake.email()
        customer_phone = fake.phone_number()
        customer_address = fake.address().replace("\n", ", ")
        cur.execute(
            "INSERT INTO customers (name, email, phone, address) VALUES (?, ?, ?, ?)",
            (customer_name, customer_email, customer_phone, customer_address),
        )
    conn.commit()


def generate_fake_shipping_methods(conn):
    cur = conn.cursor()
    shipping_methods = ["Standard", "Express", "Overnight"]
    for method in shipping_methods:
        cur.execute("INSERT INTO shipping_methods (name) VALUES (?)", (method,))
    conn.commit()


def generate_fake_orders(conn, number_of_orders=50):
    cur = conn.cursor()
    cur.execute("SELECT id FROM customers")
    customers = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT id FROM shipping_methods")
    shipping_methods = [row[0] for row in cur.fetchall()]

    for _ in range(number_of_orders):
        customer_id = fake.random_element(elements=customers)
        shipping_method_id = fake.random_element(elements=shipping_methods)
        order_total = round(
            fake.pyfloat(left_digits=4, right_digits=2, positive=True), 2
        )
        cur.execute(
            "INSERT INTO orders (customer_id, shipping_method_id, total) VALUES (?, ?, ?)",
            (customer_id, shipping_method_id, order_total),
        )
    conn.commit()


def generate_fake_order_details(conn, number_of_details=100):
    cur = conn.cursor()
    cur.execute("SELECT id FROM orders")
    orders = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT id, price FROM products")
    products = cur.fetchall()

    for _ in range(number_of_details):
        order_id = fake.random_element(elements=orders)
        product = fake.random_element(elements=products)
        product_id = product[0]
        price = product[1]
        cur.execute(
            "INSERT INTO order_details (order_id, product_id, price) VALUES (?, ?, ?, ?)",
            (order_id, product_id, price),
        )
    conn.commit()


def main():
    conn = create_connection()
    if conn:
        generate_fake_shipping_methods(conn)
        generate_fake_customers(conn)
        generate_fake_products(conn)
        generate_fake_orders(conn)
        generate_fake_order_details(conn)
        conn.close()
        print("Fake data generated successfully in database.")
    else:
        print("Failed to connect to the database.")