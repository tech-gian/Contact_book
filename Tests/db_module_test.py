#############################################
# Implementation of Tests for Database module
#############################################



import unittest
import sys

sys.path.append("../Database")
from db_module import Database


# Class for Database_Test
# Contains all the testing_functions
class Database_Test(unittest.TestCase):

    # Testing if db creation works fine
    def test_create(self):
        pass

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
