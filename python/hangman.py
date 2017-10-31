'''
Hangman Game
Marcel Schaeffer
10/23/17
'''

#load file of words

import random
def list_words():
    with open('english.txt', 'r') as f:
        contents = f.read().lower()

    words = contents.split('\n')
    list_words = []
    for word in words:
        if len(word) > 6 and len(word) < 12:
            list_words.append(word)
    return list_words

list_words = list_words()

rand_word = random.choice(words)


unknown_word = []
already_guessed = []
guesses_left = 10
for letter in rand_word:
    unknown_word.append('_')

while guesses_left > 0:
    print('Guesses remaining is ' + guesses_left)
    for char in unknown_word:
        print(char,end=' ')

    guess = input('Guess a letter: ')
    if guess in already_guessed:
        print('You already guessed that')
        continue
    found_letter = False
    for i in range(len(rand_word)):
        if rand_word[i] == guess:
            rand_word[i] = guess[i]
            found_letter = True
    if found_letter == False:
        guesses_left -= 1

    if '_' not in unknown_word:
        print('You\'ve won!')
        break
print(rand_word)