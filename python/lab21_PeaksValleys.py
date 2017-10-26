'''
Lab 21 - Peaks and Valleys
Marcel Schaeffer
10/11/17
'''

data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]

#peak function
def peak(data):
    peak_list = []
    for i in range(1, len(data)-1):
        num = data[i]
        if num > data[i + 1] and num > data[i - 1]: #compare item to item before and after
            peak_list.append(i) #append peaks to peak list
    return peak_list

print(peak(data))

#valley function
def valley(data):
    valley_list = []
    for i in range(1, len(data)-1):
        num = data[i]
        if num < data[i + 1] and num < data[i - 1]: #compare item to item before and after
            valley_list.append(i) #append valleys to valley list
    return valley_list

print(valley(data))


#peaks and valleys
def peaks_and_valleys(data): #create peaks and valleys function
    p_v = []
    p_v.extend(peak(data))
    for i in peak(data): #append peak to list
        p_v.append(i)
    for i in valley(data): #append valley to list
        p_v.append(i)

    peak_and_valley = sorted(p_v) #sort list
    return (peak_and_valley)

print(peaks_and_valleys(data))