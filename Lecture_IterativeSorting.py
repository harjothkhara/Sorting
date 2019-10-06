import math
import random
import time
from datetime import datetime

animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark',
           'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

###########
# 0(1) - constant time operation
###########

# return the name of all animals -


def getAnimals():  # constant time operation - doesn't matter if its a long or small list
    return animals  # returning a pointer to the start of our list


# time complexity is 0(1) operation - performance stays constant as inputs get larger
print(getAnimals())


###########
# 0(n) - linear - straight line. as you add more inputs the performance wil increase linearly. always drop constant coefficents.
###########

# Return the number of animals


def countAnimals():
    num_animals = 0
    for animal in animals:
        print(f"num animals: {num_animals}")
        num_animals += 1
    return num_animals
# how many operations are we doing? doing this operation 10 times. our input is size n, and for each of these inputs we need to do something, which is incrementing our counter by 1. if we had 20 animals, 1000 animals we would need to do it whatever n amount of times. the number of operations we need to do it linear.


print(countAnimals())
