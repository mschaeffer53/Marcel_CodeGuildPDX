'''
Lab 25 - Count Words
Marcel Schaeffer
10/16/17
'''

book = r'C:\Users\ducks\Documents\kama_sutra_python.txt' #location of book
new_line = '\n'
punct = ",./\;\"{}[]&@!#$%^*()'?&-" #punctuation to be removed

with open(book, 'r') as f:
    contents = f.read()
    working_book = contents.lower()
    #print(working_book)
    for char in new_line:
        working_book = working_book.replace(char, ' ') #replaces new lines with a space
    for char in punct:
        working_book = working_book.replace(char, "")  #remove punct
    working_book = working_book.split(' ')  # make list of words
print(len(working_book))
#print(working_book)

#word_count = {word:working_book.count(word) for word in set(working_book) if word != ''} #counts the keys
word_count = {}

for word in working_book:
    if word == '':
        pass
    elif word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

words = list(word_count.items()) # list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

pair_count = {}
for i in range(len(working_book) - 1):
    word = working_book[i] + working_book[i + 1] #pair words together
    if word == '':
        pass
    elif word in pair_count: #add to dict and increase value
        pair_count[word] += 1
    else:
        pair_count[word] = 1

pairs = list(pair_count.items())  # list of tuples
pairs.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(pairs))):  # print the top 10 words, or all of them, whichever is smaller
    print(pairs[i])





            # # lst = [0, 1, 2, 3, 4, 5]
# # for elem in zip(lst[:-1], lst[1:]):
# #     print(elem)
# #
# for word1, word2 in zip(working_book[:-1], working_book[1:]):
#     word = word1 + word2
#
#     print(word)

# print(word_count)
# print(pair_count)