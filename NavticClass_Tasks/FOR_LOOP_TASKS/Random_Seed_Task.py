###### SEED FUNCTION ######

import random
random.seed(2)

dice_rolls=[]
for _ in range(5):
    roll= random.randint(1,6)
    dice_rolls.append(roll)
print("dice rolls with seed 42:",dice_rolls)


random.seed(5)
dice_rolls=[]
for _ in range(5):
    roll= random.randint(1,6)
    dice_rolls.append(roll)
print("dice rolls with seed 5:",dice_rolls)

random.seed(7)


dice_rolls=[]
for _ in range(5):
    roll= random.randint(1,6)
    dice_rolls.append(roll)
print("dice rolls with seed 7:",dice_rolls)



######## end using ########

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

######## EXCLUSIVE AND INCLUDING ########

import numpy as np
import random
sd=np.random.seed(0)
x=np.random.randint(1,7 ,size=2)
print(x)
#####example#####
random.seed(0)
x=[]
for i in range(2):
    a=random.randint(1,6)


print(x)


###### YIELD  USING ######
def creator():
    i=1
    while i<=200:
        yield i
        i+=1
print(creator) #creating a generate at memory:
x=creator()
print(next(x))
print(next(x))
print(list(x))


########## CHOICE AND SAMPLE #########
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

