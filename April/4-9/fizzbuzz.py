# FizzBuzz input loop:
# Ask user for a number
# Respond with "Fizz", "Buzz", "FizzBuzz" or number
# Loop until they type "exit"
user_input = 0
while user_input != "exit":
    user_input = input("Enter your number (type 'exit' to exit): ")
    if user_input != "exit":
        user_num = int(user_input)
        
        if user_num % 3 == 0 and user_num % 5 == 0:
            print("fizzBuzz")
        elif user_num % 3 == 0:
            print("Fizz")
        elif user_num % 5 == 0:
            print("Fizzbuzz")
        else:
            print(user_input)
    