#import random grants you access to a few functions in python
#rand.int being one of them.
import random

#function for the computer to guess

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        #if low == high, the guess must be low (or high, since they are the same)
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  #or high, since they are the same
        
        #get feedback from the user
        feedback = input(f"Is {guess} H (high), L (low) or C (correct)? ").lower()
        
        if feedback == "h":
            high = guess - 1  #reduce the upper bound
        elif feedback == "l":
            low = guess + 1  #increase the lower bound
        elif feedback != "c":
            print("Please enter H, L, or C.")

    print(f"The computer guessed your number! {guess} was your desired number.")

#calling the function with a defined range
computer_guess(10)
