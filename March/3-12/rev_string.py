
# ignore spaces while reversing the string.
def reverse_string(input_string):  # initializing function
    # collect non-space characters
    characters = [c for c in input_string if c != ' ']
    reverse_string = characters[::-1]  # reversed the collected characters

    return ''.join(reverse_string)


print(reverse_string("Hello World"))  # declaring function
