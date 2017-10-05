'''
Lab 10 - Unit Conversion
Marcel Schaeffer
10/4/17
'''

#user types amount of feet

feet = float(input('Type an amount of feet: '))
unit = input('Pick units to convert feet into; i.e. meters, miles, kilometers: ')

#units in meters
ft = 0.3048
mile = 1609.34
km = 1000

#converts feet into meters
# result = feet*ft
# print(str(feet) + ' feet is equal to ' + str(result) + ' meters.')

if unit == 'meters':
    result = feet*ft
    print(str(feet) + ' feet is equal to ' + str(result) + ' meters.')
elif unit == 'miles':
    result = (feet*ft)/mile
    print(str(feet) + ' feet is equal to ' + str(result) + ' miles.')
elif unit == 'kilometers':
    result = (feet*ft)/km
    print(str(feet) + ' feet is equal to ' + str(result) + ' kilometers.')