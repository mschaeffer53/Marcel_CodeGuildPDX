'''
Lab 32 - Rain Data
Marcel Schaeffer
10/24/17
'''


import datetime
import math

path = r'C:\Users\ducks\Documents\vernon_rain.csv'


def load_data(path):
    data_list = []
    with open(path, 'r') as file:
        for line in file:
            line = line.strip('\n')
            line = line.split(',')
            data_list.append(line)

    for list in data_list: #turn date into object
        list[0] = datetime.datetime.strptime(list[0], '%d-%b-%y')
        for i in range(1, len(list)):
            if list[i] == '-' or list[i] == '':
                continue
            list[i] = int(list[i])
            #print(list[0])
    return data_list


def average(nums):
    total = 0
    for num in nums:
        if num[1] == '-' or num[1] == '':
            continue
        total += num[1]
    return total/len(nums)

def variance(nums, average):  #nums is a list of lists
    total = 0
    count = 0
    for list in nums:
        #print(list)

        if list[1] == '-' or list[1] == '':
            continue
        diff = list[1] - average
        total += diff*diff
        count += 1

    return total/count

# av = average(nums)
# var = variance(nums, av)
# std = math.sqrt(var)

data = load_data(path) #access csv and format to list of lists

av = average(data)
print('The average daily rain is ' + str(av) + ' hundredths of an inch.')

var = variance(data, av)
print(f'The variance is {var}')

std = math.sqrt(var)
print(f'The standard deviation is {std}')

#find the most rainy day
for line in data:
    print(line[1])