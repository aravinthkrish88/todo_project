# Simple To-Do List Program
# Program to manage daily tasks: add, view, mark done, delete

tasks = []  # List to store all tasks

while True:
    # Display menu
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    # Ask user to choose an option
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Add a new task
        task = input("Enter new task: ")
        tasks.append({"task": task, "done": False})
        print("✅ Task added.")

    elif choice == "2":
        # View all tasks
        if not tasks:
            print("📭 No tasks available.")
        else:
            for i, t in enumerate(tasks, 1):
                status = "✅ Done" if t["done"] else "❌ Not Done"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        # Mark a task as done
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("⚠ Invalid task number.")

    elif choice == "4":
        # Delete a task
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("🗑 Task deleted.")
        else:
            print("⚠ Invalid task number.")

    elif choice == "5":
        # Exit program
        print("👋 Exiting... Bye!")
        break

    else:
        # Handle invalid input
        print("⚠ Invalid choice. Try again.")
