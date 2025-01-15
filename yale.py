import datetime

class Task:
    """Represents a single task in the to-do list."""
    def __init__(self, title, description, due_date):
        self.id = datetime.datetime.now().timestamp()  # Unique ID based on timestamp
        self.title = title
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_complete(self):
        """Marks the task as completed."""
        self.is_completed = True

    def __str__(self):
        status = "✔" if self.is_completed else "✘"
        return f"[{status}] {self.title} (Due: {self.due_date})\n    {self.description}"


class ToDoList:
    """Manages a collection of tasks."""
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        """Adds a new task to the list."""
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)

    def delete_task(self, task_id):
        """Deletes a task by its ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def mark_task_complete(self, task_id):
        """Marks a task as complete by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                break

    def view_tasks(self):
        """Returns a formatted string of all tasks."""
        if not self.tasks:
            return "No tasks available."
        result = ""
        for index, task in enumerate(self.tasks, start=1):
            result += f"{index}. {task}\n"
        return result


# App Logic
def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(title, description, due_date)
            print("Task added successfully!")
        elif choice == "2":
            print("\nYour Tasks:")
            print(todo_list.view_tasks())
        elif choice == "3":
            task_index = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= task_index < len(todo_list.tasks):
                todo_list.mark_task_complete(todo_list.tasks[task_index].id)
                print("Task marked as complete!")
            else:
                print("Invalid task number!")
        elif choice == "4":
            task_index = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_index < len(todo_list.tasks):
                todo_list.delete_task(todo_list.tasks[task_index].id)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
