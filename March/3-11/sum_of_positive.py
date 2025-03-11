def list_of_positive(number_list):  # declare main function
    sum_of_num = 0

    for x in number_list:  # loop through list
        try:
            if x > 0:  # check number is positive
                sum_of_num += x  # store sums of positive numbers in list
        except TypeError:  # raise error if string value inserted
            print("Excluded Strings: ", x)

    return sum_of_num  # returning sum

# initializing lists


my_list1 = [6, 0, 8, -2, 0, -8]

final_list1 = list_of_positive(my_list1)

print(final_list1)

my_list2 = [1, "a", 4, -2, "water", -8]

final_list2 = list_of_positive(my_list2)
print(final_list2)
