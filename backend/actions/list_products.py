from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker  # type: ignore
from rasa_sdk.executor import CollectingDispatcher  # type: ignore
from backend.db.methods import get_all_products
from backend.helpers.decorators import with_validated_db


class ActionListProducts(Action):
    def name(self) -> Text:
        return "action_list_products"

    @with_validated_db
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        db_path,
    ) -> List[Dict[Text, Any]]:
        
        if not db_path:
            dispatcher.utter_message(text="Database path is not valid.")
            return []

        try:
            products = get_all_products(db_path)
            if products:
                products_text = "Available Products:"
                for i, product in enumerate(products, 1):
                    products_text += f"\n\n**{i}. {product['name']}**"
                    products_text += f"\nPrice: ${product['price']:.2f}"
                    products_text += f"\nStock: {product.get('quantity', 'N/A')} available"
                    if product.get('description'):
                        products_text += f"\nDescription: {product['description']}"
                    products_text += "\n"
                    image = product.get('image')
                    dispatcher.utter_message(
                        text=products_text,
                        image=image if image else None
                    )
            else:
                dispatcher.utter_message(text="No products are currently available in our inventory.")
                
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred while retrieving products: {e}")
        
        return []