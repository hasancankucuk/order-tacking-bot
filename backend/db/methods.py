import datetime
import random
from faker import Faker  # type: ignore
from .db_utils import create_connection, execute_query, fetch_data
from helpers.cancel_fee_calculator import calculate_cancellation_fee
from .queries import (
    get_order_by_id_query,
    update_order_status_query,
    update_shipping_address_query,
    update_shipping_method_query,
    get_customer_id_by_order_id_query,
    get_shipping_method_id_by_name_query,
    get_cancellation_fee_query,
    get_invoice_query,
    get_tables_query,
    get_all_customers_query,
    get_all_products_query,
    get_all_orders_query,
    get_all_order_details_query,
    get_all_shipping_methods_query,
    get_all_from_table_query,
    get_user_query,
    set_user_query,
    update_user_query,
    get_shipping_method_id_query,
    add_order_query,
    add_order_detail_query,
    drop_all_tables_query,
    add_produtcs_query,
    add_customer_query,
    add_new_shipping_method_query,
    get_customer_by_email_query,
    get_product_by_name_query,
    update_product_quantity_query,
)


def get_order_by_id(order_id, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_order_by_id_query(), (order_id,))
        result = cur.fetchone()
        return result
    except Exception as e:
        print(f"Error while fetching order: {e}")
        return None
    finally:
        if conn:
            conn.close()


def get_customer_id_by_order_id(order_id, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_customer_id_by_order_id_query(), (order_id,))
        row = cur.fetchone()
        return row[0] if row else None
    except Exception as e:
        print(f"Error fetching customer ID for order {order_id}: {e}")
        return None
    finally:
        conn.close()


