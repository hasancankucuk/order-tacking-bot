import os
from datetime import datetime
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker  # type: ignore
from rasa_sdk.executor import CollectingDispatcher  # type: ignore
from backend.db.methods import (
    get_shipping_method_id_by_name,
    update_order_status,
    update_shipping_method,
)


from backend.helpers.decorators import with_validated_db
from backend.helpers.order_validate import get_validated_order


class ActionChangeOrder(Action):
    def name(self) -> Text:
        return "action_change_order"

    @with_validated_db
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        db_path,
    ) -> List[Dict[Text, Any]]:
        order_id = tracker.get_slot("order_id")
        shipping_method = tracker.get_slot("shipping_method")

        if not db_path:
            return []

        if order_id and shipping_method:
            try:
                changed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                cur = get_shipping_method_id_by_name(shipping_method, db_path)
                print("cur" + str(cur))
                if cur is not None:
                    update_shipping_method(order_id, cur, changed_at, db_path)
                    update_order_status(order_id, "changed", db_path)
                    dispatcher.utter_message(
                        text=f"The order {order_id} has been changed to {shipping_method}."
                    )
            except Exception as e:
                dispatcher.utter_message(
                    text=f"An error occurred while processing the order change: {e}"
                )
                return []
