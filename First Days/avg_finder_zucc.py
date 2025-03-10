def calculate_average(num_list):
    """Calculates the average of a list of numbers.

    Args:
        num_list: A list of numbers.

    Returns:
        The average of the numbers in the list.  Returns an error message if the list is empty or contains non-numeric values.
    """
    if not num_list:
        return "Null List!!"
    try:
        summ = sum(num_list)
        avg = summ / len(num_list)
        return avg
    except TypeError:
        return "Error: List contains non-numeric values."


original_list = []
while True:
    try:
        input_item = input("Enter a number to add to the list (or type 'done'): ")
        if input_item.lower() == 'done':
            break
        original_list.append(int(input_item))
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

average = calculate_average(original_list)
print(f"The average is: {average}")