###################################
# Implementation of Database module
###################################


import sqlite3



# Class Database
class Database:

    # Constructor
    def __init__(self, name):
        self.name = name
        self.name_to_num = {}
        self.num_to_name = {}

        # Connecting to database
        conn = sqlite3.connect(name + ".db")
        cur = conn.cursor()

        cur.execute("select count(name) from sqlite_master where type='table' and name='" + name + "'")

        # If table exists, TODO
        if cur.fetchone()[0] == 1:
            print("Table exists")
            # TODO: fill in dicts
        # Else create it
        else:
            cur.execute("create table " + name + " (name, number)")

        # Closing connection
        conn.commit()
        conn.close()

    
    # Add new registration
    def add(self, name, number):
        # Connecting to database
        conn = sqlite3.connect(self.name + ".db")
        cur = conn.cursor()

        # TODO: Check if already registered
        
        # Inserting registration
        cur.execute("insert into " + self.name + " values (?, ?)", (name, number))

        # Insert registration to dicts
        self.name_to_num[name] = number
        self.num_to_name[number] = name

        # Closing connection
        conn.commit()
        conn.close()


    # Delete old registration, by name
    def delete(self, name):
        print("TODO")

    
    # Delete old registration, by number
    def delete(self, number):
        print("TODO")


    # Find a contact, by name
    def find(self, name):
        # Check if name exists in table
        if self.name_to_num.has_key(name):
            print("Name: " + name + ", Phone_number: " + self.name_to_num.get(name))
        else:
            print("Contact not found")


    # Find a contact, by number
    def find(self, number):
        # Check if name exists in table
        if self.num_to_name.has_key(number):
            print("Name: " + self.num_to_name.get(number) + ", Phone_number: " + number)
        else:
            print("Contact not found")


    # Print all contacts
    def print(self):
        print("TODO")


