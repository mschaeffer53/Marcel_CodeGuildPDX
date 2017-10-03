'''
Lab 5 Magic 8 Ball
Marcel Schaeffer
10/3/17
'''


import random

#welcome message
print("Welcome to magic 8 ball, bare with me..")

#user prompt

question = input("Ask me a question...")

#list
answer = ["oh, hell no", "fo sho", "ask again later", "never ask that again"]

#responce to user question
print(random.choice(answer))
