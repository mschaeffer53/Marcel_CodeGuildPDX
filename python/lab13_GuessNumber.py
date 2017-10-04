'''
Lab 13 - Guess the Number
Marcel Schaeffer
10/4/17
'''

import random

#computer picks random int
x = random.randint(1,10)

pick = 0
i = 0

#user enters picks
while i < 10 and pick != x:
    pick = int(input('Pick an integer between 1-10: '))
    i = i + 1
if pick == x:
    print('You guessed correctly!')

if pick != x:
    print('You lose')