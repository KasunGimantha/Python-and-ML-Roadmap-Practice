import random

secret_number = random.randint(1, 100)# Generate Random number between 1-100

# intialize the number of guesses to zero at the begining
guess_count = 0
while True:

    guess_num = input("Enter Number(0-100): ") #get user input
    
    if guess_num.isdigit():#check input is number or not
        
        guess_num = int(guess_num) #convert input into numeric value
        
        if guess_num>=0 and guess_num <=100: #check value between 0-100
         if guess_num == secret_number:
          print("Congrats!!")
          break
         elif guess_num > secret_number:
          print("Too Large")
          
         elif guess_num < secret_number:
          print("Too Low")   
        else:
            print("Enter Number Between 0 and 100!!!")
             
    else:
        print("Enter Numeric Vlaue!!")
        
    guess_count = guess_count+1    #calculating how many times loop runs
                           
print("Took ",guess_count," guesses to win!!")     
        
       














# while True:

#     first_number = input("Enter Your Guessing number (0-100): ")
#     try:   
#     if math.isnan(first_number):
#         print("Enter Numeric value!!!")
#     except ValueError
    
        
#     elif first_number<=100 and first_number>=0:  
#         #input_number = int(first_number)
        
#         if (first_number > secret_number):
#             print("Your guess is too high")
#         elif (first_number < secret_number):
#             print("Your guess is too low")
#         elif (first_number == secret_number):
#             print("Your guess is correct!! Congradulations")
#             break
#         num_guesses = num_guesses+1


# print("You get total of ", num_guesses, "to complete game.")


# Write a Python program that does the following:

# Generates a random number: The program should generate a random integer between 1 and 100 (inclusive). You'll need the random module for this.

# Prompts the user for guesses: The program should repeatedly prompt the user to guess the number.

# Provides feedback: After each guess, the program should tell the user whether their guess was too high, too low, or correct.

# Keeps track of guesses: The program should count the number of guesses the user takes.

# Ends the game: The game should end when the user guesses the correct number, displaying the total number of guesses it took.
