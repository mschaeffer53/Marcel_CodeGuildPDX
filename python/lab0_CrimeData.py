'''
Lab (optional) - Crime Data
Marcel Schaeffer
10/25/17
'''

import datetime

#location of data file
crime_file = r'C:\Users\ducks\Documents\portland_crime_data.csv'

#read data file of crime
with open(crime_file, 'r') as file:
    data_list = []
    skip_first = True
    for line in file:
        if skip_first:
            skip_first = False
            continue
        line = line.strip('\n')
        line = line.split(',')
        data_list.append(line)

#create list of crime types
crime_types = []
for list in data_list:
    if list[9] not in crime_types:
        crime_types.append(list[9])

#dictionary of crime types (key) and occurances (value)
crime_dict = {}
for crime in crime_types:
    crime_dict[crime] = 0
    for list in data_list:
        if list[9] == crime:
            crime_dict[crime] += 1

#print(crime_dict)

#find the most/least common crimes
max_crime = 0
for key in crime_dict:
    if crime_dict[key] > max_crime:
        max_crime = crime_dict[key]

min_crime = max_crime #this is like setting count to 0 when counting up, except here we're counting down later

for key, value in crime_dict.items():
    if value == max_crime:
        max_crime = key

print(f'The most common crime in Portland is {max_crime}.')

# min_crime = 10000000000
for key in crime_dict:
    if key == 'Offense Type':
        pass
    elif crime_dict[key] < min_crime:
        min_crime = crime_dict[key]

for key, value in crime_dict.items():
    if value == min_crime:
        min_crime = key

print(f'The least common crime in Portland is {min_crime}.')

#find unique years of data
unique_years = []
for list in data_list:
    list[4] = datetime.datetime.strptime(list[4], '%m/%d/%Y')
    if list[4].year not in unique_years:
        unique_years.append(list[4].year)

#make dictionary of years and count of crimes
year_dict = {}
for year in unique_years:
    year_dict[year] = 0


for year in unique_years:
    for list in data_list:
        if list[4].year == year:
            year_dict[year] += 1

print(year_dict)

#find the year with the most crime
max_crime = 0
for key in year_dict:
    if year_dict[key] > max_crime:
        max_crime = year_dict[key]

for key, value in year_dict.items():
    if value == max_crime:
        max_crime = key

print(f'The year with the most crime recorded (in the spreadsheet I downloaded) was {max_crime}.')
