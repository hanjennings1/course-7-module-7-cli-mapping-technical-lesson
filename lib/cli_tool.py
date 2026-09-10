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

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
