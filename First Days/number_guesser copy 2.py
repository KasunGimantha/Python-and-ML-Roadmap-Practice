import random

def guess_number(secret_number, guess_count):
    guess_num = input("Enter Number (0-100): ")  # Get user input

    if not guess_num.isdigit():  # Ensure input is a number
        print("Enter a Numeric Value!!")
        return guess_count  # No increment for invalid input

    guess_num = int(guess_num)

    if not (0 <= guess_num <= 100):  # Ensure number is in range
        print("Enter a Number Between 0 and 100!!!")
        return guess_count

    guess_count += 1  # Valid guess, so increment count

    if guess_num == secret_number:
        print(f"Congrats!! You took {guess_count} guesses to win.")
        return -1  # Break signal

    print("Too Low" if guess_num < secret_number else "Too Large")
    return guess_count  # Return updated count

# Generate Random number
secret_number = random.randint(1, 100)
guess_count = 0 

while True:
    guess_count = guess_number(secret_number, guess_count)
    if guess_count == -1:
        break
