#Import random grants you access to a few functions in python
#rand.int being one of them.
import random

#Function to guess

def guess (x):
    random_num = random.randint(1, x)
    guess = 0 
    while  (guess != random_num):
        #Let's you define the range
        guess = int (input (f"Guess a number between 1 and {x}: "))
        print(guess)
        
        if (guess < random_num):
            print("Guess again, too low.")
        elif guess > random_num:
            print("Guess again, too high.")
    
    print(f"Congratulations, right guess. {random_num} was the right one.")

#Calling the function with a defined range
guess(10)
