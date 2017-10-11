'''
Lab 20 - Credit Card Validation
Marcel Schaeffer
10/11/17
'''


cc = input('Type a credit card number: ')

def valid(cc):
    nums = []
    for char in cc:
        nums.append(int(char))
    check_digit = nums[-1] #create the check digit
    nums = nums[:-1]  # del list[-1] #this also works to remove last digit from the list

    nums.reverse() #reverse the list

    for i in range(0, len(nums), 2): #double every other digit in the reveresed list
        nums[i] *= 2

    for i in range(len(nums)): #subtract 9 from numbers larger than 9
        if nums[i] > 9:
            num = nums[i]
            num -= 9
            nums[i] = num
    sum_nums = sum(nums)  # sum the list
    sum_nums = str(sum_nums)  # convert sum_nums to string
    last_digit = sum_nums.strip()[-1]  # get the last digit
    last_digit = int(last_digit) #convert last digit from string to int

    #print(last_digit)
    #print(check_digit)

    if last_digit == check_digit: #compare check digit and last digit to confirm validity
        return 'Credit card is Valid!'
    return 'Credit card is Invalid!'

print(valid(cc))
