'''
Lab 29 - Road Trip
Marcel Schaeffer
10/19/17
'''

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}}

city_list = []
for city in city_to_accessible_cities:
    city_list.append(city)

print('You can start in one of these cities...' + str(city_list))
start = input('Which city would you like to start in? ')
print('OK, you\'re starting in ' + start + '.')
print('Let\'s hop to another city.')
for key in city_to_accessible_cities:
    if key == start:
        print('You can go to one of these cities: '+ str(city_to_accessible_cities[key]))
hop = input('Which of these cities do you want to hop to? ')
for key in city_to_accessible_cities:
    if key == hop:
        print('Sweet, now we are in ' + str(hop))