# Quickstart Guide: Todo App CLI

## Overview
This guide provides instructions for setting up and using the command-line Todo application.

## Prerequisites
- Python 3.12 or higher
- UV package manager (for dependency management)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone [repository-url]
cd [repository-name]
```

### 2. Install Dependencies
```bash
uv sync
```

### 3. Run the Application
```bash
cd src/todo_app
python main.py
```

## Usage Instructions

### Starting the Application
Run the application using the command above. You will see a prompt like:
```
> 
```

### Available Commands

#### Add a Task
Add a new task with a title and optional description:
```
> add "Task title" "Task description (optional)"
```

Example:
```
> add "Buy groceries" "Milk, bread, eggs"
Task added successfully with ID 1
```

#### List All Tasks
View all tasks in your list:
```
> list
```

Example output:
```
ID  | Title            | Description      | Status
----|------------------|------------------|--------
1   | Buy groceries    | Milk, bread, eggs| [ ]
2   | Finish report    |                  | [x]
```

#### Update a Task
Update the title or description of an existing task:
```
> update <task_id> "New title" "New description (optional)"
```

Examples:
```
> update 1 "Buy groceries and cook dinner"
Task 1 updated successfully

> update 1 "Buy groceries and cook dinner" "Milk, bread, eggs, chicken, vegetables"
Task 1 updated successfully
```

#### Delete a Task
Remove a task permanently:
```
> delete <task_id>
```

Example:
```
> delete 1
Task 1 deleted successfully
```

#### Mark Task as Complete
Mark a task as completed:
```
> complete <task_id>
```

Example:
```
> complete 1
Task 1 marked as complete
```

#### Mark Task as Incomplete
Mark a completed task as incomplete again:
```
> incomplete <task_id>
```

Example:
```
> incomplete 1
Task 1 marked as incomplete
```

#### Get Help
View all available commands:
```
> help
```

#### Exit the Application
Quit the application:
```
> exit
```
or
```
> quit
```

## Example Workflow

1. Add some tasks:
```
> add "Finish project proposal" "Complete the proposal document for client"
Task added successfully with ID 1

> add "Buy groceries"
Task added successfully with ID 2
```

2. View your tasks:
```
> list
ID  | Title                  | Description                    | Status
----|------------------------|--------------------------------|--------
1   | Finish project proposal| Complete the proposal document | [ ]
    |                        | for client                     | 
2   | Buy groceries          |                                | [ ]
```

3. Mark a task as complete:
```
> complete 2
Task 2 marked as complete
```

4. Update a task:
```
> update 1 "Finish and submit project proposal"
Task 1 updated successfully
```

5. Exit the application:
```
> exit
```

## Troubleshooting

### Common Issues
- **Command not recognized**: Make sure you're using the correct command syntax
- **Invalid task ID**: Verify the task ID exists before trying to update, delete, or mark complete
- **Empty title**: All tasks must have a title

### Error Messages
- "Error: Task with ID [X] not found" - The specified task ID does not exist
- "Error: Title cannot be empty" - All tasks must have a title
- "Error: Invalid command format" - Check the command syntax