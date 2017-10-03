'''
lab 4 - grading
Marcel Schaeffer
'''

grade = int(input("Type a number 0-100"))

if grade > 90:
    print('A')
elif grade > 80:
    print('B')
elif grade > 70:
    print('C')
elif grade > 60:
    print('D')
else:
    print('Fail!')

