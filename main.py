###################################
# Main file, user "interface" calls
###################################


import sys
import os
from os import path

sys.path.append("./Database")
from db_module import Database


# Main UserInterface
print("Welcome to your Contact Book")

DB_NAME = input("Give me your name: ")
db = Database(DB_NAME)

# Start the loop
while True:
    ans = input("Type 'i' to insert a contact, 'd' to delete, 'f' to find one, 'p' to see all of them or 'q' to quit: ")

    # Add contact
    if ans == 'i':
        name = input("Type contact's name: ")
        number = input("Type contact's number: ")

        db.add(name, number)
    # Delete contact
    elif ans == 'd':
        an = input("Type 'n' if you want to delete by name or anything else to delete by number: ")
        
        if an == 'n':
            name = input("Type name: ")
            db.delete_name(name)
        else:
            number = input("Type number: ")
            db.delete_num(number)
    # Find contact
    elif ans == 'f':
        an = input("Type 'n' if you want to find by name or anything else to find by number: ")

        if an == 'n':
            name = input("Type name: ")
            db.find_name(name)
        else:
            number = input("Type number: ")
            db.find_num(number)
    # Print all contacts
    elif ans == 'p':
        db.print()
    # Quit the loop (and the program)
    else:
        break

print("Closing program!")
