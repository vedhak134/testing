import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {
        "title": title,
        "description": description,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['title']}")

def view_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Select task number: ")) - 1
        task = tasks[index]
        print("\nTitle:", task["title"])
        print("Description:", task["description"])
        print("Completed:", task["completed"])
        print("Created At:", task["created_at"])
    except (IndexError, ValueError):
        print("Invalid selection.")

def complete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Task number to complete: ")) - 1
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid selection.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
    except (IndexError, ValueError):
        print("Invalid selection.")

def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. View Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            view_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
