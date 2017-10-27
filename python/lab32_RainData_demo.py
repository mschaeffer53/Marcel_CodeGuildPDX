'''
Lab 32 - Rain Data
Marcel Schaeffer
10/24/17
'''


import datetime
path = r'C:\Users\ducks\Documents\vernon_rain.csv'


def load_data(path):
    data_list = []
    with open(path, 'r') as file:
        for line in file:
            line = line.strip('\n')
            line = line.split(',')
            data_list.append(line)

    for list in data_list: #turn date into object
        list[0] = datetime.datetime.strptime(list[0], '%d-%b-%y') #create datetime object
        for i in range(1, len(list)):
            if list[i] == '-' or list[i] == '': #skip the lines with no data
                continue
            list[i] = int(list[i])
    return data_list

data = load_data(path) #access csv and format to list of lists


#find unique years
years = [] #list of unique years
for line in data:
    if line[0] == '-' or line[0] == '': #skip no data
        continue
    if line[0].year in years: #skip years already in list
        continue
    else: years.append(line[0].year) #append unique years

print(years) #list of years

year_dict = {} #assign each year as a key in a dict
for year in years:
    year_dict[year] = 0 #default value = 0

#print(year_dict) #empty dict

#add total rain as values to year keys in dict
for year in years:
    total_rain = 0
    day_count = 0
    for line in data:
        if year == line[0].year:
            if line[1] == '-' or line[1] == '':
                continue
            total_rain += int(line[1])
            day_count += 1
    year_dict[year] = total_rain/day_count #average daily rain accounts for days with no data

#print(year_dict) #dict with values

#find the rainiest year in a dictionary of years and rain values
max_rain_val = 0
for key in year_dict: #key is the year
    if year_dict[key] > max_rain_val: #if the year's value is greater than the current max set a new max
        max_rain_val = year_dict[key]

#print(max_rain_val) #value of most average rain

for key, value in year_dict.items(): #create a tuple of (key, value) from the key, value in the dictionary
    if value == max_rain_val:
        max_rain_year = key  #set max year to the key (year) of the value (max rain)

#print(f'The year with the most daily average rain was {max_rain_year}.')

