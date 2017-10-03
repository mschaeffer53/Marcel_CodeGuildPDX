'''
Lab 6 - Random Emoticon Generator
Marcel Schaeffer
10/3/17
'''

import random

#create lists

eyes = [':', ';', 'x', '$']
noses = ['-', '^', 'v', '']
mouths = ['p', 'D', 'O', 'X']

#randomly select from list

# eye = random.choice(eyes)
# nose = random.choice(noses)
# mouth = random.choice(mouths)

#smiley face
i = 0
while i<5:
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)

    print(eye + nose + mouth)
    i += 1
