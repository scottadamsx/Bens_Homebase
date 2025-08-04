# import all files and make them call a test function to make sure theyre linked
import contacts
import notes
import settings
import saveData
import games
import data
import projects

def load_data():
    contactList = data.get_contacts()
    return contactList


def save_data():
    "placeholder for the save data function"

def menu(contactList):
    print("MENU OPTIONS")
    print("option 1: contacts [C]")
    print("option 2: games [G]")
    print("option 3: projects [P]")
    print("option 5: notes [N]")
    print("option 5: settings [S]")
    print("option 6: Save and Exit [ENTER]")

    choice = "enterLoop"
    while choice != ("C", "G", "P", "N", "S", ""):
        choice = input("Choose Menu Option [C, G, P, N, S, ENTER]: ").upper()
        if choice == "":
            print("Saving data")
            break
        elif choice == "C":
            contacts.title()
            contacts.contacts(contactList)
        elif choice == "G":
            games.title()
        elif choice == "P":
            projects.title()
        elif choice == "N":
            notes.title()
        elif choice == "S":
            settings.title()
        else:
            print("not a valid option chief")

        

    return choice

    


def main():
    
    # program logic 

    # upon loading, try to create our data sets from last session
    contactList = load_data()

    # Allow user to enter menu and exit when they are finished. menu loops until they exit on their own
    choice = menu(contactList)
    


if __name__ == "__main__":
    main()