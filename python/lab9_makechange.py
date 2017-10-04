'''
Lab 9 - Make Change
Marcel Schaeffer
10/4/17
'''

#user input
coins = int(input("Type an amount of pennies: "))

#coin values
quarter = 25
dime = 10
nickle = 5
penny = 1

#math
quarters = coins//quarter
print(quarters)
print("you have " + str(quarters) + " quarters")

x = coins - quarter*quarters

dimes = x//dime
print('you have ' + str(dimes) + ' dimes')

y = x - dime*dimes

nickles = y//nickle
print('you have ' + str(nickles) + ' nickles')

z = y - nickle*nickles

pennies = z//penny
print('you have ' + str(pennies) + ' pennies')

#Dollars to pennies

dollar = float(input('Enter an amount of dollars; e.g. 1.25'))
pens = dollar*100
print(str(dollar) + ' dollars equals ' + str(pens) + ' pennies')