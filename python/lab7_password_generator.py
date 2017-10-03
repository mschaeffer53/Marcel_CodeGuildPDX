'''
Lab 7 - password
Marcel Schaeffer
10/3/17
'''

import random

n = int(input('pick a number to represent the amount of characters in a password'))
char = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

password = ""
i = 0
while i < n:
    password += random.choice(char)
    i += 1

print(password)
