def get_validated_order (dispatcher, entity):
    try:
        order_id = int(entity)
        return order_id
    except Exception:
        dispatcher.utter_message(text=f"Order id '{entity}' is not valid. Please provide a numeric order ID.")
        return []