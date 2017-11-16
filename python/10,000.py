import random


roll_list = []
saved_rolls = []
dice = 6
for die in range(dice):
    roll = random.randint(1, 6)
    roll_list.append(roll)

print(roll_list)

save = int(input('Save which numbers? '))
while save != 'done':
    save = int(input('Save which numbers? '))
    if save in roll_list:
        dice -= 1