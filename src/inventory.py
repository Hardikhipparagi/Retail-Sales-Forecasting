import numpy as np

def inventory_policy(predictions, on_hand=50):

    # Convert to numpy array (safe)
    predictions = np.array(predictions)

    demand = np.mean(predictions)
    std = np.std(predictions)

    # Safety Stock
    safety_stock = 1.65 * std

    # Reorder Point
    reorder_point = demand + safety_stock

    # EOQ
    annual_demand = demand * 365
    ordering_cost = 500
    holding_cost = 2

    eoq = ((2 * annual_demand * ordering_cost) / holding_cost) ** 0.5

    # Order Quantity
    order_qty = max(0, max(eoq, reorder_point - on_hand))

    return {
        "demand": demand,
        "safety_stock": safety_stock,
        "reorder_point": reorder_point,
        "eoq": eoq,
        "order_quantity": order_qty
    }