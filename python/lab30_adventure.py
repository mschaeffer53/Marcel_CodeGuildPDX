'''
Lab 30 - Adventure
Marcel Schaeffer
10/19/17
'''



import random

class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for j in range(height):
            row = []
            for i in range(width):
                row.append(' ')
            self.board.append(row)

    # def random_location(self):
    #     i =


class Entity:
    def __init__(self, name, symbol, loc_i, loc_j):
        self.name = name
        self.symbol = symbol
        self.loc_i = loc_i
        self.loc_j  = loc_j

class LivingEntity(Entity):
    def __init__(self, name, symbol, loc_i, loc_j, health, attack, defense):
        super().__init__(name, symbol, loc_i, loc_j)
        self.health = health
        self.attack = attack
        self.defense = defense

class Player(LivingEntity):
    def __init__(self):
        super().__init__('Player', '𓁕', health=10, attack=1,defense=1)

class Skeleton(LivingEntity):
    def __init__(self, loc_i, loc_j):
        super().__init__('Skeleton','☠', health=10, attack=1, defense=1)



width = 11  # the width of the board #made board wider-ms
height = 11  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = random.randint(1,9) #made changes to random starting place-ms
player_j = random.randint(1,9)

# add 4 enemies in random locations
for i in range(10): #made change to add extra enemys-ms
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

#add some treasure
for i in range(5): #made change to add extra enemys-ms
    treasure_i = random.randint(0, height - 1)
    treasure_j = random.randint(0, width - 1)
    board[treasure_i][treasure_j] = '*'
# loop until the user says 'done' or dies

lives = 3
treasure = 0
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'done' or command == 'exit' or command == 'quit': #made change to add 'quit and 'exit' -ms
        break  # exit the game
    elif command == 'left' or command == 'l':
        player_j -= 1  # move left
    elif command == 'right' or command == 'r':
        player_j += 1  # move right
    elif command == 'up' or command == 'u':
        player_i -= 1  # move up
    elif command == 'down' or command == 'd':
        player_i += 1  # move down

    # check if the player is on the same space as an enemy

    if board[player_i][player_j] == '§':

        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':

            fiftyfifty = random.randint(1,2) #made change, you have 75% chance of winning when you attack
            print(fiftyfifty)
            if fiftyfifty < 2:
                print('you\'ve slain the enemy')
            else:
                if lives != -1:
                    print('you lost one life')
                    lives -= 1 #this isnt working right
            print(str(lives) + ' lives left.')
            board[player_i][player_j] = ' '  # remove the enemy from the board
            if lives == -1:
                print('You\'re dead meow.')
                break
        else:
            print('you hestitated and were slain')
            break
    elif board[player_i][player_j] == '*':
        treasure += 1
        print(str(treasure))
            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()