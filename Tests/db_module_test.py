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
        pass

    # Testing if deleting contact works fine
    def test_delete(self):
        pass

    # Testing if finding contact works fine
    def test_find(self):
        pass




# Run test_functions
if __name__ == '__main__':
    unittest.main()
