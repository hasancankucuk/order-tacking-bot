def calculate_cancellation_fee(order_total: float, hours_since_order: float) -> float:
    if hours_since_order < 1:
        return 0.0 

    elif hours_since_order <= 24:
        return round(order_total * 0.1, 2)

    else:
        return round(order_total * 0.25, 2)