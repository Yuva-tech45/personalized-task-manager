# Handles database connection and all task-related database operations
import mysql.connector
from datetime import datetime, timedelta
db = mysql.connector.connect(
    host='localhost',
    user='root',  
    password='your_password',  
    database='task_manager')
c = db.cursor()

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    s = "INSERT INTO users (username, password) VALUES (%s, %s)"
    c.execute(s, (username, password))
    db.commit()
    print("User registered successfully!")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    s = "SELECT password FROM users WHERE username = %s"
    c.execute(s, (username,))
    result = c.fetchone()
    if result:
        stored_password = result[0]
        if password == stored_password:
            print("Login successful!")
            return True  
        else:
            print("Incorrect password!")
    else:
        print("User not found!")
    return False

def add_task():
    task_name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low, Medium, High): ")
    s = "INSERT INTO tasks (task_name, description, due_date, priority) VALUES (%s, %s, %s, %s)"
    c.execute(s, (task_name, description, due_date, priority))
    db.commit()
    print("Task added successfully!")

def main():
    print("Welcome to Task Manager!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        register_user()
        main()
    elif choice == '2':
        if login_user():
            task_manager_menu()  
    elif choice == '3':
        print("Exiting...")
        c.close()
        db.close()
    else:
        print("Invalid option!")
        main()

def update_task_status():
    task_id = int(input("Enter task ID to update: "))
    status = input("Enter new status (Pending, In Progress, Completed): ")
    s = "UPDATE tasks SET status = %s WHERE task_id = %s"
    c.execute(s, (status, task_id))
    db.commit()

def modify_task():
    task_id = int(input("Enter task ID to modify: "))
    print("Select detail to modify: ")
    print("1. Task Name")
    print("2. Description")
    print("3. Priority")
    choice = input("Enter choice: ")

    if choice == '1':
        new_name = input("Enter new task name: ")
        s = "UPDATE tasks SET task_name = %s WHERE task_id = %s"
        c.execute(s, (new_name, task_id))
    elif choice == '2':
        new_description = input("Enter new description: ")
        s = "UPDATE tasks SET description = %s WHERE task_id = %s"
        c.execute(s, (new_description, task_id))
    elif choice == '3':
        new_priority = input("Enter new priority (Low, Medium, High): ")
        s = "UPDATE tasks SET priority = %s WHERE task_id = %s"
        c.execute(s, (new_priority, task_id))
    
    db.commit()
    print("Task updated successfully!")

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    s = "DELETE FROM tasks WHERE task_id = %s"
    c.execute(s, (task_id,))
    db.commit()
    print("Task deleted successfully!")

def mark_task_complete():
    task_id = int(input("Enter task ID to mark as complete: "))
    s = "UPDATE tasks SET status = 'Completed' WHERE task_id = %s"
    c.execute(s, (task_id,))
    db.commit()
    print("Task marked as complete!")

def view_overdue_tasks():
    today = datetime.today().date()
    s = "SELECT * FROM tasks WHERE due_date < %s AND status != 'Completed'"
    c.execute(s, (today,))
    tasks = c.fetchall()
    if tasks:
        print("\nOverdue Tasks:")
        for k in tasks:
            task_details = (
                "Task ID: " + str(k[0]) + ", "
                "Name: " + k[1] + ", "
                "Description: " + k[2] + ", "
                "Due Date: " + str(k[3]) + ", "
                "Status: " + k[4] + ", "
                "Priority: " + k[5]
                )
            print(task_details)
    else:
        print("No overdue tasks.")

def count_tasks_by_status():
    s = "SELECT status, COUNT(*) FROM tasks GROUP BY status"
    c.execute(s)
    counts = c.fetchall()
    print("\nTask Count by Status:")
    for status, count in counts:
        print(status + ": " + str(count) + " tasks")

def view_tasks():
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    for k in tasks:
        print(
            "Task ID: " + str(k[0]) + 
            ", Name: " + k[1] + 
            ", Description: " + k[2] + 
            ", Due Date: " + str(k[3]) + 
            ", Status: " + k[4] + 
            ", Priority: " + k[5]
        )
    
def search_task_by_name():
    search_term = input("Enter the task name to search: ")
    s = "SELECT * FROM tasks WHERE task_name LIKE %s"
    c.execute(s, ('%' + search_term + '%',))
    tasks = c.fetchall()
    if tasks:
        for k in tasks:
            print(
                "Task ID: " + str(k[0]) + 
                ", Name: " + k[1] + 
                ", Description: " + k[2] + 
                ", Due Date: " + str(k[3]) + 
                ", Status: " + k[4] + 
                ", Priority: " + k[5]
                )
    else:
        print("No tasks found with that name.")

def search_task_by_due_date():
    due_date = input("Enter the due date to search (YYYY-MM-DD): ")
    s = "SELECT * FROM tasks WHERE due_date = %s"
    c.execute(s, (due_date,))
    tasks = c.fetchall()
    if tasks:
        for k in tasks:
            print(
                "Task ID: " + str(k[0]) +
                ", Name: " + k[1] +
                ", Description: " + k[2] +
                ", Due Date: " + str(k[3]) +
                ", Status: " + k[4] +
                ", Priority: " + k[5]
                )
    else:
        print("No tasks found with that due date.")

def view_tasks_by_status():
    status = input("Enter status to filter by (Pending, In Progress, Completed): ")
    s = "SELECT * FROM tasks WHERE status = %s"
    c.execute(s, (status,))
    tasks = c.fetchall()
    if tasks:
        for k in tasks:
            print(
                "Task ID: " + str(k[0]) +
                ", Name: " + k[1] +
                ", Description: " + k[2] +
                ", Due Date: " + str(k[3]) +
                ", Status: " + k[4] +
                ", Priority: " + k[5]
                )
    else:
        print("No tasks found with status " + status + ".")

def check_deadline_alerts():
    today = datetime.today().date()
    alert_date = today + timedelta(days=3)  
    s = "SELECT * FROM tasks WHERE due_date <= %s AND status != 'Completed'"
    c.execute(s, (alert_date,))
    tasks = c.fetchall()
    if tasks:
        print("\nUpcoming deadlines:")
        for k in tasks:
            print(
                "Task ID: " + str(k[0]) +
                ", Name: " + k[1] +
                ", Due Date: " + str(k[3]) +
                ", Status: " + k[4]
                )
    else:
        print("No tasks have deadlines within the next 3 days.")

def sort_tasks():
    print("Sort by:")
    print("1. Due Date")
    print("2. Priority")
    choice = input("Enter your choice: ")

    if choice == '1':
        s = "SELECT * FROM tasks ORDER BY due_date"
    elif choice == '2':
        s = "SELECT * FROM tasks ORDER BY priority"
    else:
        print("Invalid choice!")
        return
    
    c.execute(s)
    tasks = c.fetchall()
    for k in tasks:
        print(
            "Task ID: " + str(k[0]) +
            ", Name: " + k[1] +
            ", Description: " + k[2] +
            ", Due Date: " + str(k[3]) +
            ", Status: " + k[4] +
            ", Priority: " + k[5]
            )

def task_manager_menu():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Update Task Status")
        print("3. Modify Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. View Overdue Tasks")
        print("7. Count Tasks by Status")
        print("8. View All Tasks")
        print("9. Search Task by Name")
        print("10. Search Task by Due Date")
        print("11. View Tasks by Status")
        print("12. Deadline Alerts")
        print("13. Sort Tasks")
        print("14. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            update_task_status()
        elif choice == '3':
            modify_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_task_complete()
        elif choice == '6':
            view_overdue_tasks()
        elif choice == '7':
            count_tasks_by_status()
        elif choice == '8':
            view_tasks()
        elif choice == '9':
            search_task_by_name()
        elif choice == '10':
            search_task_by_due_date()
        elif choice == '11':
            view_tasks_by_status()
        elif choice == '12':
            check_deadline_alerts()
        elif choice == '13':
            sort_tasks()
        elif choice == '14':
            break
        else:
            print("Invalid choice! Please try again.")
main()

c.close()
db.close()
