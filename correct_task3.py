def average_valid_measurements(values):
    if not values:
        return 0.0

    total = 0.0
    valid_count = 0

    for v in values:
        if v is None:
            continue
            
        try:
            # Attempt to convert to float. 
            # This handles integers, float numbers, and numeric strings (e.g., "12.5").
            numeric_value = float(v)
            total += numeric_value
            valid_count += 1
        except (ValueError, TypeError):
            # Ignore values that cannot be converted to a number
            continue

    if valid_count == 0:
        return 0.0

    return total / valid_count