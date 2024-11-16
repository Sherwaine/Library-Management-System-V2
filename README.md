# Library Management System

This Python project implements a library management system using MySQL for data persistence. The system allows for managing books, users, and administrators.  It provides functionalities for adding, viewing, searching, updating, and deleting records for each entity type.

## 1. Overview

This project demonstrates database interactions using MySQL and Python's `mysql.connector`.  The system features separate user interfaces for administrators and library users, providing role-based access control.  The core functionalities include book management, user account management, and feedback collection.


## 2. Database Structure

The system utilizes a MySQL database named `Library` containing the following tables:

* **BookRecord:** Stores book information (BookID, BookName, Author, Publisher).
* **UserRecord:** Stores user information (UserID, UserName, Password, BookID - the ID of the book currently issued).  `BookID` acts as a foreign key referencing `BookRecord`.
* **AdminRecord:** Stores administrator credentials (AdminID, Password).
* **Feedback:** Stores user feedback and ratings (Feedback, Rating).


The script creates these tables if they do not already exist.  Ensure MySQL is installed and running, and adjust the database connection parameters in the code to reflect your specific MySQL configuration.


## 3. System Features

**Administrator Features:**

* **Login/Logout:** Secure administrator login.
* **Book Management:** Add, display, search, update, and delete book records.
* **User Management:**  Add, display, search, update, and delete user accounts.
* **Admin Management:** Add, display, search, update, and delete admin accounts.
* **Feedback Table:** View all user feedback and ratings.


**User Features:**

* **Login/Registration:** Users can login or create a new account.
* **Book Centre:** View available books, issue books, view issued books, and return books.
* **Feedback and Ratings:** Submit feedback and ratings for the library.


## 4. Code Structure

The code is organized into multiple Python files for better maintainability:

* **`main.py`:** Contains the main menu and login functionality.
* **`Operations.py`:** Contains functions for managing the Admin and User Menus.
* **`Book.py`:** Contains functions for book-related operations (both admin and user).
* **`User.py`:** Contains functions for user-related operations (admin functions and user's login/registration).
* **`Admin.py`:** Contains functions for admin-related operations.


## 5. How to Run

1. **Install Dependencies:**  Ensure you have `mysql-connector-python` installed: `pip install mysql-connector-python`
2. **Database Setup:** Create a MySQL database named `Library` and ensure the tables (BookRecord, UserRecord, AdminRecord, Feedback) exist or create them using the SQL commands within the provided script.
3. **Run `main.py`:** Execute the `main.py` script. The program will start with the main menu, allowing you to choose between admin and user login.

## 6. Dependencies

* `mysql.connector`
* (Implicit) `sys`


## 7.  Limitations and Future Enhancements

* **Security:** Password storage is currently insecure (plain text).  Implement strong password hashing (e.g., bcrypt, Argon2) and salting for enhanced security.
* **Error Handling:** Add more comprehensive error handling (e.g., invalid inputs, database errors).
* **Input Validation:** Implement robust input validation to prevent SQL injection vulnerabilities.  Use parameterized queries.
* **Data Validation:** Add data validation to ensure data integrity (e.g., checking for duplicate entries, valid data types).
* **User Interface:** Consider developing a more user-friendly interface (e.g., a graphical user interface).
* **Advanced Features:** Add features like due dates for issued books, reservation system, search by author/title, and more sophisticated reporting capabilities.


This README provides a detailed overview. Remember to prioritize security best practices, particularly secure password handling and prevention of SQL injection, when developing and deploying this system.  The use of parameterized queries is crucial for mitigating SQL injection risks.
