'''
Lab 16 -Pick 6
Marcel Schaeffer
10/10/17
'''

# generate 6 random numbers

import random #import module

#creates 'powerball' function to generate 6 numbers in a list
def powerball():
    picks = []
    limit = 0
    while limit < 6:
        n = random.randint(1, 99) #this can return a number more than once :/
        picks.append(n)
        limit += 1
    return(picks)

#run function for the winning numbers
winning = powerball()

print('The 6 winning Powerball numbers are: ' + str(winning))


#function to compare winning numbers to user ticket

def win(list1, list2): #list1 is the winning powerball nums, list2 is the ticket being compared
    matches = {}
    for num in list1:
        matches[num] = list2.count(num)

    total = sum(matches.values()) #total number of correct numbers on a ticket
    return(total)


#starting counts for each type of winning ticket
pick1 = 0
pick2 = 0
pick3 = 0
pick4 = 0
pick5 = 0
pick6 = 0

#computer generates user tickets and uses win function to compare tickets

num_picks = int(input('Type the number of lottery picks (e.g. 100,000): ')) #prompt to select amount of tickets

i = 0
while i < num_picks:
    x = powerball()
    #print(x)
    i += 1
    tally = win(winning, x)
    #print(tally)

    #loop to count the totals for each ticket and tally the total tickets with that number of correct numbers
    if tally == 1:
        pick1 += 1
    if tally == 2:
        pick2 += 1
    if tally == 3:
        pick3 += 1
    if tally == 4:
        pick4 += 1
    if tally == 5:
        pick5 += 1
    if tally == 6:
        pick6 += 1

# print(pick1)
# print(pick2)
# print(pick3)
# print(pick4)
# print(pick5)
# print(pick6)

# #winning guide
correct_1 = 4
correct_2 = 7
correct_3 = 100
correct_4 = 50000
correct_5 = 1000000
correct_6 = 25000000

# #profits/losses calc
ticket_cost = -2

win1 = pick1*correct_1
win2 = pick2*correct_2
win3 = pick3*correct_3
win4 = pick4*correct_4
win5 = pick5*correct_5
win6 = pick6*correct_6
win_total = (win1 + win2 + win3 + win4 + win5 + win6)

balance = (num_picks*ticket_cost) + win_total
print('You bought ' + str(num_picks) + ' tickets and won $' + str(balance))

expenses = (num_picks*ticket_cost*-1)
roi = balance/expenses
print('Your return on investment is $' + str(roi))