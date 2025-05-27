import os
from dotenv import load_dotenv  # type: ignore
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker  # type: ignore
from rasa_sdk.executor import CollectingDispatcher  # type: ignore


from backend.helpers.order_validate import get_validated_order
from backend.helpers.decorators import with_validated_db
from backend.db.methods import get_customer_id_by_order_id, update_shipping_address


class ActionChangeShippingAddress(Action):
    def name(self) -> Text:
        return "action_change_shipping_address"

    @with_validated_db
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        db_path,
    ) -> List[Dict[Text, Any]]:
        order_id = tracker.get_slot("order_id")
        new_address = tracker.get_slot("new_address")

        if order_id and new_address:
            try:
                row = get_customer_id_by_order_id(order_id, db_path)
                if row:
                    update_shipping_address(order_id, new_address, db_path)
                    dispatcher.utter_message(
                        text=f"The shipping address for order {order_id} has been changed to {new_address}."
                    )
            except Exception as e:
                dispatcher.utter_message(
                    text=f"An error occurred while updating the address: {e}"
                )
        return []
