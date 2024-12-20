def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks in your to-do list.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def to_do_list():
    tasks = []

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
        elif choice == '2':
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                show_tasks(tasks)
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    tasks.pop(task_num - 1)
                    print(f"Task {task_num} removed.")
                else:
                    print("Invalid task number.")
        elif choice == '3':
            show_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


to_do_list()
