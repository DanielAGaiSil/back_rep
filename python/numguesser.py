import random

def guess (x):
    random_num = random.randint(1, x)
    guess = 0 
    while  (guess != random_num):
        guess = int (input (f"Guess a number between 1 and {x}: "))
        print(guess)
        
        if (guess < random_num):
            print("Guess again, too low.")
        elif guess > random_num:
            print("Guess again, too high.")
    print(f"Congratulations, right guess. {random_num} was the right one.")

guess(10)
