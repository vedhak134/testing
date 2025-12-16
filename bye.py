import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})

def list_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")

def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def main():
    tasks = load_tasks()
    while True:
        print("\n(a)dd (l)ist (d)one (q)uit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            title = input("Task title: ")
            add_task(tasks, title)
            save_tasks(tasks)

        elif choice == "l":
            list_tasks(tasks)

        elif choice == "d":
            index = int(input("Task number: ")) - 1
            mark_done(tasks, index)
            save_tasks(tasks)

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
