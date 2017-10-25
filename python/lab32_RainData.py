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
max_rain = 0
for line in data:
    if line[1] == '-' or line[1] == '':
        continue
    if int(line[1]) > max_rain:
        max_rain = line[1]
print(f'The rainiest day had {max_rain} hundredths of an inch of rain.')

for line in data:
    if line[1] == '-' or line[1] == '':
        continue
    if int(line[1]) == max_rain:
        max_day = line[0]

#print day, month, year of rainiest day
print(f'The rainiest day was {max_day.month}/{max_day.day}/{max_day.year}.')

#find unique years
years = [] #list of unique years
for line in data:
    if line[0] == '-' or line[0] == '':
        continue
    if line[0].year in years:
        continue
    else: years.append(line[0].year)

year_dict = {} #assign each year as a key in a dict
for year in years:
    year_dict[year] = 0


#add total rain as values to year keys in dict
for year in years:
    total_rain = 0
    for line in data:
        if year == line[0].year:
            if line[1] == '-' or line[1] == '':
                continue
            total_rain += int(line[1])
    year_dict[year] = total_rain


#find the rainiest year in a dictionary of years and rain values
max_rain_val = 0
for key in year_dict:
    if year_dict[key] > max_rain_val:
        max_rain_val = year_dict[key]

for key, value in year_dict.items():
    if value == max_rain_val:
        max_rain_year = key

print(f'The rainiest year was {max_rain_year}.')