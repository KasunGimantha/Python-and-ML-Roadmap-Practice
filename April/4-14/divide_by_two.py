# A function that takes two numbers, divides them, and handles ZeroDivisionError with a proper message.


def divide_by_two(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError as e:
        print(f"can't divide by zero : {e} error")
        return None


operation1 = divide_by_two(5, 0)
print(operation1)
