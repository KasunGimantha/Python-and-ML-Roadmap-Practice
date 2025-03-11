# filter out even numbers from a list
def even_list(my_list):  # declare function
    new_list = []
    for x in my_list:  # looping through list
        if x % 2 == 0:  # check condition
            new_list.append(x)

    return new_list


my_list = [3, 4, 1, 6, 7, 8]  # initialize list
filtered_list = even_list(my_list)
print(filtered_list)
