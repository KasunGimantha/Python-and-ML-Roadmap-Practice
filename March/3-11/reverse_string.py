# reverses a string without using [::-1] or reversed()

def reverse_string(input_string):  # intializing function
    char_list = []
    popped_list = []  # creating empty lists to store appended items
    z = len(input_string)  # storing length of the string

    for x in range(z):
        # appending all characters in input string seperately into a list named char_list
        char_list.append(input_string[x:x+1])

    for x in range(z):
        # popping out every character in char_list to store characters reverse order in popped_list
        popped_list.append(char_list.pop())

    # join characters into one string in popped_list
    return "".join(popped_list)


word = "Kasun"

final_string = reverse_string(word)
print(final_string)
