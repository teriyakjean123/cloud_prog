from scheduler import add_task, run_scheduler

def main():
    """Main function to handle user input."""
    while True:
        print("Task Scheduler Menu:")
        print("1. Add a task")
        print("2. Run scheduler")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            run_scheduler()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
