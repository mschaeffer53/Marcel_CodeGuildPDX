'''
Lab 8 - Rock Paper Scissors
Marcel Schaeffer
10/4/17
'''

import random

list = ['rock', 'paper', 'scissors']

auto = random.choice(list) #copmuter generates a throw
pick = input('Type one: rock, paper, scissors: \n') #user types their throw
print('computer throws ' + auto)
print('you threw ' + pick)

#this prints the winner of all of the scenarios

if pick == auto:
    print("Tie")
elif pick == 'rock' and auto == 'paper':
    print('paper covers rock')
elif pick == 'rock' and auto == 'scissors':
    print('rock smashes scissors')
elif pick == 'paper' and auto == 'scissors':
    print('scissors cuts paper')
elif pick == 'paper' and auto == 'rock':
    print('paper covers rock')
elif pick == 'scissors' and auto == 'rock':
    print('rock crushes scissors')
elif pick == 'scissors' and auto == 'paper':
    print('scissors cuts paper')