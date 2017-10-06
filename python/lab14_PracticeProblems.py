'''
Lab 14 - Practice Problems
Marcel Schaeffer
10/5/17
'''

#problem 1

word = 'Antidisestablishmentterianism'
print(word.count('i'))

word2 = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
print((word2.count('p')) + (word2.count('P')))

#problem 2

latest = 'Pneumonoultramicroscopicsilicovolcanoconiosis'

sort = sorted(latest)
print((sort)[-1])

#problem 3

upper_case = 'SUPER!'
lower_case = upper_case.lower()
print(lower_case)

whitespace = '     NANANANA BATMAN!     '
caps = (whitespace[5:-5])
no_caps = caps.lower()
print(no_caps)

#problem 4

#create odd/even function
def is_even(a):
    if a % 2 == 0:
        print('even')
    else:
        print('odd')

#execute function
b = 5
c = 6
is_even(b)
is_even(c)

#problem 5

#create random from list function
import random
def random_element(a):
    index = random.randint(0,2)
    print(a[index])

#execute function
fruits = ['apples', 'bananas', 'pears']
random_element(fruits)

#problem 6

#create function to pick max of 3 parameters

def max_of_three(a, b, c):
    max = sorted((a, b, c), reverse = True)
    print(max[0])

#execute function
max_of_three(100,5,3)

#problem 7

i = 0
while i < 20:
    print(2**i)
    i += 1

#problem 8

#create functions

def minimum(nums):
    sort = sorted(nums)
    print(sort[0])

def maximum(nums):
    sort = sorted(nums,reverse = True )
    print(sort[0])

#execute minimum/maximum functions
list = [5, 3, 34, -22, 8, 99, -5]
list2 = [ 50, 0, 50, 25, 75, 100]
list3 = [1, 1, 4, 5, 5, 7, 5, 9, 5, 154]
minimum(list)
maximum(list)

#create mean/mode functions

def mean(nums):
    length = len(nums)
    total = sum(nums)
    average = total // length
    print(average)

def mode(nums):
    dictionary = {}
    for char in nums:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    print((max_dict(dictionary)))

def max_dict(dictionary):
    max_value = 0
    max_key = 0

    for key in dictionary:
        if dictionary[key] > max_value:
            max_value = dictionary[key]
            max_key = key

    return max_key

#execute mean/mode functions

mean(list2)
mode(list3)

#problem 8?

#write function to return the reverse of a list

def reverse(nums):
    mylist = []
    for i in reversed(nums):
        mylist.append(i)
    print(mylist)

#execute reverse function

list4 = [1, 2, 3, 4, 5]
reverse(list4)

#problem 9

#write a function to find common elements between two lists

def common_elements(num1, num2):
    for item in num1:
        for thing in num2:
            if item == thing:
                print(item)


#execute common_elements function

list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list6 = [2, 4, 6, 8, 9]

common_elements(list5, list6)

#problem 10

#write function to add items less than 10 to new list

def extract_less_than_ten(nums):
    newlist = []
    for item in nums:
        if item < 10:
            newlist.append(item)
    print(newlist)


#execute less than ten function
list7 = [1, 5, 6, 8, 8, 11, 15, 21]

extract_less_than_ten(list7)


#problem 11

#function to combine two lists into one list aternating items

def combine(nums1, nums2):
    newlist = []
    for i in range(len(nums1)):
        newlist.append(nums1[i])
        newlist.append(nums2[i])
    print(newlist)

#lists
list8 = ['a','b','c']
list9 = [1,2,3]

#execture the function
combine(list8, list9)