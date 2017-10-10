'''
Lab 17 - Number to Phrase
Marcel Schaeffer
10/10/17
'''

#user types number to be converted
num = int(input('Type an integer: '))

#get 100s, 10s, 1s digit
hundreds_digit = num//100
tens_digit = (num - (hundreds_digit*100))//10
ones_digit = num%10

#text results

ones_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_list = ['', '', '', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_list = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds_list = ['one hundred ', 'two hundred ', 'three hundred ', 'four hundred ', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred', '']

one = ones_list[ones_digit]
ten = tens_list[tens_digit]
hundred = hundreds_list[hundreds_digit-1]

if tens_digit == 1 and ones_digit == 1:
    ten = 'eleven'
    one = ' '
elif tens_digit == 1 and ones_digit == 2:
    ten = 'twelve'
    one = ' '
elif tens_digit == 1 and ones_digit == 3:
    ten = teens_list[ones_digit]
    one = ' '
elif tens_digit == 1 and ones_digit == 4:
    ten = teens_list[ones_digit]
    one = ' '
elif tens_digit == 1 and ones_digit == 5:
    ten = teens_list[ones_digit]
    one = ' '
elif tens_digit == 1 and ones_digit == 6:
    ten = teens_list[ones_digit]
    one = ' '
elif tens_digit == 1 and ones_digit == 7:
    ten = teens_list[ones_digit]
    one = ' '
elif tens_digit == 1 and ones_digit == 8:
    ten = teens_list[ones_digit]
    one = ' '
elif tens_digit == 1 and ones_digit == 9:
    ten = teens_list[ones_digit]
    one = ' '
else:
    pass
print(hundred + ' ' + ten + ' ' + one)

