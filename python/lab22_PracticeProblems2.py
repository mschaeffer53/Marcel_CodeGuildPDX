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

print(REPL())


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

print(every_other_while(nums))
print(every_other_for(nums))


#problem 3
nums = [5,6,2,3]
target = 7

def find_pair(nums, target):

    for i in range(len(nums)): #iterate thru each num in list
        for j in range(i+1, len(nums)): #iterate thru the num after the num from the above line of code
            if (nums[i] + nums[j]) == target: #compare nums to target
                return([nums[i] ,nums[j]]) #return list

print(find_pair(nums, target))

#problem 4

text = input('Enter some text: ')
word = ''
for letter in text:
    double = letter*2
    word += double
print(word)

#problem 5
list_odds = [1,3,5]
list_evens =[2,4,6]
list_odds_evens = list(zip(list_odds, list_evens))
print(list_odds_evens)

#problem 6
def opposite(num1, num2):
    if num1*num2 < 0:
        return True
    else: return False

print(opposite(4,-5))

#problem 7
def near_100(num):
    if num > 89 and num < 111:
        return True
    else:
        return False

print(near_100(111))

