import os
from typing import Optional, Tuple
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user= os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host="db",
        port=os.getenv("DB_PORT")
    )


def get_invoice(order_id: str) -> Optional[str]:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT invoice FROM orders WHERE order_id = %s", (order_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    except psycopg2.Error as e:
        print(f"DB error: {e}")
        return None

def check_cancel_fee(order_id: str) -> Optional[str]:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT cancel_fee FROM orders WHERE order_id = %s", (order_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    except psycopg2.Error as e:
        print(f"DB error: {e}")
        return None

def change_order_status(order_id: str, new_status: str) -> bool:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE orders SET status = %s WHERE order_id = %s",
            (new_status, order_id),
        )
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except psycopg2.Error as e:
        print(f"DB error: {e}")
        return False
    
def cancel_order(order_id: str) -> bool:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE orders SET status = 'CANCELLED' WHERE order_id = %s",
            (order_id,),
        )
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except psycopg2.Error as e:
        print(f"DB error: {e}")
        return False

def change_shipping_address(order_id: str, new_address: str) -> bool:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE orders SET shipping_address = %s WHERE order_id = %s",
            (new_address, order_id),
        )
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except psycopg2.Error as e:
        print(f"DB error: {e}")
        return False

def get_order_status(order_id: str) -> Optional[Tuple[str, str]]:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT status, estimated_delivery FROM orders WHERE order_id = %s",
            (order_id,),
        )
        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as e:
        print(f"DB error: {e}")
        return None
