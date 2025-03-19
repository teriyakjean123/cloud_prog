import time


tasks = []

def add_task():
    task_name = input("Enter task name: ")
    task_time = input("Enter task time in seconds: ")
    
    if not task_time.isdigit():
        print("Invalid time. Please enter a number.")
        return
    
    task = {"name": task_name, "time": int(task_time)}
    tasks.append(task)
    print("Task added successfully!")

def run_scheduler():
    """Function to execute tasks in order."""
    print("Task scheduler started!")

    while tasks:
        task = tasks.pop(0)  # Remove the first task in the list
        print(f"Running task: {task['name']}")
        time.sleep(task["time"])  # Pause execution for task duration
        print(f"Task {task['name']} completed!")
