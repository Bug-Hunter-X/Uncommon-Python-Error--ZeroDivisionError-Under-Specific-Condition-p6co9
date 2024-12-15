def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # Handle the case where a is 0 to avoid ZeroDivisionError
    return a + b