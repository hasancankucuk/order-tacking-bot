import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker # type: ignore
from rasa_sdk.executor import CollectingDispatcher # type: ignore
from backend.db.methods import get_order_by_id, update_order_status
from backend.helpers.order_validate import get_validated_order
from backend.helpers.decorators import with_validated_db

class ActionCancelOrder(Action):
    def name(self) -> Text:
        return "action_cancel_order"
    
    @with_validated_db
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], db_path) -> List[Dict[Text, Any]]:

        order_id = tracker.get_slot("order_id")
        if order_id:
            try:
                if order_id is not None:
                    row = get_order_by_id(order_id, db_path)
                    if row:
                        if update_order_status(order_id, "cancelled", db_path):
                            dispatcher.utter_message(text=f"The order with ID {order_id} has been cancelled.")
                        else:
                            dispatcher.utter_message(text=f"Failed to cancel order with ID {order_id}.")
                    else:
                        dispatcher.utter_message(text=f"Order with ID {order_id} not found.")
                else:
                    dispatcher.utter_message(text=f"Order with ID {order_id} is not valid.")
            except Exception as e:
                dispatcher.utter_message(text=f"An error occurred while processing the order cancellation: {e}")
                return []
        return []
