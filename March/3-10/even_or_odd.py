
while True:
    # get input from user
    input_number = input("Enter Number to check if it even or odd:")
    try:
        # convert string input to int
        input_number = int(input_number)
        break
    # throw exception if enter numeric value
    except ValueError:
        print("Enter Numeric Value!!")

# check odd or even
if input_number % 2 == 0:
    print("Even number")
else:
    print("Odd Number")
