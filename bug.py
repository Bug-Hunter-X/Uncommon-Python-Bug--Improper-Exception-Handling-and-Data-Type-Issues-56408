def function_with_uncommon_error(data):
    try:
        # Simulate a scenario where the data might be missing or of the wrong type
        result = data['key'] * 2
    except (KeyError, TypeError) as e:
        # Handle the exception appropriately and log the error. Do not simply swallow the exception.
        print(f"An error occurred: {e}")
        return None # or raise the exception for better error handling
    return result