# Foster Higginbotham's File.
# This assignment will demonstrate the ability to write and apply python code that can play a random guessing game.

#import our random function for our random number
import random

#range for our random number
number = random.randrange(1,100)

#variables for counting and printing purposes
attempts = 0 
guess = 0
highcounter = 0

#if guess does not equal our random number AND our highcounter doesnt equal 4 then go through the loop
while guess != number and highcounter != 4:
    guess = int(input("Please guess a number between 1 and 100 please: "))
#count our attempts
    attempts = attempts + 1
#if guess equals number 
    if guess == number:
        print ("Congrats, you guessed the number correctly after", attempts, "attempts!, of which", highcounter, "were too high.")
#when guess is greater then our random number 
    elif guess > number:
#add to our counter for guesses over our random number
        highcounter = highcounter + 1
#if our highcounter hits 4 then we
        if highcounter == 4:
            print("Sorry you lost by making too many high guesses. The correct number was", number)
        else:
            print("Your guess is too high. You have made ", highcounter,"guesses that were too high.")
#when guess is less then our random number
    elif guess < number:
        print ("Your guess is too low.")
    

