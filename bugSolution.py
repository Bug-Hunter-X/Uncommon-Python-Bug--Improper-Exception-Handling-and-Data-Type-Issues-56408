import logging

# Configure basic logging to output to console
logging.basicConfig(level=logging.ERROR)  # Or logging.DEBUG for detailed info

def function_with_improved_error_handling(data):
    try:
        # Check if 'key' exists and if its type is appropriate
        if 'key' not in data or not isinstance(data['key'], (int, float)):
            logging.error("Data missing or of incorrect type")
            return None
        result = data['key'] * 2
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")  # Log detailed exception info
        return None
    return result