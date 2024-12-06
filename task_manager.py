tasks = [] #List to store tasks
TASK_FILE = "tasks.txt" # File to save tasks

def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Sort Tasks by Priority")
    print("5. Exit")

def add_task():
    task_description = input("Enter the task: ")
    priority = input("Enter the priority (High, Medium, Low): ").capitalize()
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority! Defaulting to 'Medium'.")
        priority = "Medium"
    task = {"description": task_description, "priority": priority}
    tasks.append(task)
    print(f'Task "{task_description}" with priority "{priority}" added successfully!')

def view_task():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. [{task['priority']}] {task['description']}")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
    else:
        view_task()
        try:
            task_number = int(input("Enter the number of the task to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f'Task "{removed_task}" deleted successfully!')
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def sort_tasks_by_priority():
    """Sort tasks by priority: High > Medium > Low."""
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(tasks, key=lambda task: priority_order[task["priority"]])
    tasks.clear()
    tasks.extend(sorted_tasks)
    print("Tasks sorted by priority!")

def load_task():
    """Load tasks from the file"""
    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                task_description, priority = line.strip().split(" | ")
                tasks.append({"description": task_description, "priority": priority})
        print(f"Loaded {len(tasks)} tasks from {TASK_FILE}.")
    except FileNotFoundError:
        print(f"no existing task file found. Starting fresh.")

def save_task():
    """Save tasks to the file"""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['description']} | {task['priority']}\n")
    print(f"Tasks saved to {TASK_FILE}.")


def main():
    load_task()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            sort_tasks_by_priority()
        elif choice == "5":
            save_task()
            print("Exiting Task Manager.Goodbye!")
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()