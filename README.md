## Contact_book

### Project Overview and Requirements

In this Project the main goal is to save and modify contacts in our computer.
With this program you are going to be able to save, see and modify your contacts
through a simple UI. The contacts are saved in the same directory with main.py
and I use sqlite3 ready library from python. It's just a simple database, so
every time you run the program, you can have access to all of your contacts.

- To run this Project, the only thing you need is to have installed python3.
You just have to go to main's directory and run: python3 main.py
The rest is going to be easy and full of instructions

- The "secret" of this project is to create a simple .db file, where the program
saves a table. There are all of your contacts. They are accessible by you to
see them (alphabetical or in the order you entered them), to change them, to
add a new one, to find one particular or to delete one.

- Besides the main file, I have implemented a module to manipulate the database
through a simple class (with simple functions for its use) and some tests, in the
correspoding directory, to show that the module works fine. To run the tests you
just have to go to tests' directory and run: python3 db_module_test.py
Everything should work just fine.
