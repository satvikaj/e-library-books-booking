# E-Booking Portal: A User-Friendly Booking Management System

## Background:
The **E-Booking Portal** is a Python-based booking management software developed with MySQL as its database backend. This project was created as part of a coursework assignment during a Wise Session. The system’s core interface is built with Python’s `Tkinter` library, offering an intuitive graphical user interface (GUI) for interacting with the system.

It is crucial to ensure that the system is operated with the necessary text files in the same directory as the Python files for proper functionality. The project was coded using **Python 3.11.2**.

## Key Design Principles:
The primary goal of the **E-Booking Portal** is to deliver a clear, efficient, and user-friendly interface, focusing on simplicity in design. The key design principles that guide this system include:

1. **Single Page Interface:**
   - The system consolidates all functionalities onto a single page. This approach minimizes complexity and ensures the user’s journey is straightforward, enabling them to accomplish tasks with ease.

2. **Dynamic Widgets:**
   - Widgets, such as buttons and entry boxes, are hidden by default. They are activated only when necessary, reducing visual clutter and presenting relevant options based on the user's actions.

3. **Intuitive Functionality:**
   - The system provides key functionalities like:
     - Viewing all library books
     - Adding new books
     - Deleting books
     - Handling book returns
     - Searching for specific book titles

4. **Consistent Presentation:**
   - Information is displayed in a clear and centralized manner, whether it is a list of books, the status of a booking, or search results. This consistency helps users quickly understand the data being presented.

5. **Confirmation Dialogs:**
   - For critical actions (e.g., deleting a book), confirmation prompts are displayed to ensure the user’s intent is confirmed before proceeding with the action.

6. **Automatic Restart:**
   - After performing actions such as adding, deleting, borrowing, or returning books, the system automatically restarts to reflect the updated information without requiring manual input from the user. This ensures a smooth experience and maintains system integrity.

## Technologies Used:
- **Programming Language**: Python 3.11.2
- **Database**: MySQL
- **GUI Framework**: Tkinter
- **Backend**: MySQL database for storing book details

## Features:
- **View All Books**: Users can view a list of all available books in the library.
- **Add a New Book**: Users can add new books to the system with the title and author details.
- **Delete a Book**: Admins can delete books after confirming the action.
- **Handle Book Returns**: Users can mark a book as returned.
- **Search Functionality**: Users can search for specific books by title or author.

## Installation:
1. **Clone this repository**:
    ```bash
    git clone https://github.com/satvikaj/e-library-books-booking.git
    ```

2. **Install dependencies**:
    Ensure you have Python 3.11.2 or later installed. Install MySQL if it's not already set up.
    Install the required Python libraries:
    ```bash
    pip install mysql-connector-python
    ```

3. **Setup Database**:
    Create a MySQL database and a `books` table with the following structure:
    ```sql
    CREATE DATABASE library_db;
    USE library_db;

    CREATE TABLE books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL
    );
    ```

4. **Run the Application**:
    - After the setup, run the Python application:
    ```bash
    python library.py
    ```


## Conclusion:
The **E-Booking Portal** embodies effective UI design principles and focuses on delivering a user-centric, intuitive experience. The system's simplicity, clear presentation, and responsiveness provide an easy and efficient way for users to manage their library bookings. As a foundational project, the E-Booking Portal offers an excellent base for exploring more advanced Python and GUI development techniques in future projects.

