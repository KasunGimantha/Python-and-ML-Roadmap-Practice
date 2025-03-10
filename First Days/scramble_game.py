import random
word_list = ["python", "java", "ruby", "apple",
             "orange"]  # declare list of random words
random_pick = word_list[random.randint(0, 4)]  # pick a random word from list
shuffled_word = ''.join(random.sample(
    random_pick, len(random_pick)))  # shuffle choosen word
guess_count = 0  # inirialize guess count to 0

print("Scrambled Word: ", shuffled_word)  # show user scrambled word


def word_shuffle(random_pick, guess_count):  # declare method
    while True:
        user_word = input("Your Guess: ")  # ask user for input

        if not user_word.isdigit():  # check whether the input is digit or not
            guess_count = + 1
            if not user_word == random_pick:  # check user word equal to picked word

                print("Try Again")
                return
            print("Correct! You guessed it in ", guess_count, " attempt")
            return -1
        print("Enter a Word!!")


while True:  # loop the method
    final_result = word_shuffle(random_pick, guess_count)
    if final_result == -1:
        break
