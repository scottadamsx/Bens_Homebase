
# grab the user data from the files. 
# have a file for all info 
'''
File for notes, list of lines 
contacts use a list of dictionaries (CSV)

'''

def get_contacts():
    contacts = []
    # we use our open function to create file object
    with open("contacts.csv", "r") as file:
        # for every contact in the file, grab the line as a list automatically
        for contact in file:
            contacts.append(contact.strip().split(",")) # strip takes the new line \n out, split will seperate them at every comma

    ''' NOWT: this is test code to display contacts
    print(contacts)
    for contact in contacts:
        print(contact)

    return contacts
    '''
    


def title():
    print("WELCOME TO THE GAMES MENU")

