from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker  # type: ignore
from rasa_sdk.executor import CollectingDispatcher  # type: ignore
from backend.helpers.decorators import with_validated_db
from backend.helpers.order_validate import get_validated_order
from backend.helpers.invoice_generator import invoice_generator
from backend.db.methods import get_invoice

from dotenv import load_dotenv
import os

load_dotenv()


class ActionCheckInvoice(Action):
    def name(self) -> Text:
        return "action_retrieve_invoice"

    @with_validated_db
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        db_path,
    ) -> List[Dict[Text, Any]]:

        order_id = tracker.get_slot("order_id")
        if order_id:
            try:
                invoice_info = get_invoice(order_id, db_path)
                if invoice_info:

                    invoice_path = invoice_generator(invoice_info)
                    backend_url = os.getenv('process.env.REACT_APP_BACKEND_URL')
                    filename = invoice_path.replace('invoice/', '')
                    pdf_url = f"{backend_url}/invoice/{filename}"
                    print(f"Generated PDF URL: {pdf_url}")
                    dispatcher.utter_message(
                        text="Here is your invoice:", custom={"pdf_url": pdf_url}
                    )
                else:
                    dispatcher.utter_message(
                        text=f"No invoice found for order {order_id}."
                    )
            except Exception as e:
                dispatcher.utter_message(
                    text=f"An error occurred while retrieving the invoice: {e}"
                )
                return []
