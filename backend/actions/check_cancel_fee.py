import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker # type: ignore
from rasa_sdk.executor import CollectingDispatcher # type: ignore

from backend.helpers.decorators import with_validated_db
from backend.helpers.order_validate import get_validated_order
from backend.db.methods import get_cancellation_fee


class ActionCheckCancelFee(Action):
    def name(self) -> Text:
        return "action_check_cancel_fee"

    @with_validated_db
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        db_path,
    ) -> List[Dict[Text, Any]]:

        entity = tracker.get_slot("entity")

        if entity:
            try:
                order_id = get_validated_order(dispatcher, entity)
                if order_id is not None:
                    cancel_fee = get_cancellation_fee(order_id, db_path)
                    if cancel_fee is not None:
                        dispatcher.utter_message(
                            text=f"The cancellation fee for order {order_id} is {cancel_fee}."
                        )
                    else:
                        dispatcher.utter_message(
                            text=f"No cancellation fee found for order {order_id}."
                        )
            except Exception as e:
                dispatcher.utter_message(
                    text=f"An error occurred while checking the cancellation fee: {e}"
                )
                return []
