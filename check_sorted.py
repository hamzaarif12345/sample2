def check_sorted(values_str):
    # Split the input string by commas and strip whitespace
    items = [item.strip() for item in values_str.split(',') if item.strip()]
    
    # Check if the list is empty or has only one element
    if len(items) <= 1:
        return True
    
    # Try to convert to numbers (integers or floats)
    try:
        # First try integers
        numeric_items = [int(item) for item in items]
    except ValueError:
        try:
            # If integer conversion fails, try floats
            numeric_items = [float(item) for item in items]
        except ValueError:
            # If both fail, treat as strings
            numeric_items = items
    
    # Check if the list is sorted in non-decreasing order
    for i in range(len(numeric_items) - 1):
        if numeric_items[i] > numeric_items[i + 1]:
            return False
    
    return True

# Get input from user
user_input = input("Enter comma-separated values: ")

# Check if sorted and print result
result = check_sorted(user_input)
print(result)