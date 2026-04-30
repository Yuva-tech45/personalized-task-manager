import datetime

class Task: 
    def __init__(self, title, description, due_date): 
        self.title = title 
        self.description = description 
        self.due_date = due_date 
        self.created_at = datetime.datetime.now()
        self.status = 'Not Yet Started'

class TaskManager: 
    def __init__(self): 
        self.tasks = [] 

    def add_task(self, title, description, due_date): 
        self.tasks.append(Task(title, description, due_date)) 
        print("Task added successfully!") 

    def delete_task(self, index): 
        if 0 <= index < len(self.tasks): 
            del self.tasks[index]           
            print("Task deleted successfully!") 
        else: 
            print("Invalid task index.") 

    def display_tasks(self):                                     
        if not self.tasks: 
            print("No tasks found.") 
        else: 
            for i, task in enumerate(self.tasks, 1): 
                print("Task:" + str(i))
                print("Title:" + task.title)
                print("Description:" + task.description)
                print("Due Date:" + str(task.due_date))
                print("Created At:" + str(task.created_at))
                print("Status:" + task.status)
                print()

    def update_task_status(self, index, status):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = status
            print("Task status updated successfully!")
        else:
            print("Invalid task index.")
    
    def display_tasks_by_status(self):
        completed_tasks = [i+1 for i, task in enumerate(self.tasks) if task.status == 'Completed']
        ongoing_tasks = [i+1 for i, task in enumerate(self.tasks) if task.status == 'Ongoing']
        not_started_tasks = [i+1 for i, task in enumerate(self.tasks) if task.status == 'Not Yet Started']
        
        print(datetime.datetime.now())
        
        print("COMPLETED TASK")
        print(','.join(map(str, completed_tasks)) if completed_tasks else "None")
        
        print("ONGOING TASK")
        print(','.join(map(str, ongoing_tasks)) if ongoing_tasks else "None")
        
        print("NOT YET STARTED")
        print(','.join(map(str, not_started_tasks)) if not_started_tasks else "None")

def main(): 
    task_manager = TaskManager() 

    while True: 
        print("1. Add Task") 
        print("2. Delete Task") 
        print("3. View Tasks") 
        print("4. Update Task Status")
        print("5. Display Tasks by Status")
        print("6. Exit") 

        choice = input("Enter your choice: ") 

        if choice == '1': 
            title = input("Enter task title: ") 
            description = input("Enter task description: ") 
            due_date = input("Enter due date (YYYY-MM-DD): ") 
            task_manager.add_task(title, description, due_date) 
        elif choice == '2': 
            index = int(input("Enter index of task to delete: ")) - 1 
            task_manager.delete_task(index) 
        elif choice == '3': 
            task_manager.display_tasks() 
        elif choice == '4': 
            index = int(input("Enter index of task to update status: ")) - 1
            print("Choose status: 1. Not Yet Started 2. Ongoing 3. Completed")
            status_choice = input("Enter status choice: ")
            status_dict = {'1': 'Not Yet Started', '2': 'Ongoing', '3': 'Completed'}
            status = status_dict.get(status_choice, 'Not Yet Started')
            task_manager.update_task_status(index, status)
        elif choice == '5': 
            task_manager.display_tasks_by_status()
        elif choice == '6': 
            print("Exiting...") 
            break 
        else: 
            print("Invalid choice. Please try again.") 

if __name__ == "__main__": 
    main()

