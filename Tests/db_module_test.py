#############################################
# Implementation of Tests for Database module
#############################################



import unittest
import sys
import string
import random
import os
from os import path

sys.path.append("../Database")
from db_module import Database



# Helping Functions


def get_random_string(len):
    # Generates random string with upper and lower case letters
    letters = string.ascii_letters
    temp = ''.join(random.choice(letters) for i in range(len))
    return temp



# Class for Database_Test
# Contains all the testing_functions
class Database_Test(unittest.TestCase):

    # Testing if db creation works fine
    def test_create(self):
        DB_NAME = get_random_string(10)

        # Create db
        db = Database(DB_NAME)

        # Check if file exists
        self.assertTrue(os.path.exists(DB_NAME + ".db"))
        self.assertEqual(db.size(), 0)

        # Delete file
        os.remove(DB_NAME + ".db")


    # Testing if inserting contact works fine
    def test_add(self):
        DB_NAME = get_random_string(10)

        # Create db
        db = Database(DB_NAME)


        # Inserting names with phones
        for i in range(0, 100):
            if i < 10:
                num = "692030400"
            else:
                num = "69203040"
            
            # Check if returned True
            self.assertTrue(db.add("test_name" + str(i), num + str(i)))

            # Check if inserted
            self.assertEqual(db.size(), i+1)


        # Check if we try to insert an existing contact
        self.assertFalse(db.add("test_name1", "6920304001"))
        self.assertEqual(db.size(), 100)


        # Delete file
        os.remove(DB_NAME + ".db")



    # Testing if deleting contact works fine
    def test_delete(self):
        DB_NAME = get_random_string(10)


        # Create db
        db = Database(DB_NAME)

        # Insert names with phones
        for i in range(0, 100):
            if i < 10:
                num = "692030400"
            else:
                num = "69203040"

            db.add("test_name" + str(i), num + str(i))

        # Delete a contact by name
        self.assertTrue(db.delete_name("test_name63"))
        self.assertFalse(db.delete_name("no_existing"))
        self.assertEqual(db.size(), 99)

        # Delete a contact by number
        self.assertTrue(db.delete_num("6920304082"))
        self.assertFalse(db.delete_num("8150607080"))
        self.assertEqual(db.size(), 98)

        os.remove(DB_NAME + ".db")



    # Testing if finding contact works fine
    def test_find(self):
        pass




# Run test_functions
if __name__ == '__main__':
    unittest.main()
