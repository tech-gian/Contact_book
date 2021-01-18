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
        self.id_counter = 0
        self.name_to_id = {}
        self.num_to_id = {}
        self.id_to = {}

        # Connecting to database
        conn = sqlite3.connect(name + ".db")
        cur = conn.cursor()

        cur.execute("select count(name) from sqlite_master where type='table' and name='" + name + "'")

        # If table exists
        if cur.fetchone()[0] == 1:
            print("Table exists")
            cur.execute("select * from " + name)
            rows = cur.fetchall()

            for row in rows:
                self.name_to_id[row[1]] = row[0]
                self.num_to_id[row[2]] = row[0]
                self.id_to[row[0]] = [row[1], row[2]]
                
            self.id_counter = rows[-1][0] + 1
        # Else create it
        else:
            cur.execute("create table " + name + " (id, name, number)")

        # Closing connection
        conn.commit()
        conn.close()


    # Return size of table (meaning dict)
    def size(self):
        return len(self.name_to_id)


    # Add new registration
    def add(self, name, number):
        # Connecting to database
        conn = sqlite3.connect(self.name + ".db")
        cur = conn.cursor()

        flag = True

        # If already registered
        if name in self.name_to_id or number in self.num_to_id:
            print("Contact already existing")
            flag = False
        else:
            # Inserting registration
            cur.execute("insert into " + self.name + " values (?, ?, ?)", (self.id_counter, name, number))

            # Insert registration to dicts
            self.name_to_id[name] = self.id_counter
            self.num_to_id[number] = self.id_counter
            self.id_to[self.id_counter] = [name, number]

            self.id_counter += 1

        # Closing connection
        conn.commit()
        conn.close()
        
        return flag


    # Delete old registration, by name
    def delete_name(self, name):
        # Check if name exists in table
        if name in self.name_to_id:
            # Removing elements from dicts
            temp_id = self.name_to_id.get(name)
            temp_num = self.id_to.get(temp_id)[1]
            self.name_to_id.pop(name)
            self.num_to_id.pop(temp_num)
            self.id_to.pop(temp_id)

            # Removing register from db
            # (Assume table exists)
            conn = sqlite3.connect(self.name + ".db")
            cur = conn.cursor()

            cur.execute("delete from " + self.name + " where id=?", (temp_id, ))
            
            # Closing connection
            conn.commit()
            conn.close()
            return True
        else:
            print("No contact with name: " + name + ", found")
            return False



    
    # Delete old registration, by number
    def delete_num(self, number):
        # Check if number exists in table
        if number in self.num_to_id:
            # Removing elements from dicts
            temp_id = self.num_to_id.get(number)
            temp_name = self.id_to.get(temp_id)[0]
            self.num_to_id.pop(number)
            self.name_to_id.pop(temp_name)
            self.id_to.pop(temp_id)

            # Removing register from db
            # (Assume table exists)
            conn = sqlite3.connect(self.name + ".db")
            cur = conn.cursor()

            cur.execute("delete from " + self.name + " where id=?", (temp_id, ))

            # Closing connection
            conn.commit()
            conn.close()
            return True
        else:
            print("No contact with number: " + number + ", found")
            return False


    # Find a contact, by name
    def find_name(self, name):
        # Check if name exists in table
        if name in self.name_to_id:
            temp_id = self.name_to_id.get(name)
            print("Name: " + name + ", Phone_number: " + self.id_to.get(temp_id)[1])
            return True
        else:
            print("Contact not found")
            return False


    # Find a contact, by number
    def find_num(self, number):
        # Check if number exists in table
        if number in self.num_to_id:
            temp_id = self.num_to_id.get(number)
            print("Name: " + self.id_to.get(temp_id)[0] + ", Phone_number: " + number)
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
                        print(item + " " + str(self.name_to_num.get(item)))

                    break
                # For alphabetical order
                elif ans == 'a':
                    temp = []
                    for item in self.name_to_num:
                        tup = (item, self.name_to_num.get(item))
                        temp.append(tup)

                    temp.sort(key=list_sort)
                    for item in temp:
                        print(item[0] + " " + str(item[1]))
                    
                    break
                else:
                    print("This isn't a valid answer. Type again")
