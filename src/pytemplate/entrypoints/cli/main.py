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
