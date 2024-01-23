#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{i}. {task['description']} - {status}")

def add_task(tasks, description):
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task '{description}' added.")

def mark_completed(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]['completed'] = True
        print(f"Task marked as completed: {tasks[index - 1]['description']}")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            mark_completed(tasks, index)
        elif choice == '4':
            save_tasks(tasks)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




