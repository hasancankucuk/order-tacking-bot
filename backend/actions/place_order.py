from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker  # type: ignore
from rasa_sdk.executor import CollectingDispatcher  # type: ignore
from rasa_sdk.events import SlotSet

from backend.helpers.decorators import with_validated_db
from backend.db.methods import create_order, get_all_products

from dotenv import load_dotenv
import os

load_dotenv()

class ActionPlaceOrder(Action):
    def name(self) -> Text:
        return "action_place_order"

    @with_validated_db
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        db_path
    ) -> List[Dict[Text, Any]]:

        product = tracker.get_slot("product")
        quantity = tracker.get_slot("quantity")
        shipping_address = tracker.get_slot("new_address") or tracker.get_slot("address")

        if not product:
            dispatcher.utter_message(text="I need to know which product you want to order.")
            return []
        
        if not shipping_address:
            dispatcher.utter_message(text="I need a shipping address to place your order.")
            return []

        try:
            if not quantity:
                quantity_int = 1
            else:
                text_to_number = {
                    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
                }
                
                if str(quantity).lower() in text_to_number:
                    quantity_int = text_to_number[str(quantity).lower()]
                else:
                    quantity_int = int(quantity)
            
            if quantity_int <= 0:
                dispatcher.utter_message(text="Quantity must be a positive number.")
                return []

            all_products = get_all_products(db_path)
            matched_product = None
            
            for prod in all_products:
                if prod['name'].lower() == product.lower():
                    matched_product = prod['name']
                    break
            
            if not matched_product:
                for prod in all_products:
                    if product.lower() in prod['name'].lower() or prod['name'].lower() in product.lower():
                        matched_product = prod['name']
                        break
            
            if not matched_product:
                product_names = [prod['name'] for prod in all_products[:5]]  # Show first 5
                dispatcher.utter_message(
                    text=f"Sorry, I couldn't find '{product}'. Available products include: {', '.join(product_names)}"
                )
                return []

            order_id = create_order(
                product=matched_product,
                quantity=quantity_int,
                shipping_address=shipping_address,
                db_path=db_path
            )

            if order_id:
                dispatcher.utter_message(
                    text=f"Your order (ID: {order_id}) for {quantity_int} x {matched_product} has been placed successfully! It will be shipped to: {shipping_address}"
                )
                return [SlotSet("order_id", str(order_id))]
            else:
                dispatcher.utter_message(
                    text=f"Failed to place your order. This could be due to insufficient stock or a database error."
                )
                return []

        except ValueError:
            dispatcher.utter_message(text="Quantity must be a valid number.")
            return []
        except Exception as e:
            dispatcher.utter_message(
                text=f"Failed to place your order due to an error: {str(e)}"
            )
            return []