'''
Drop Dead - Dice Game
Marcel Schaeffer
10/26
'''

import random

class Die:

    def __init__(self):
        self.alive = True


    def roll(self):
        return random.randint(1,6)


num_players = 4#int(input('How many players? '))
dice = []

for i in range(5): #create 5 instances of die
    dice.append(Die())

player_scores =[]

for i in range(num_players):
    print(f'player {i}\'s turn')
    player_dice = 5
    player_score = 0
    while len(player_dice) > 0:
        die_values = []

        for r in range(player_dice):
            die_values.append(random.randint(1,6))
        print('\t' + str(die_values)
        if 2 in die_values or 5 in die_values:
            player_dice -= die_values.count(2)
            player_dice -= die_values.count(5)
        else:
            player_score += sum(die_values)
        print('\t' + str(player_score)))
    player_scores.append(player_score)
winner = player_scores.index(winning_score)
print(player_scores)