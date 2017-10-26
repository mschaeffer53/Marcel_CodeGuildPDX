'''
Lab 22 - Practice Problems 2
Marcel Schaeffer
10/12/17
'''


#problem 1
def REPL(): #create function that puts user numbers into a list
    num_list = []
    user_num = ""
    while user_num != 'done': #loops until user types 'done'
        if user_num != "": #skips adding the initial blank user number to list
            user_num = int(user_num) #changes string to int
            num_list.append(user_num) #adds user num to list
        user_num = input('Enter a number (or type \'done\' to exit): ') #prompts for user input
    return num_list

# print(REPL())


#problem 2
nums = [0,1,2,3,4,5,6,7,8]

#while loop version
def every_other_while(nums):
    list2 = []
    i = 0
    while i < len(nums):
        list2.append(nums[i])
        i += 2
    return list2

#for loop version
def every_other_for(nums):
    list = []
    for i in range(0, len(nums), 2):
        list.append(nums[i])
    return list

# print(every_other_while(nums))
# print(every_other_for(nums))


#problem 3
nums = [5,6,2,3]
target = 7

def find_pair(nums, target):

    for i in range(len(nums)): #iterate thru each num in list
        for j in range(i+1, len(nums)): #iterate thru the num after the num from the above line of code
            if (nums[i] + nums[j]) == target: #compare nums to target
                return([nums[i] ,nums[j]]) #return list

# print(find_pair(nums, target))

#problem 4

def double_word(string):
    word = ''
    for letter in text:
        double = letter*2
        word += double
    return word

# text = input('Enter some text: ')
# print(double_word(text))

#problem 5
list_odds = [1,3,5]
list_evens =[2,4,6]
list_odds_evens = list(zip(list_odds, list_evens))
# print(list_odds_evens)

#problem 6
def opposite(num1, num2):
    if num1*num2 < 0:
        return True
    else: return False

#print(opposite(4,-5))

#problem 7
def near_100(num):
    if num > 89 and num < 111:
        return True
    else:
        return False

# print(near_100(111))

#problem 8





#problem 9

def count_hi(string): #count the frequency of 'hi' in a string
    count = 0
    for i in range(len(string)):
        if string[i] == 'h' and string[i+1] == 'i':
            count += 1
    return count

# string = 'hihihibyehi'
# print(f'The string \'{string}\' has the word \'hi\' in it {count_hi(string)} times.')

#problem 10

def count_cat(string): #count the frequency of 'cat' in a string
    cat_count = 0
    for i in range(len(string)):
        if string[i] == 'c' and string[i+1] == 'a' and string[i+2] == 't':
            cat_count += 1
    return cat_count

def count_dog(string): #count the frequency of 'cat' in a string
    dog_count = 0
    for i in range(len(string)):
        if string[i] == 'd' and string[i+1] == 'o' and string[i+2] == 'g':
            dog_count += 1
    return dog_count

def cat_dog_is_equal(string):
    if count_cat(string) == count_dog(string):
        return True
    else:
        return False

# s = 'catdogdogcat'
# print(cat_dog_is_equal(s))


#problem 11

def eveneven(list):
    count = 0
    for num in list:
        if num%2 == 0:
            count +=1

    if count%2 == 0:
        return True
    else: return False

# list_nums = [2, 4, 6, 8, 9]
# print(eveneven(list_nums))


#problem 12

def combine_all(list_lists):
    list_nums = []
    for i in range(len(list_lists)):
        for num in list_lists[i]:
            list_nums.append(num)
    return list_nums

# list_lists = [[1,2,3], [4,6,8], [10,11]]
# print(combine_all(list_lists))


#problem 13

#def fibonacci(n):


#problem 14

word = 'pneumonoultramicroscopicsilicovolcanoconiosis'

abc_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
            'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
            'y': 25, 'z': 26}

abc_dict_reversed = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
                     13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
                     24: 'x', 25: 'y', 26: 'z'}

value = 0
for letter in word:
    if abc_dict[letter] > value:
        value = abc_dict[letter]
latest_letter = abc_dict_reversed[value]
#print(f'The latest letter in \'{word}\' is \'{latest_letter}\'.')