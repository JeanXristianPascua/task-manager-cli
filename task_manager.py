def display_menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            print("Feature to add task comming soon...")
        elif choice == "2":
            print("Feature to view tasks comming soon...")
        elif choice == "3":
            print("Feature to delete task comming soon...")
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else: 
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    

