# this module contains the rng generator
import random

random.random

# input
guess = int(input("Guess a number from 0 to 9! "))
print("")

# process
n = random.randint(0, 9)

# output

print("")
if n == guess:
    print("You guessed correctly!")
else:

    print("You guessed incorrectly")
    print("")
    print("The correct number was {}!".format(n))
