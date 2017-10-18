'''
Lab 27 - Contact List
Marcel Schaeffer
10/17/17
'''

csv_file = 'contacts.csv'
new_line = '\n'
list_dict = []
with open(csv_file, 'r') as file:
    lines = file.read().split('\n')
    header = lines[0].split(',') #keys
    #print(header)

    for i in range(1, len(lines)):
        non_header = lines[i].split(',') #values
        #print(non_header)

        contact = {}
        for i in range(len(header)):
            key = header[i]
            value = non_header[i]
            contact[key] = value #dictionary
        list_dict.append(contact) #append dicts to list
#print(list_dict)

#create a record
def create_record():
    #user values
    info = []
    name = (input('What is your name?: '))
    color = (input('What is your favorite color?: '))
    fruit = (input('What is your favorite fruit?: '))

    info.append(name) #add user values to info list
    info.append(color)
    info.append(fruit)
    #print(info)

    new_contact = {}
    for i in range(len(header)): #add keys and values to new contact dictionary
        key = header[i]
        value = info[i]
        new_contact[key] = value
    list_dict.append(new_contact) #add new contact to the original list of dictionaries

    #print(list_dict)
    return list_dict


#retrieve a record
def retrieve(list_dict):
    contact_name = input('Type the name of a contact: ') #enter contact name to look up

    #look up contact info and print it
    for i in range(len(list_dict)):
        contact = list_dict[i]
        if contact['Name'] == contact_name:
            print(contact)

#update a record
def update_contact(list_dict):

    contact_name_update = input('Who would you like to update the contact info for? ')
    key_update = input('Update \'Name\', \'Favorite Color\', or \'Favorite Fruit\'?')
    value_update = input('What is the new value?')

    for i in range(len(list_dict)):
        contact = list_dict[i]
        if contact['Name'] == contact_name_update: #matches the name of contact to the contact name update
            contact[key_update] = value_update #changes the value of the key
    print(list_dict)
    return list_dict

#delete a record

def delete_record(list_dict):
    print('Lets delete someone meow.')
    delete = input('Who should we remove from the contact list? ')

    for i in range(len(list_dict)):
        contact = list_dict[i]
        if contact['Name'] == delete: #matches the name of contact to the contact to be removed
            list_dict.pop(i)
            print(list_dict)
            return list_dict


#repl function to do stuff to the contact list
def repl():
    print('Lets get started...')
    while True:
        no_more = input('Type \'exit\', \'done\', or \'quit\' to end this program. Type any key to continue. ')
        if no_more in ['done', 'exit', 'quit']:
            break
        else:
            pass
            print('First, we need to create a new record...')
            create_record()
            print('Great! We added that to the contact list.')
            print('Now lets look up a contact\'s info...')
            retrieve(list_dict)
            print('Now lets update a contact...')
            update_contact(list_dict)
    return list_dict
print(repl())






#write dict to file

# list_rewrite = []
# for i in list_dict:
#     list_rewrite.append(i)
# print(list_rewrite)
#
# csv_rewrite = 'contacts_rewrite'
# with open(csv_rewrite, 'w') as file:
#     file.write(list_dict)