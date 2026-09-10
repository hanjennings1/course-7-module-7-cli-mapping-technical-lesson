# lib/cli_tool.py

import argparse
# Import Task and User classes from models module
from models import Task, User

# Initialize an empty dictionary to store users
users = {}

# Define function to handle adding a task
def add_task(args):
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user
    task = Task(args.title)
    user.add_task(task)

# Define function to handle completing a task
def complete_task(args):
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return
    task = user.get_task_by_title(args.title)
    if task:
        task.complete()
    else:
        print("❌ Task not found.")

# Function to handle listing out the tasks and if completed
def list_tasks(args):
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return
    if not user.task:
        print(f"No tasks for {user.name}.")
        return
    for task in user.tasks:
        status = "✅" if task.completed else "⬜"
        print(f"{status} {task.title}")

# Function to handle deleting task(s)
def delete_task(args):
    user = users.get(args.user)
    if not user:
        print("❌ User not found.")
        return
    task = user.get_task_by_title(args.title)
    if task:
        user.tasks.remove(task)
        print(f"🗑️ Task '{task.title}' deleted.")
    else:
        print(f"❌ Task not found.")


def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for add-task
    add_parser = subparsers.add_parser("add-task", help="Add a task to a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Subparser for complete-task
    complete_parser = subparsers.add_parser("complete-task", help="Complete a task for a user")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    # Suparser for list-tasks
    list_parser = subparsers.add_parser("list-tasks", help="List all tasks for a user")
    list_parser.add_argument("user")
    list_parser.set_defaults(func=list_tasks)

    # Subparser for delete-task
    delete_parser = subparsers.add_parser("delete-task", help="Delete a task from a user")
    delete_parser.add_argument("user")
    delete_parser.add_argument("title")
    delete_parser.set_defaults(func=delete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
