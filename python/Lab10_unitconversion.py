'''
Lab 10 - Unit Conversion
Marcel Schaeffer
10/4/17
'''

#user types amount of feet

feet = int(input('Type an amount of feet: '))

meters = 0.3048

#converts feet into meters
result = feet*meters
print(str(feet) + ' feet is equal to ' + str(result) + ' meters.')
