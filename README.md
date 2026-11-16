# Movie Night — Film Database Manager

A desktop GUI application built with Python, **wxPython**, and **SQLite** for viewing, adding, and deleting film records from a local database (`movies.db`).

---

## Features

- **Display Film Records:** Loads and displays all records from the `afilms` table in a structured report-style list view (`film_id`, `title`, `release_year`, `language`, `rental_rate`, `length`, `rating`).
- **Insert New Films:** Opens a modal dialog box with input validation to add new movies to the database.
- **Delete Film Records:** Opens a modal dialog box allowing users to remove a film record by matching its exact title.
- **Error Handling:** Displays pop-up alert dialogs for missing fields, invalid data types, missing records, or SQLite connection issues.

---

## Prerequisites

- **Python 3.x**
- **wxPython** (GUI toolkit)
- **sqlite3** (included in the Python Standard Library)

Install `wxPython` via pip if it is not already installed:

bash
pip install wxPython
Database Setup
The application expects a SQLite database file named movies.db in the same directory as the script, containing a table named afilms.

If you need to initialize the database manually, run the following SQL schema:

SQL
CREATE TABLE IF NOT EXISTS afilms (
    film_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_year INTEGER NOT NULL,
    language INTEGER NOT NULL,
    rental_rate REAL NOT NULL,
    length INTEGER NOT NULL,
    rating TEXT NOT NULL
);
Usage
Place cit244-program-3.py and movies.db in the same working directory.

Run the application from your terminal:

Bash
python cit244-program-3.py

Use the buttons along the bottom of the main Movie Night window:

Display Data: Fetches and populates the table with all entries from movies.db.

Insert Data: Opens the Insert Data dialog. All fields are required:

Title: Text string (e.g., Inception)

Release Year: 4-digit integer (e.g., 2010)

Language: Integer representing the language ID/count (e.g., 1)

Rental Rate: Decimal number (e.g., 4.99)

Length: Runtime in minutes as an integer (e.g., 148)

Rating: MPAA/content rating string (e.g., PG-13)

delete entry: Opens the Delete Data dialog. Enter the exact title of the movie you want to remove and click OK.

Cancel: Closes the application.