def get_shipping_method_id_by_name(shipping_method_name, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(
            conn, get_shipping_method_id_by_name_query(), (shipping_method_name,)
        )
        row = cur.fetchone()
        return row[0] if row else None
    except Exception as e:
        print(f"Error fetching shipping method ID for '{shipping_method_name}': {e}")
        return None
    finally:
        conn.close()


def get_cancellation_fee(order_id, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_cancellation_fee_query(), (order_id,))
        row = cur.fetchone()
        print("row", row)
        return row[0] if row else None
    except Exception as e:
        print(f"Error fetching cancellation fee for order ${order_id}: {e}")
        return None
    finally:
        conn.close()


def get_invoice(order_id, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_invoice_query(), (order_id,))
        row = cur.fetchone()
        if row:
            invoice = {
                "order_id": row[0],
                "shipping_address": row[1],
                "customer_name": row[2],
                "shipping_method": row[3],
                "status": row[4],
                "cancellation_fee": row[5],
                "total": row[6],
                "ordered_items": row[7],
            }
            return invoice
        else:
            print(f"No invoice found for order {order_id}.")
            return None
    except Exception as e:
        print(f"Error while fetching invoice: {e}")
        return None
    finally:
        if conn:
            conn.close()


def get_tables(db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_tables_query())
        return [row[0] for row in cur.fetchall()]
    except Exception as e:
        print(f"Error while fetching tables: {e}")
        return []


def get_all_customers(db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_all_customers_query())
        return [
            dict(zip([column[0] for column in cur.description], row))
            for row in cur.fetchall()
        ]
    except Exception as e:
        print(f"Error while fetching customers: {e}")
        return []
    finally:
        if conn:
            conn.close()


def get_all_products(db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_all_products_query())
        return [
            dict(zip([column[0] for column in cur.description], row))
            for row in cur.fetchall()
        ]
    except Exception as e:
        print(f"Error while fetching products: {e}")
        return []
    finally:
        if conn:
            conn.close()


def get_all_orders(db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_all_orders_query())
        return [
            dict(zip([column[0] for column in cur.description], row))
            for row in cur.fetchall()
        ]
    except Exception as e:
        print(f"Error while fetching orders: {e}")
        return []
    finally:
        if conn:
            conn.close()


def get_all_order_details(db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_all_order_details_query())
        return [
            dict(zip([column[0] for column in cur.description], row))
            for row in cur.fetchall()
        ]
    except Exception as e:
        print(f"Error while fetching order details: {e}")
        return []
    finally:
        if conn:
            conn.close()


def get_all_shipping_methods(db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_all_shipping_methods_query())
        return [
            dict(zip([column[0] for column in cur.description], row))
            for row in cur.fetchall()
        ]
    except Exception as e:
        print(f"Error while fetching shipping methods: {e}")
        return []
    finally:
        if conn:
            conn.close()


def get_all_from_table(table_name, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_all_from_table_query(table_name))
        return [
            dict(zip([column[0] for column in cur.description], row))
            for row in cur.fetchall()
        ]
    except Exception as e:
        print(f"Error while fetching data from table {table_name}: {e}")
        return []
    finally:
        if conn:
            conn.close()


def update_order_status(order_id, status, db_path=None):
    conn = create_connection(db_path)
    try:
        changed_at = datetime.datetime.now().isoformat()
        cur = execute_query(
            conn, update_order_status_query(), (status, changed_at, order_id)
        )
        conn.commit()
        if cur.rowcount == 0:
            print(f"No order found with id {order_id}.")
            return False
        print(f"Order {order_id} updated to status '{status}'")
        return True
    except Exception as e:
        print(f"Error while updating order status: {e}")
        return False
    finally:
        if conn:
            conn.close()


def update_shipping_address(order_id, new_address, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(
            conn, update_shipping_address_query(), (new_address, order_id)
        )
        conn.commit()
        if cur.rowcount == 0:
            print(f"No order found with id {order_id}.")
            return False
        print(f"Order {order_id} shipping address updated to '{new_address}'")
        return True
    except Exception as e:
        print(f"Error while updating shipping address: {e}")
        return False
    finally:
        if conn:
            conn.close()


def update_shipping_method(order_id, shipping_method_id, changed_at, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(
            conn,
            update_shipping_method_query(),
            (changed_at, shipping_method_id, order_id),
        )
        conn.commit()
        if cur.rowcount == 0:
            print(f"No order found with id {order_id}.")
            return False
        print(f"Order {order_id} shipping method updated to '{shipping_method_id}'")
        return True
    except Exception as e:
        print(f"Error while updating shipping method: {e}")
        return False
    finally:
        if conn:
            conn.close()


def get_custom_query(query, params=None, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        rows = cur.fetchall()
        return [
            dict(zip([column[0] for column in cur.description], row)) for row in rows
        ]
    except Exception as e:
        print(f"Error while executing custom query: {e}")
        return None
    finally:
        if conn:
            conn.close()
    return None


def get_user(username, password, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, get_user_query(), (username, password))
        row = cur.fetchone()
        if row:
            return {
                "id": row[0],
                "username": row[1],
                "password": row[2],
                "email": row[3],
                "role": row[4],
            }
        else:
            print(f"No user found with username {username}.")
            return None
    except Exception as e:
        print(f"Error while fetching user: {e}")
        return None


def set_user(username, password, email, role, db_path=None):
    conn = create_connection(db_path)
    try:
        cur = execute_query(conn, set_user_query(), (username, password, email, role))
        print(cur)
        if cur.rowcount == 0:
            print(f"Failed to insert user {username}.")
            return False
        print(f"User {username} inserted successfully.")
        return True
    except Exception as e:
        print(f"Error while inserting user: {e}")
        return False


def update_user(
    user_id, username=None, password=None, email=None, role=None, db_path=None
):
    conn = create_connection(db_path)
    try:
        fields = []
        params = []
        if password is not None:
            fields.append("password = ?")
            params.append(password)
        if email is not None:
            fields.append("email = ?")
            params.append(email)
        if role is not None:
            fields.append("role = ?")
            params.append(role)
        if username is not None:
            fields.append("username = ?")
            params.append(username)
        if not fields:
            return False
        params.append(user_id)
        sql = f"UPDATE users SET {', '.join(fields)} WHERE id = ?;"
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        return cur.rowcount > 0
    except Exception as e:
        print(f"Error while updating user: {e}")
        return False


def delete_database(db_path=None):
    try:
        conn = create_connection(db_path)
        if conn:
            cur = conn.cursor()
            cur.executescript(drop_all_tables_query())
            conn.commit()
            conn.close()
            print("All tables dropped successfully.")
            return True
        else:
            print(f"Database {db_path} does not exist.")
            return False
    except Exception as e:
        print(f"Error while deleting database: {e}")
        return False


def seed_database(db_path=None):
    fake = Faker()
    try:
        conn = create_connection(db_path)
        if conn:
            existing = fetch_data(conn, "SELECT 1 FROM customers LIMIT 1;")
            if existing:
                print("Database already contains data, skipping seeding.")
                conn.close()
                return

            print("Database is empty, seeding started...")

            shipping_methods = ["Standard", "Express", "Overnight"]
            for method in shipping_methods:
                execute_query(conn, add_new_shipping_method_query(), (method,))

            number_of_products = 10
            number_of_customers = 10
            number_of_orders = 10
            number_of_order_details = 5

            for _ in range(number_of_customers):
                name = fake.name()
                email = fake.email()
                phone = fake.phone_number()
                address = fake.address().replace("\n", ", ")
                execute_query(
                    conn,
                    add_customer_query(),
                    (name, email, phone, address),
                )

            fake_products = [
                    {
                        "name": "Wireless Headphones",
                        "image": "https://de.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw9f5d8cf1/1.JBL_Tune_770NC_Product%20Image_Hero_Purple.png?sw=680&sh=680",
                        "category": "Electronics",
                    },
                    {
                        "name": "Smartphone Case",
                        "image": "https://bellroy-product-images.imgix.net/bellroy_dot_com_gallery_image/EUR/PCYI-SEN-133/0?auto=format&fit=crop&w=1500&h=1500",
                        "category": "Accessories",
                    },
                    {
                        "name": "Bluetooth Speaker",
                        "image": "https://de.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dwf3572623/JBL_FLIP_ESSENTIAL_2_HERO_36360_x3.png?sw=680&sh=680",
                        "category": "Electronics",
                    },
                    {
                        "name": "Coffee Mug",
                        "image": "https://merchery.co/cdn-cgi/image/width=1440,quality=75,format=auto/cms/uploads/ceramic_mug_orange_eae2bd04b6.png",
                        "category": "Kitchen",
                    },
                    {
                        "name": "Running Shoes",
                        "image": "https://assets.adidas.com/images/h_2000,f_auto,q_auto,fl_lossy,c_fill,g_auto/0a184c1eb3914d40be8a7ef7ef145927_9366/Duramo_Speed_2_Laufschuh_Weiss_IF9392_HM1.jpg",
                        "category": "Footwear",
                    },
                    {
                        "name": "LED Desk Lamp",
                        "image": "https://cdn1.home24.net/images/media/catalog/product/original/jpg/3/8/38da3ebf55684ac3ab29bca954d1c436.webp",
                        "category": "Lighting",
                    },
                    {
                        "name": "Yoga Mat",
                        "image": "https://cdn1.home24.net/images/media/catalog/product/original/jpg/3/8/38da3ebf55684ac3ab29bca954d1c436.webp",
                        "category": "Fitness",
                    },
                    {
                        "name": "Powerbank",
                        "image": "https://flightscopemevo.eu/cdn/shop/files/Anker-Battery-1_80ba7e27-7741-4e24-a953-f33781a99d36.jpg?v=1719820588&width=1800",
                        "category": "Electronics",
                    },
                    {
                        "name": "Laptop Stand",
                        "image": "https://www.ikea.com/de/de/images/products/vattenkar-laptop-monitorstaender-birke__1149392_pe884019_s5.jpg?f=xl",
                        "category": "Office",
                    },
                ]
            for i in range(len(fake_products)):
                product = fake_products[i]
                name = product["name"]
                image = product["image"]
                description = fake.sentence()
                price = fake.random_number(digits=2) + fake.random.random()
                quantity = fake.random_int(min=1, max=100)
                category = product["category"]
                execute_query(
                    conn,
                    add_produtcs_query(),
                    (name, description, price, quantity, category, image),
                )

            shipping_method_ids = fetch_data(conn, get_shipping_method_id_query())
            shipping_method_ids = [row[0] for row in shipping_method_ids]

            for i in range(number_of_orders):
                customer_id = fake.random_int(min=1, max=number_of_customers)
                shipping_method_id = shipping_method_ids[i % len(shipping_method_ids)]
                shipping_address = fake.address().replace("\n", ", ")
                total = 0
                created_at = datetime.datetime.now()
                cancellation_fee = calculate_cancellation_fee(total, 0)
                cur = conn.cursor()
                cur.execute(
                    add_order_query(),
                    (
                        customer_id,
                        shipping_method_id,
                        total,
                        cancellation_fee,
                        shipping_address,
                        created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    ),
                )
                order_id = cur.lastrowid
                for j in range(number_of_order_details):
                    product_id = fake.random_int(min=1, max=number_of_products)
                    price = fake.random_number(digits=2) + fake.random.random()
                    cur.execute(
                        add_order_detail_query(),
                        (order_id, product_id, price),
                    )

            for i in range(10):
                username = fake.user_name()
                password = fake.password()
                email = fake.email()
                role = "admin" if i == 0 else "user"
                execute_query(
                    conn,
                    set_user_query(),
                    (username, password, email, role),
                )
                conn.commit()

            print("Database seeded successfully.")
            conn.close()
            return True
    except Exception as e:
        print(f"Error while seeding database: {e}")
        return False


def create_order(product, quantity, shipping_address, db_path=None):
    try:
        conn = create_connection(db_path)
        if not conn:
            print(f"Could not connect to database at {db_path}")
            return None

        customer_name = "Default"
        customer_email = "customer@example.com"
        customer_phone = "000-000-0000"

        customer_cur = execute_query(
            conn, get_customer_by_email_query(), (customer_email,)
        )
        customer_row = customer_cur.fetchone()

        if customer_row:
            customer_id = customer_row[0]
        else:
            # Create new customer
            customer_cur = execute_query(
                conn,
                add_customer_query(),
                (customer_name, customer_email, customer_phone, shipping_address),
            )
            customer_id = customer_cur.lastrowid

        product_cur = execute_query(conn, get_product_by_name_query(), (product,))
        product_row = product_cur.fetchone()

        if not product_row:
            print(f"Product '{product}' not found in database")
            return None

        product_id = product_row[0]
        product_price = product_row[3]

        available_quantity = product_row[4]
        if available_quantity < quantity:
            print(
                f"Not enough quantity available. Requested: {quantity}, Available: {available_quantity}"
            )
            return None

        total = product_price * quantity

        shipping_cur = execute_query(
            conn, get_shipping_method_id_by_name_query(), ("Standard",)
        )
        shipping_row = shipping_cur.fetchone()
        shipping_method_id = (
            shipping_row[0] if shipping_row else 1
        )  # Default to 1 if not found

        created_at = datetime.datetime.now().isoformat()
        cancellation_fee = 0  # No cancellation fee for new orders

        order_cur = execute_query(
            conn,
            add_order_query(),
            (
                customer_id,
                shipping_method_id,
                total,
                cancellation_fee,
                shipping_address,
                created_at,
            ),
        )
        order_id = order_cur.lastrowid

        execute_query(
            conn, add_order_detail_query(), (order_id, product_id, product_price)
        )

        new_quantity = available_quantity - quantity
        execute_query(conn, update_product_quantity_query(), (new_quantity, product_id))

        conn.commit()
        print(f"Order {order_id} created successfully for {quantity}x {product}")

        return order_id

    except Exception as e:
        print(f"Error while creating order: {e}")
        if conn:
            conn.rollback()
        return None
    finally:
        if conn:
            conn.close()
