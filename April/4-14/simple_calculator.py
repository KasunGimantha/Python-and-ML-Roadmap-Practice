# Simple Calculator with Error Handling & State Memory

last_result = 0


def check_operator(operator):
    op_list = ['+', '-', '*', '/']
    if operator not in op_list:
        print("Invalid Operator!")
    else:
        return operator


while True:
    try:
        num1 = float(input("Enter value 1: "))
        num2 = float(input("Enter value 2: "))
        operator = input("Enter Operation(+,-,*,/): ")
        check_operator(operator)
        break
    except ValueError:
        print("Enter Numerical value for both!")


def operations(num1, num2, operator):

    try:
        global last_result

        def addition():
            return num1+num2

        def substraction():
            return num1-num2

        def multiplication():
            return num1*num2

        def division():
            try:
                result = num1/num2
                return result
            except ZeroDivisionError as e:
                print(f"Error occured: {e}")

        if operator == '+':
            last_result = addition()
        elif operator == '-':
            last_result = substraction()
        elif operator == '*':
            last_result = multiplication()
        elif operator == '/':
            last_result = division()
        return last_result
    except Exception as e:
        print(f'Error occured:{e}')


operation1 = operations(num1, num2, operator)
print(operation1)
