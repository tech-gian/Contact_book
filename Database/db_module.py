###################################
# Implementation of Database module
###################################


import sqlite3



# Helping functions
def list_sort(item):
    return item[0]


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

        return True


    # Delete old registration, by name
    def delete(self, name):
        # Check if name exists in table
        if self.name_to_num.has_key(name):
            # Removing elements from dicts
            number = self.name_to_num.get(name)
            self.name_to_num.pop(name)
            self.num_to_name.pop(number)

            # Removing register from db
            # TODO: check if table exists
            conn = sqlite3.connect(self.name + ".db")
            cur = conn.cursor()

            cur.execute("delete from " + self.name + " where id=?", name)
            
            # Closing connection
            conn.commit()
            conn.close()
            return True
        else:
            print("No contact with name: " + name + ", found")
            return False



    
    # Delete old registration, by number
    def delete(self, number):
        # Check if number exists in table
        if self.num_to_name.has_key(number):
            # Removing elements from dicts
            name = self.num_to_name.get(number)
            self.num_to_name.pop(number)
            self.name_to_num.pop(name)

            # Removing register from db
            # TODO: check if table exists
            conn = sqlite3.connect(self.name + ".db")
            cur = conn.cursor()

            cur.execute("delete from " + self.name + " where id=?", name)

            # Closing connection
            conn.commit()
            conn.close()
            return True
        else:
            print("No contact with number: " + number + ", found")
            return False


    # Find a contact, by name
    def find(self, name):
        # Check if name exists in table
        if self.name_to_num.has_key(name):
            print("Name: " + name + ", Phone_number: " + self.name_to_num.get(name))
            return True
        else:
            print("Contact not found")
            return False


    # Find a contact, by number
    def find(self, number):
        # Check if number exists in table
        if self.num_to_name.has_key(number):
            print("Name: " + self.num_to_name.get(number) + ", Phone_number: " + number)
            return True
        else:
            print("Contact not found")
            return False


    # Print all contacts
    def print(self):
        while (True):
            ans = input("Show your contacts with the order you entered them or alphbetical? (Type 'o' or 'a'): ")
            if type(ans) != str:
                print("This isn't a valid answer. Type again")
            else:
                ans = str(ans)

                # For entered order
                if ans == 'o':
                    for item in self.name_to_num:
                        print(item + " " + self.name_to_num.get(item))

                    break
                # For alphabetical order
                elif ans == 'a':
                    temp = []
                    for item in self.name_to_num:
                        tup = tuple(item, self.name_to_num.get(item))
                        temp.append(tup)
                    
                    # TODO: check that list_sort() works fine
                    temp.sort(key=list_sort)
                    for item in temp:
                        print(item[0] + " " + item[1])
                    
                    break
                else:
                    print("This isn't a valid answer. Type again")
                

