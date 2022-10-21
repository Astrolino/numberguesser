import random
import math
# Let's get inputs here. Start with the lower bound.
lower = int(input("Enter lower number: "))
 
# Take another input here. Now the upper bound.
upper = int(input("Enter upper bound: "))
 
# now we are generating a random number between the lower and upper bound.
x = random.randint(lower, upper)
 
# Init number of guesses.
count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
