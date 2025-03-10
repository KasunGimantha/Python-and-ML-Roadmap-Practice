import random

# List of words
word_list = ["python", "java", "ruby", "apple", "orange"]

# Pick a random word
random_pick = random.choice(word_list)

# Shuffle the word
shuffled_word = ''.join(random.sample(random_pick, len(random_pick)))

print("Scrambled Word:", shuffled_word)


def word_shuffle(random_pick):
    guess_count = 0  # Initialize guess count

    while True:
        # Take input & clean it
        user_word = input("Your Guess: ").strip().lower()

        if not user_word.isalpha():  # Ensure input is a word (not numbers)
            print("Enter a valid word!")
            continue  # Ask again

        guess_count += 1  # Increase attempt count

        if user_word == random_pick:  # Check if the guess is correct
            print(f"Correct! You guessed it in {guess_count} attempts.")
            break  # Exit loop
        else:
            print("Try Again!")


# Run the function
word_shuffle(random_pick)
