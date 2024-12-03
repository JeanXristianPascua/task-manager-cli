tasks = [] #List to store tasks

def display_menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f'Task "{task}" added successfully!')

def view_task():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

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

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()