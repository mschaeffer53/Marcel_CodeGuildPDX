'''
Lab 12 - Simple Calculator
Marcel Schaeffer 10/4/17
'''

#user inputs
operator = input('Enter an operator (e.g. +, -, /, *) : ')
num1 = input('Enter your first number: ')
num2 = input('Enter another number: ')

result = eval(num1 + operator + num2)

print(result)

