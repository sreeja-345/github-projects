# Simple To-Do List App

tasks = []

def show_menu():
    print("\n==== TO-DO LIST ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            status = "✅ Done" if t["done"] else "❌ Not Done"
            print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        task_num = int(input("Enter task number to mark as done: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting... Bye 👋")
        break

    else:
        print("Invalid choice. Try again!")
