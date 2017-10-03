'''
lab 2 - mad lib
'''

#user inputs

noun1 = input("Type a noun")
noun2 = input("Type another noun")
holiday1 = input("Name a holiday")
person1 = input("Name a person")
noun3 = input("Type another noun")
noun4 = input("Type another noun")
noun5 = input("Type another noun")
color = input("How about a color this time")
veggie1 = input("Say a vetegable")
noun6 = input("Type another noun")
verb1 = input("Ok, how about a verb")
verb2 = input("another verb")
exclamation1 = input("Now I want an exclamation like 'yikes'")
veggie2 = input("Type another veggie")
noun7 = input("Type another noun")
verb3 = input("Type another verb")
verb4 = input("Type another verb")
person2 = input("Another person")
exclamation2 = input("Type another exclamation")
holiday2 = input("Last one! Another holiday")

madlib = "Tonight is the " + noun1 + "! The one " + noun2 + " we all waited for, well next to " + holiday1
madlib += ". " + person1 + " and I are going to be a " + noun3 + " " + noun4 + ". The " + noun5
madlib += " turns " + color + ". The " + veggie1 + " are lit. We\'re ready to collect our " + noun6
madlib += "! A quick " + verb1 + " on the door to " + verb2 + " what we get. "
madlib += exclamation1 + " it\'s a " + veggie2 + ", my favorite I bet! More "
madlib += noun7 + " to" + verb3 + " upon, more treats to" + verb4 + ". " + person2
madlib += " and I are finally done!" + exclamation2 + " for Halloween my favorite " + holiday2

print(madlib)