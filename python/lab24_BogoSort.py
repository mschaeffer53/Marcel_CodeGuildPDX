'''
Lab 24 - Bogo Sort
Marcel Schaeffer
10/13/17
'''

#function that makes random list of numbers between 0-99 with a length of n
def random_list(n):
    import random
    rand_list = []
    i = 0
    while i < n:
        rand_list.append(random.randint(0,99))
        i += 1
    return rand_list


#function to shuffle nums in list
def shuffle(nums):
    from random import shuffle
    shuffle(nums)
    return nums


#is sorted
def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False #if any number is larger than the next then False
    return True #if nothing in list is False then True

#bogo sort
def bogosort(nums):
    sort = False
    count = 1
    while sort is False:
        shuffle(nums) #shuffle list of nums
        sort = is_sorted(nums) #nums is true if sorted else false
        count += 1
        if sort is True:
            print(nums)
            print('It took ' + str(count) + ' tries to sort the list.')
            return nums

#run functions
n = int(input('Type a number that represents the length of the random list: '))
nums = random_list(n) #make list of (n) length
print(nums)
bogosort(nums)
