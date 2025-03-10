import random

secret_number = random.randint(1, 100) # Generate Random number between 1-100

guess_count = 0 
# intialize the number of guesses to zero at the begining
while True:
    def loop_part():
        global guess_count  #declare guess_count in global scope becuase it need to access outside from function  
        guess_num = input("Enter Number(0-100): ")  # get user input
        
        if not guess_num.isdigit():  # check input is number or not
            print("Enter Numeric Vlaue!!")
            return
        guess_num = int(guess_num)  # convert input into numeric valu

        if not guess_num < 0 and guess_num > 100:  # check value is not between 0-100
            print("Enter Number Between 0 and 100!!!")
            return

        if not guess_num == secret_number: #check the value is not equal to genrated number
            
            guess_count = guess_count +1 # iterate guessing count by one
            if not guess_num > secret_number: # check number is larger than random number
                print("Too low")               
                return
            print("Too large")           
            return
        print("Congrats!!")
        print("You took ", guess_count, "Guesses to win") #final statement       
        exit() # exit the function
        return

    loop_part() #declare main iterative function

    
