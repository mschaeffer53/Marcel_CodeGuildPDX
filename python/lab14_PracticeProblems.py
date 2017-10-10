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

def  count_letter(char_to_find, text): #in class example
    count = 0
    for char in text:
        if char == char_to_find:
            count += 1
    return count


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

def lower_case(text): #in class example
    text = text.lower()
    text = text.strip()
    return text



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
    index = random.randint(0,2) #(0, len(a)-1) in class example
    return(a[index])

#execute function
fruits = ['apples', 'bananas', 'pears']
random_element(fruits)

#problem 6

#create function to pick max of 3 parameters

def max_of_three(a, b, c):
    max = sorted((a, b, c), reverse = True)
    return(max[0])

#execute function
print(max_of_three(100,5,3))

#problem 7

i = 0
while i < 20:
    print(2**i)
    i += 1

#problem 8

#create functions

def minimum(nums):
    sort = sorted(nums)
    return(sort[0])

def maximum(nums):
    sort = sorted(nums,reverse = True )
    return(sort[0])

#execute minimum/maximum functions
list = [5, 3, 34, -22, 8, 99, -5]
list2 = [ 50, 0, 50, 25, 75, 100]
list3 = [1, 1, 4, 5, 5, 7, 5, 9, 5, 154]
print(minimum(list))
print(maximum(list))

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
    return(mylist)

#execute reverse function

list4 = [1, 2, 3, 4, 5]
print(reverse(list4))

#problem 9

#write a function to find common elements between two lists

def common_elements(num1, num2):

    for item in num1:
        for thing in num2:
            if item == thing:
                return(item)


#execute common_elements function

list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list6 = [2, 4, 6, 8, 9]

print(common_elements(list5, list6))

#problem 10

#write function to add items less than 10 to new list

def extract_less_than_ten(nums):
    newlist = []
    for item in nums:
        if item < 10:
            newlist.append(item)
    return(newlist)


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
    return(newlist)

#lists
list8 = ['a','b','c']
list9 = [1,2,3]

#execture the function
mixed = combine(list8, list9)
print(mixed)