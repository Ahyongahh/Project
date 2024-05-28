def main():
    tasks = []

    while True:
        print("\n====== To-Do List ======")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your Choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many task do you want to add?"))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("task added!")

        #Choice 2
        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        #Choice 3
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Tasks Marked as Done!")
            else:
                print("Invalid Task Number")

        #Choice 4
        elif choice == '4':
            print("Exiting to-do list")
            break

        #Wrong Number
        else:
            print("invalid choice number")

#What's this?
if __name__ == "__main__":
        main()