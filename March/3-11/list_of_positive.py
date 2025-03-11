def list_of_positive(number_list):
    positive_list = []

    for x in number_list:
        try:
            if x > 0:
                positive_list.append(x)
        except TypeError:
            print("Excluded Strings: ", x)
    return positive_list


my_list1 = [6, 0, 8, -2, 0, -8]

final_list1 = list_of_positive(my_list1)
print(final_list1)

my_list2 = [1, "a", 4, -2, "water", -8]

final_list2 = list_of_positive(my_list2)
print(final_list2)
