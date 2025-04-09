#highLow.py

#import libraries
import random

isWrong = True
number = random.randint(1,100)
tries = 1

print("I'm thinking of a number between 1 and 100. Guess a number, and I'll tell you if you're too high, too low, or got it right. Good luck!")

while isWrong:
    guess = input("{}) Please enter a number ".format(tries))
    guess = int(guess)
    if guess == number:
        isWrong = False
        print("Correct!")
        print("It took {} turns.".format(tries))
    elif guess < number:
        print("Too low!")
        tries += 1
    elif guess > number:
        print("Too high!")
        tries += 1