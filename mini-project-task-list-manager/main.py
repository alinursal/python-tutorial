import os

# Function to add tasks to the list
def add_task(task_list, task):
    task_list.append(task)
    print(f'Task added: "{task}"')

# Function to remove completed tasks
def remove_task(task_list, task):
    try:
        task_list.remove(task)
        print(f'Task removed: "{task}"')
    except ValueError:
        print(f'Task "{task}" not found in the list.')

# Function to view the current task list
def view_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        print("Current Task List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

# Function to save tasks to a file
def save_tasks(task_list, filename):
    try:
        with open(filename, 'w') as file:
            for task in task_list:
                file.write(task + '\n')
        print(f'Tasks saved to {filename}.')
    except IOError as e:
        print(f'Error saving tasks: {e}')

# Function to load tasks from a file
def load_tasks(filename):
    task_list = []
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                task_list = [line.strip() for line in file.readlines()]
            print(f'Tasks loaded from {filename}.')
        else:
            print(f'File {filename} does not exist.')
    except IOError as e:
        print(f'Error loading tasks: {e}')
    return task_list

# Example usage
def main():
    task_list = []

    # Load existing tasks from a file
    task_list = load_tasks('tasks.txt')

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task_list, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task_list, task)
        elif choice == '3':
            view_tasks(task_list)
        elif choice == '4':
            save_tasks(task_list, 'tasks.txt')
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()