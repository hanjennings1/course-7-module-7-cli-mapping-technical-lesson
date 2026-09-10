# lib/models.py

# Define a Task class
class Task:
    def __init__(self, title):
        # Store the title
        self.title = title
        # Initialize completed state to False
        self.completed = False

    def complete(self):
        # Set completed to True
        self.completed  = True
        # Print confirmation message
        print(f"✅ Task '{title}' completed.")


# Define a User class
class User:
    def __init__(self, name):
        # Store the user's name
        self.name = name
        # Initialize an empty task list
        self.tasks = []

    def add_task(self, task):
        # Append task to the user's task list
        self.tasks.append(task)
        # Print confirmation message
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # Return the task matching the title if it exists
        for task in self.tasks:
            if task.title == title:
                return task
        # Return None if not found
        return None
