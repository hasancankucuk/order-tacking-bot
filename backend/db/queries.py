def delete_database_query():
    return "DROP TABLE IF EXISTS {};"


def drop_all_tables_query():
    return """
    PRAGMA foreign_keys = OFF;
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS order_details;
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS shipping_methods;
    DROP TABLE IF EXISTS products;
    DROP TABLE IF EXISTS customers;
    PRAGMA foreign_keys = ON;
    """


def get_order_by_id_query():
    return "SELECT id FROM orders WHERE id = ?;"


def get_customer_id_by_order_id_query():
    return "SELECT customer_id FROM orders WHERE id = ?;"


def get_shipping_method_id_by_name_query():
    return "SELECT id FROM shipping_methods WHERE name = ?;"


def get_cancellation_fee_query():
    return "SELECT cancellation_fee FROM orders WHERE id = ?;"


def get_invoice_query():
    return """
        SELECT orders.id AS order_id, 
               orders.shipping_address AS shipping_address,
               customers.name AS customer_name,
               shipping_methods.name AS shipping_method, 
               orders.status, 
               orders.cancellation_fee,
               orders.total,
               GROUP_CONCAT(products.name || ' (Price: $' || order_details.price || ')') AS ordered_items
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        JOIN shipping_methods ON orders.shipping_method_id = shipping_methods.id
        JOIN order_details ON orders.id = order_details.order_id
        JOIN products ON order_details.product_id = products.id
        WHERE orders.id = ?
        GROUP BY orders.id, orders.shipping_address, customers.name, 
                 shipping_methods.name, orders.status, orders.cancellation_fee, orders.total;
    """


def get_tables_query():
    return "SELECT name from sqlite_master WHERE type='table';"


def get_all_customers_query():
    return "SELECT * FROM customers;"


def get_all_products_query():
    return "SELECT * FROM products;"


def get_all_orders_query():
    return """
        SELECT orders.id, customers.name AS customer_name, 
               shipping_methods.name AS shipping_method, 
               orders.status, orders.total
        FROM orders
        JOIN customers ON orders.customer_id = customers.id
        JOIN shipping_methods ON orders.shipping_method_id = shipping_methods.id;
    """


def get_all_order_details_query():
    return """
        SELECT order_details.id, orders.id AS order_id, 
               products.name AS product_name, order_details.price
        FROM order_details
        JOIN orders ON order_details.order_id = orders.id
        JOIN products ON order_details.product_id = products.id;
    """


def get_all_shipping_methods_query():
    return "SELECT * FROM shipping_methods;"


def get_all_from_table_query(table_name):
    return f"SELECT * FROM {table_name};"


def get_user_query():
    return "SELECT * FROM users WHERE username = ? AND password = ?;"


def get_shipping_method_id_query():
    return "SELECT id FROM shipping_methods;"


def set_user_query():
    return "INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?);"


def update_user_query():
    return "UPDATE users SET password = ?, email = ? , role = ?, username = ? WHERE id = ?;"


def update_order_status_query():
    return "UPDATE orders SET status = ?, changed_at = ? WHERE id = ?;"


def update_shipping_address_query():
    return " UPDATE orders  SET shipping_address = ?  WHERE id = ?;"


def update_shipping_method_query():
    return "UPDATE orders SET changed_at = ?, shipping_method_id = ? WHERE id = ?;"


def add_order_query():
    return """
        INSERT INTO orders (customer_id, shipping_method_id, total, cancellation_fee, shipping_address, created_at)
        VALUES (?, ?, ?, ?, ?, ?);
    """


def add_order_detail_query():
    return "INSERT INTO order_details (order_id, product_id, price) VALUES (?, ?, ?);"


def add_produtcs_query():
    return "INSERT INTO products (name, description, price, quantity, category, image) VALUES (?, ?, ?, ?, ?, ?);"


def add_customer_query():
    return "INSERT INTO customers (name, email, phone, address) VALUES (?, ?, ?, ?);"


def add_new_shipping_method_query():
    return "INSERT INTO shipping_methods (name) VALUES (?);"


def get_customer_by_email_query():
    return "SELECT id, name, email, phone, address FROM customers WHERE email = ?;"


def get_product_by_name_query():
    return "SELECT id, name, description, price, quantity, category FROM products WHERE name = ?;"


def update_product_quantity_query():
    return "UPDATE products SET quantity = ? WHERE id = ?;"
