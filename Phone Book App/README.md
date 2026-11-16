Here's the complete `README.md` code for your **Phone Book App**, ready to copy and paste into your GitHub repository.

````

# 📞 Phone Book App

A simple command-line phone book application built with Python. This project allows users to add contacts, validate phone numbers, display all saved contacts, and search for a contact by name.

## 📌 Features

* ➕ Add new contacts
* 📋 Display all contacts in the phone directory
* 🔍 Search for a contact by name (case-insensitive)
* ☎️ Validate phone numbers before saving them
* ⚠️ Display a message when a phone number is invalid
* 📭 Handle an empty contact directory

## 🛠️ Technologies Used

* Python 3
* Classes and Objects
* Constructors (`__init__`)
* Class Variables
* Instance Methods
* Class Methods
* Static Methods
* Lists
* Loops and Conditional Statements
* User Input Handling
* String Methods

## 📂 Project Structure

```text
Phone-Book-App/
│
├── phone_book.py
└── README.md
```

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/Phone-Book-App.git
```

2. Navigate to the project folder

```bash
cd Phone-Book-App
```

3. Run the program

```bash
python phone_book.py
```

## 📋 How It Works

1. Enter how many contacts you want to add.
2. Enter the name and phone number for each contact.
3. The app checks whether each phone number contains only digits and has at least 8 digits.
4. Valid contacts are added to the phone directory.
5. Invalid phone numbers are rejected with an error message.
6. After the input process, the app displays all valid contacts.

## 🔎 Contact Search

The `search_contact()` class method searches for a contact using the name provided. The search is case-insensitive and returns the matching phone number. If no matching contact is found, it returns a message.

> Note: The search method is implemented in the class but is not called in the current program flow.

## ☎️ Phone Number Validation

The `validate_phone_number()` static method accepts a phone number only when:

* It contains digits only.
* It has at least 8 digits.

Phone numbers containing letters, spaces, or special characters are rejected.

## 💡 Concepts Practiced

* Creating classes and objects
* Using constructors to initialize object attributes
* Managing shared data with a class variable
* Defining instance methods, class methods, and static methods
* Storing objects in a list
* Iterating through a list of objects
* Performing case-insensitive string comparisons
* Validating user input
* Building a basic command-line application

## 🚀 Future Improvements

* Add a menu to add, search, view, update, and delete contacts
* Allow users to search for contacts from the command line
* Prevent duplicate contacts
* Save contacts permanently using a text file, JSON, or database
* Add stronger phone number validation
* Create a graphical user interface (GUI)

## 📸 Sample Output

```text
How many contacts do you want to add?: 2

Enter the name of the contact: Alex
Enter the phone number: 9876543210

Enter the name of the contact: Sam
Enter the phone number: 12345
Invalid phone number for Sam, phone number should be atleast 8 digits and should only contain numbers

All contacts found in the directory
Name: Alex, Contact number: 9876543210
```

## 📚 Learning Outcomes

This project demonstrates the fundamentals of object-oriented programming in Python. It uses classes, objects, class variables, and different types of methods to manage contacts, while applying loops, conditional statements, and input validation in a practical command-line application.

---

⭐ If you found this project helpful, consider giving it a star!

````