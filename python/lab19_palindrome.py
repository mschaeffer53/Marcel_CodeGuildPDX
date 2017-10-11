'''
Lab 19 - Palindrome Check
Marcel Schaeffer
10/11/17
'''


word = str(input('Type a word see check whether it is a palindrome: ')) #user types word

#remove spaces from word
word = word.replace(' ', '')

#check palindrome function
def check_palindrome(word):
    if word == word[::-1]:
        return True
    return False

print(check_palindrome(word)) #print the answer

#check anagram function
def check_anagram(word1, word2):
    word1 = word1.lower() #make lowercase
    word2 = word2.lower()
    word1 = word1.replace(' ', '') #remove spaces
    word2 = word2.replace(' ', '')
    word1 = ''.join(sorted(word1)) #alphabetize letters of word
    word2 = ''.join(sorted(word2))

    if word1 == word2:
        return True
    return False

word1 = input('See if two words are anagrams...Type first word: ') #user inputs words
word2 = input('Type second word: ')

#compare word1 and word2 and print result of anagram check
if check_anagram(word1, word2) == True:
    print(word1 + ' and ' + word2 + ' ARE anagrams')

else: print(word1 + ' and ' + word2 + ' AREN\'T anagrams')


