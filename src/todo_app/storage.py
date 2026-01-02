"""
Storage module for the Todo App CLI.
Contains the InMemoryStorage class for managing tasks in memory.
"""
from typing import List, Optional
try:
    from .models import Task
except ImportError:
    # When running directly as a script
    from models import Task


class InMemoryStorage:
    """
    Manages the collection of tasks in memory.

    Attributes:
        tasks: Internal storage of Task objects
        next_id: The next ID to assign to a new task (starts at 1)
    """

    def __init__(self):
        """
        Initialize the in-memory storage with an empty task list and starting ID of 1.
        """
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Create and add a new task.

        Args:
            title: The title of the task
            description: Optional description of the task

        Returns:
            The newly created Task object
        """
        task = Task(id=self.next_id, title=title, description=description, completed=False)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        """
        Return all tasks.

        Returns:
            List of all Task objects
        """
        return self.tasks

    def update_task(self, task_id: int, title: Optional[str] = None,
                    description: Optional[str] = None) -> Optional[Task]:
        """
        Update a task with the given ID.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            Updated Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if task was deleted, False if not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: ID of the task to mark complete

        Returns:
            True if task was marked complete, False if not found
        """
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False

    def incomplete_task(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: ID of the task to mark incomplete

        Returns:
            True if task was marked incomplete, False if not found
        """
        for task in self.tasks:
            if task.id == task_id:
                task.completed = False
                return True
        return False

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            The next available ID
        """
        return self.next_id