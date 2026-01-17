def calculate_average_order_value(orders):
    if not orders:
        return 0.0

    total = 0.0
    valid_count = 0

    for order in orders:
        # Check if keys exist to avoid KeyError, though usually we might expect consistent data structure.
        # Assuming standard dict structure based on original code usage.
        # We also treat missing status as 'valid' or strictly require it? 
        # The original code crashed if key missing. I'll add safety.
        status = order.get("status")
        amount = order.get("amount")
        
        if status != "cancelled" and isinstance(amount, (int, float)):
            total += amount
            valid_count += 1

    if valid_count == 0:
        return 0.0

    return total / valid_count
