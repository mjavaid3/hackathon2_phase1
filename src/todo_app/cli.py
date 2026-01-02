"""
CLI module for the Todo App CLI.
Contains the command-line interface implementation.
"""
import re
from typing import List, Optional
try:
    from .models import Task
    from .storage import InMemoryStorage
except ImportError:
    # When running directly as a script
    from models import Task
    from storage import InMemoryStorage


class TodoAppCLI:
    """
    Command-line interface for the Todo App.
    Handles user commands and interacts with storage.
    """

    def __init__(self):
        """
        Initialize the CLI with storage and command handlers.
        """
        self.storage = InMemoryStorage()
        self.command_handlers = {
            'add': self.handle_add,
            'list': self.handle_list,
            'update': self.handle_update,
            'delete': self.handle_delete,
            'complete': self.handle_complete,
            'incomplete': self.handle_incomplete,
            'help': self.handle_help,
            'exit': self.handle_exit,
            'quit': self.handle_exit
        }
        self.running = True

    def run(self):
        """
        Run the main REPL loop.
        """
        print("Welcome to the Todo App CLI!")
        print("Type 'help' for available commands or 'exit' to quit.")

        while self.running:
            try:
                command_input = input("> ").strip()
                if not command_input:
                    continue

                # Parse the command and arguments
                parts = self.parse_command(command_input)
                if not parts:
                    print("Invalid command format. Type 'help' for available commands.")
                    continue

                command = parts[0].lower()
                args = parts[1:]

                if command in self.command_handlers:
                    self.command_handlers[command](args)
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")

            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except EOFError:
                print("\nExiting...")
                break

    def parse_command(self, command_input: str) -> List[str]:
        """
        Parse a command string into command and arguments.
        Handles quoted arguments.

        Args:
            command_input: The full command string from user

        Returns:
            List with command as first element and arguments following
        """
        # Regular expression to match quoted strings or individual words
        pattern = r'"([^"]*)"|\'([^\']*)\'|(\S+)'
        matches = re.findall(pattern, command_input)

        # Each match is a tuple of (double_quoted, single_quoted, unquoted)
        parts = [match[0] or match[1] or match[2] for match in matches]
        return parts

    def handle_add(self, args: List[str]):
        """
        Handle the 'add' command.
        Usage: add "title" ["description"]

        Args:
            args: List of arguments for the add command
        """
        if len(args) < 1:
            print("Usage: add \"title\" [\"description\"]")
            return

        title = args[0]
        description = args[1] if len(args) > 1 else None

        if not title:
            print("Error: Title cannot be empty")
            return

        task = self.storage.add_task(title, description)
        print(f"Task added successfully with ID {task.id}")

    def handle_list(self, args: List[str]):
        """
        Handle the 'list' command.
        Usage: list

        Args:
            args: List of arguments for the list command (should be empty)
        """
        if args:
            print("Usage: list")
            return

        tasks = self.storage.list_tasks()

        if not tasks:
            print("No tasks found.")
            return

        # Print header
        print(f"{'ID':<4} | {'Title':<20} | {'Description':<30} | {'Status'}")
        print("-" * 65)

        # Print each task
        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            description = task.description if task.description else ""
            # Truncate long titles or descriptions
            title = task.title[:17] + "..." if len(task.title) > 20 else task.title
            desc = description[:27] + "..." if len(description) > 30 else description
            print(f"{task.id:<4} | {title:<20} | {desc:<30} | {status}")

    def handle_update(self, args: List[str]):
        """
        Handle the 'update' command.
        Usage: update <id> ["new_title"] ["new_description"]

        Args:
            args: List of arguments for the update command
        """
        if len(args) < 2:
            print("Usage: update <id> [\"new_title\"] [\"new_description\"]")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            print("Error: Task ID must be a number")
            return

        # Find the task
        task = self.storage.get_task(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return

        # Prepare update parameters
        title = args[1] if len(args) > 1 and args[1] else None
        description = args[2] if len(args) > 2 and args[2] else None

        # At least one field must be provided for update
        if title is None and description is None:
            print("Error: At least one field (title or description) must be provided for update")
            return

        updated_task = self.storage.update_task(task_id, title, description)
        if updated_task:
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Error: Failed to update task {task_id}")

    def handle_delete(self, args: List[str]):
        """
        Handle the 'delete' command.
        Usage: delete <id>

        Args:
            args: List of arguments for the delete command
        """
        if len(args) != 1:
            print("Usage: delete <id>")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            print("Error: Task ID must be a number")
            return

        success = self.storage.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def handle_complete(self, args: List[str]):
        """
        Handle the 'complete' command.
        Usage: complete <id>

        Args:
            args: List of arguments for the complete command
        """
        if len(args) != 1:
            print("Usage: complete <id>")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            print("Error: Task ID must be a number")
            return

        success = self.storage.complete_task(task_id)
        if success:
            print(f"Task {task_id} marked as complete")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def handle_incomplete(self, args: List[str]):
        """
        Handle the 'incomplete' command.
        Usage: incomplete <id>

        Args:
            args: List of arguments for the incomplete command
        """
        if len(args) != 1:
            print("Usage: incomplete <id>")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            print("Error: Task ID must be a number")
            return

        success = self.storage.incomplete_task(task_id)
        if success:
            print(f"Task {task_id} marked as incomplete")
        else:
            print(f"Error: Task with ID {task_id} not found")

    def handle_help(self, args: List[str]):
        """
        Handle the 'help' command.
        Usage: help

        Args:
            args: List of arguments for the help command (should be empty)
        """
        if args:
            print("Usage: help")
            return

        print("Available commands:")
        print("  add \"title\" [\"description\"]    - Add a new task")
        print("  list                           - List all tasks")
        print("  update <id> [\"title\"] [\"desc\"] - Update a task")
        print("  delete <id>                    - Delete a task")
        print("  complete <id>                  - Mark task as complete")
        print("  incomplete <id>                - Mark task as incomplete")
        print("  help                           - Show this help message")
        print("  exit/quit                      - Exit the application")

    def handle_exit(self, args: List[str]):
        """
        Handle the 'exit' or 'quit' command.
        Usage: exit or quit

        Args:
            args: List of arguments for the exit command (should be empty)
        """
        if args:
            print("Usage: exit or quit")
            return

        print("Goodbye!")
        self.running = False