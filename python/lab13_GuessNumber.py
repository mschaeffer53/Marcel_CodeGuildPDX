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
while i < 10:
    pick = int(input('Pick an integer between 1-10: '))
    if pick == x:
        print('you win')
        break
    if pick > x:
        print('too high')
    else:
        print('too low')
    i += 1


if pick != x:
    print('You lose')