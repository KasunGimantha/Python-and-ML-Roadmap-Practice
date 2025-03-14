def custom_num_process():
    while True:

        # get input from user
        input_num = input("Enter Number list seperated by spaces: ").split()

        if all(x.isdigit() for x in input_num):  # check numbers are numeric or not
            int_list = [int(x) for x in input_num]
            break
        else:
            print("Enter Numeric Value!!")

    def even_of_list(int_list):  # function to get even numers in list
        list_even = [x for x in int_list if x % 2 == 0]
        print(f"even: {list_even}")

    def odd_of_list(int_list):  # function to get odd numbers from list
        list_odd = [x for x in int_list if x % 2 != 0]
        print(f"odd: {list_odd}")

    def sum_of_list(int_list):  # function to get sum of list
        list_sum = sum(int_list)
        print(f"sum: {list_sum}")

    def square_of_list(int_list):  # function to turn numbers in list to square
        list_square = [x**2 for x in int_list]
        print(f"squared: {list_square}")

    even_of_list(int_list)  # calling  even,odd,sum,squared functions
    odd_of_list(int_list)
    sum_of_list(int_list)
    square_of_list(int_list)


custom_num_process()  # calling main function
