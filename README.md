# Personalized Task Manager
A simple task manager I built using Python and MySQL while learning how applications interact with databases.

## Features
* User registration and login
* Add, update, and delete tasks
* Task status tracking
* Search tasks (by name and due date)
* Deadline alerts
* Task sorting (by date and priority)
* View overdue tasks

## Tech Stack
* Python
* MySQL

## Project Structure
* `src/` → Contains source code
* `docs/` → Contains project report

## How to Run
1. Clone the repository
2. Install dependencies:
   pip install mysql-connector-python
3. Set up your MySQL database:
   * Create a database named `task_manager`
   * Create required tables (`users`, `tasks`)
4. Update your database credentials in `database.py`
5. Run the application:
   python main.py
   
## What I Learned
* Connecting Python applications with a database
* Performing CRUD operations using SQL
* Structuring a small backend project

## Note
This is a CLI-based project built to understand how backend logic and databases work together.
