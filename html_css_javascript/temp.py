my_rps_list = ['rock','paper','scissors']
your_rps_list = ['rock','paper','scissors']
you_count = 0
bot_count = 0
game_count = 0
import random
print("Let's play rock, paper, scissors!")
while game_count < 3:
    you_shoot = input("1, 2, 3, Shoot!\n:")
    bot_shoot = (random.choice(my_rps_list))
    print(bot_shoot)

    if you_shoot ==  bot_shoot:
        print("Tie!")
    if you_shoot == 'rock' and bot_shoot == 'paper':
        print("I win!")
        bot_count += 1
        print("Good game. Best out of 3?")
    elif you_shoot == 'rock' and bot_shoot == 'scissors':
        print("You win!")
        you_count += 1
        print("Good game. Best out of 3?")
    elif you_shoot == 'paper' and bot_shoot == 'scissors':
        print("I win!")
        bot_count += 1
        print("Good game. Best out of 3?")
    elif you_shoot == 'paper' and bot_shoot == 'rock':
        print("You win!")
        you_count += 1
        print("Good game. Best out of 3?")
    elif you_shoot == 'scissors' and bot_shoot == 'rock':
        print("I win!")
        bot_count += 1
        print("Good game. Best out of 3?")
    elif you_shoot == 'scissors' and bot_shoot == 'paper':
        print("You win!")
        you_count += 1
        print("Good game. Best out of 3?")
    else:
        print("That's not part of the game.")

    print('You' + str(you_count))
    print('Bot' + str(bot_count))
    game_count = you_count + bot_count
    print(game_count)
if you_count > bot_count:
    print("Awesome! You win!")
elif bot_count > you_count:
    print("Cool beans! I win!")