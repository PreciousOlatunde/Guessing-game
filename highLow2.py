#highLow2.py

#import library
import random

print("Please think of a number between 1 and 100. I'll guess your number. You tell me if I'm too high, too low, or correct.")

guess = random.randint(1,100)
low = 0
high = 100
answer = ""
tries = 1
isWrong = True

while isWrong:
    print("I guess: {}".format(guess))
    print("too (h)igh, too (l)ow, or (c)orrect?")
    answer = input("")
    answer = answer.lower()

    if answer == "c":
        print("I got it! It took me {} turns.".format(tries))
        isWrong = False
    elif answer == "h":
        high = guess - 1
        guess = random.randint(low, high)
        tries += 1
    elif answer == "l":
        low = guess + 1
        guess = random.randint(low, high)
        tries += 1
    else:
        print("Sorry, I didn't understand you...")
