# find the maximum of three numbers without using max()

def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the largest")
    elif num2 >= num3:
        print(f"{num2} is the largest")
    else:
        print(f"{num3} is the largest")


max_of_three(60, 40, 30)
