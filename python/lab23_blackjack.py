'''
Lab 23 - Blackjack
Marcel Schaeffer
10/13/17
'''

#Blackjack game
def play_blackjack():
    #card values
    dict = {'A' : 1, '2' : 2, '3' : 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'a': 1, 'j': 10, 'q': 10, 'k': 10}
    #situations
    hit = 16
    stay = 20
    blackjack = 21
    bust = 22

    #user inputs cards
    first_card = input('What is your first card?: ')
    second_card = input('What is your second card?: ')
    third_card = input('What is your third card?: ')

    #hand total
    total = (dict[first_card] + dict[second_card] + dict[third_card])

    #check for aces to decide whether 1 or 11 value
    if first_card == 'a' or 'A' or second_card == 'a' or 'A' or third_card == 'a' or 'A':
        if total <= 12:
            total += 10

    #print hand total and advice
    if total <= hit:
        return (str(total) + ' hit') #these work too #print(f"{total} hit") #print("{0} hit".format(total))
    elif total <= stay:
        return (f'{total} stay')
    elif total == blackjack:
        return (f'{total} BLACKJACK!')
    else:
        return (f'{total} BUST!')

print(play_blackjack())