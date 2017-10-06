'''
Lab 10 - Unit Conversion
Marcel Schaeffer
10/4/17
revised 10/6/17
'''

#user types amount of distance

feet = float(input('Type a distance: ')) #feet is really just a unitless distance
in_unit = input('What are the units to be converted from; i.g. feet, meters, miles, kilometers, inches, yards: ')
unit = input('Pick units to convert feet into; i.e. feet, meters, miles, kilometers, inches, yards: ')

#units in meters
ft = 0.3048
mile = 1609.34
km = 1000
inch = .0254
yard = .9144
#other conversions
meters_ft = 3.28084
mile_ft = 5280
mile_meter = 1608.34
mile_km = 1.60934
mile_in = 63360
mile_yd = 1760
km_mile = 0.621371
km_ft = 3280.84
km_in = 39370.1
km_yd = 1093.61
in_meter = 0.0254
in_yard = 0.0277778
yard_meter = 0.9144


#feet
if in_unit == 'feet':
    if unit == 'meters':
        result = feet*ft
        print(str(feet) + ' feet is equal to ' + str(result) + ' meters.')
    elif unit == 'miles':
        result = (feet*ft)/mile
        print(str(feet) + ' feet is equal to ' + str(result) + ' miles.')
    elif unit == 'kilometers':
        result = (feet*ft)/km
        print(str(feet) + ' feet is equal to ' + str(result) + ' kilometers.')

    #add yards and inches

    elif unit == 'inches':
        result = (feet*ft)/inch
        print(str(feet) + ' feet is equal to ' + str(result) + ' inches.')

    elif unit == 'yards':
        result = (feet * ft) / yard
        print(str(feet) + ' feet is equal to ' + str(result) + ' yards.')

#meters
if in_unit == 'meters':
    if unit == 'meters':
        result = feet
        print(str(feet) + ' meters is equal to ' + str(result) + ' meters.')
    elif unit == 'miles':
        result = (feet)/mile
        print(str(feet) + ' meters is equal to ' + str(result) + ' miles.')
    elif unit == 'kilometers':
        result = (feet)/km
        print(str(feet) + ' meters is equal to ' + str(result) + ' kilometers.')

    #add yards and inches

    elif unit == 'inches':
        result = (feet)/inch
        print(str(feet) + ' meters is equal to ' + str(result) + ' inches.')

    elif unit == 'yards':
        result = (feet)/yard
        print(str(feet) + ' meters is equal to ' + str(result) + ' yards.')

    elif unit == 'feet':
        result = (feet)*meters_ft
        print(str(feet) + ' meters is equal to ' + str(result) + ' feet.')

#miles

if in_unit == 'miles':
    if unit == 'meters':
        result = feet*mile_meter
        print(str(feet) + ' miles is equal to ' + str(result) + ' meters.')
    elif unit == 'miles':
        result = (feet)
        print(str(feet) + ' miles is equal to ' + str(result) + ' miles.')
    elif unit == 'kilometers':
        result = (feet)*mile_km
        print(str(feet) + ' miles is equal to ' + str(result) + ' kilometers.')

    #add yards and inches

    elif unit == 'inches':
        result = (feet)*mile_in
        print(str(feet) + ' miles is equal to ' + str(result) + ' inches.')

    elif unit == 'yards':
        result = (feet)*mile_yd
        print(str(feet) + ' miles is equal to ' + str(result) + ' yards.')

    elif unit == 'feet':
        result = (feet)*mile_ft
        print(str(feet) + ' miles is equal to ' + str(result) + ' feet.')

#kilometers

if in_unit == 'kilometers':
    if unit == 'meters':
        result = feet*1000
        print(str(feet) + ' kilometers is equal to ' + str(result) + ' meters.')
    elif unit == 'miles':
        result = (feet)*km_mile
        print(str(feet) + ' kilometers is equal to ' + str(result) + ' miles.')
    elif unit == 'kilometers':
        result = (feet)
        print(str(feet) + ' kilometers is equal to ' + str(result) + ' kilometers.')

    #add yards and inches

    elif unit == 'inches':
        result = (feet)*km_in
        print(str(feet) + ' kilometers is equal to ' + str(result) + ' inches.')

    elif unit == 'yards':
        result = (feet)*km_yd
        print(str(feet) + ' kilometers is equal to ' + str(result) + ' yards.')

    elif unit == 'feet':
        result = (feet)*km_ft
        print(str(feet) + ' kilometers is equal to ' + str(result) + ' feet.')

#inches

if in_unit == 'inches':
    if unit == 'meters':
        result = feet*in_meter
        print(str(feet) + ' inches is equal to ' + str(result) + ' meters.')
    elif unit == 'miles':
        result = (feet)/mile_in
        print(str(feet) + ' inches is equal to ' + str(result) + ' miles.')
    elif unit == 'kilometers':
        result = (feet)/km_in
        print(str(feet) + ' inches is equal to ' + str(result) + ' kilometers.')

    #add yards and inches

    elif unit == 'inches':
        result = (feet)
        print(str(feet) + ' inches is equal to ' + str(result) + ' inches.')

    elif unit == 'yards':
        result = (feet)*in_yard
        print(str(feet) + ' inches is equal to ' + str(result) + ' yards.')

    elif unit == 'feet':
        result = (feet)/12
        print(str(feet) + ' inches is equal to ' + str(result) + ' feet.')

#yards

if in_unit == 'yards':
    if unit == 'meters':
        result = feet*yard_meter
        print(str(feet) + ' yards is equal to ' + str(result) + ' meters.')
    elif unit == 'miles':
        result = (feet)/in_yard
        print(str(feet) + ' yards is equal to ' + str(result) + ' miles.')
    elif unit == 'kilometers':
        result = (feet)/km_yd
        print(str(feet) + ' yards is equal to ' + str(result) + ' kilometers.')

    #add yards and inches

    elif unit == 'inches':
        result = (feet)/in_yard
        print(str(feet) + ' yards is equal to ' + str(result) + ' inches.')

    elif unit == 'yards':
        result = (feet)
        print(str(feet) + ' yards is equal to ' + str(result) + ' yards.')

    elif unit == 'feet':
        result = (feet)*3
        print(str(feet) + ' yards is equal to ' + str(result) + ' feet.')
