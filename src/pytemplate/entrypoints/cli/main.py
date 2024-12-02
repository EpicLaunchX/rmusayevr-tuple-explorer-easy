def get_items():
    """
    Prompts the user to enter a list of items separated by commas.
    Converts the input into a tuple and returns it.
    """
    user_input = input("Enter items separated by commas: ")  # Prompt the user for input
    items_list = user_input.split(",")  # Convert the input string into a list
    items_tuple = tuple(items_list)  # Convert the list into a tuple
    display_tuple(items_tuple)  # Display the tuple
    return items_tuple


def display_tuple(t):
    """
    Takes a tuple as an argument and prints it to the console.
    """
    print("The tuple is:", t)


def access_element(t, index):
    """
    Takes a tuple and an index as arguments, and tries to access the element at the given index.
    Returns the element if the index is valid; otherwise, returns an error message.
    """
    try:
        return t[index]  # Try to access the element
    except IndexError:
        return f"Error: Index {index} is out of range."


def slice_tuple(t, start, end):
    """
    Takes a tuple and two indices (start, end) as arguments and returns the sliced portion.
    If indices are out of range, returns an appropriate message.
    """
    try:
        if start < 0 or end > len(t):
            raise IndexError
        return t[start:end]  # Slice the tuple
    except IndexError:
        return f"Error: Indices [{start}:{end}] are out of range for a tuple of length {len(t)}."
