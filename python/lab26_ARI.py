'''
Lab 26 - ARI
Marcel Schaeffer
10/17/17
'''

import math

book = r'C:\Users\ducks\Documents\kama_sutra_python.txt' #location of book
punct = ",./\;\"{}[]&@!#$%^*()'?&-" #punctuation to be removed
book_name = book.rsplit('\\', 1)[-1] #name of the text doc

with open(book, 'r') as f:
    contents = f.read()
    working_book = contents.lower()
    sentences = working_book.split('.')  # make list of sentences
    working_book = working_book.replace('\n', ' ') #replaces new lines with a space
    for char in punct:
        working_book = working_book.replace(char, "")  #remove punct

    working_book = working_book.split(' ')  # make list of words

word_count = (len(working_book)) #amount of words in text
print(working_book)
sentence_count = (len(sentences)) #amount of sentences
char_count = 0 #amount of characters in text
for word in working_book:
    for char in word:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            char_count += 1

# print(char_count)
# print(word_count)
# print(sentence_count)

#calc ARI
ARI = math.ceil(4.71*(char_count/word_count) + 0.5*(word_count/sentence_count) - 21.43)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}}


#results
grade_level = ari_scale[ARI]
print('The ARI for the ' + book_name + ' is ' + str(ARI) + '.')
if ARI == 9:
    print('This corresponds to an ' + str(grade_level['grade_level']) + ' level of difficulty.')
else: print('This corresponds to a ' + str(grade_level['grade_level']) + ' level of difficulty.')
print('This is suitable for an average person ' + str(grade_level['ages']) + ' years old.')