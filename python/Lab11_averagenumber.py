'''
Lab 11 - Average Numbers
Marcel Schaeffer
10/4/17
'''

#user inputs numbers to be averaged
nums = []
while True:
    num = input("enter numbers to be averaged. Type \'done\' when finished: ")
    if num == 'done':
        break
    num = int(num)
    nums.append(num)

# #list of numbers to be averaged
# nums = [5, 0, 8, 3, 4, 1, 6]
#
#sum of list
total = sum(nums)

#length of list
length = len(nums)

#average of list
average = (total/length)
print(round(average, 2))



