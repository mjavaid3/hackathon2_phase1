# Data Model: Todo App CLI

## Overview
This document defines the data structures and models for the command-line Todo application.

## Core Entities

### Task
The Task entity represents a single todo item in the application.

**Fields**:
- `id`: int - Unique incremental identifier for the task (starting from 1)
- `title`: str - The title or name of the task
- `description`: str | None - Optional detailed description of the task (default: None)
- `completed`: bool - Status indicator showing if the task is completed (default: False)

**Dataclass Definition**:
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
```

**Validation Rules**:
- `id` must be a positive integer
- `title` must not be empty or None
- `description` can be None or a string of any length
- `completed` must be a boolean value

**State Transitions**:
- A task starts with `completed=False`
- A task can transition from `completed=False` to `completed=True` using the "complete" command
- A task can transition from `completed=True` to `completed=False` using the "incomplete" command

### TaskList
The TaskList represents the collection of all tasks in the application.

**Structure**:
- Implemented as a Python list of Task objects
- Maintains order of insertion
- Supports operations: add, remove, update, retrieve by ID

**Operations**:
- `add_task(task: Task)`: Add a new task to the list
- `get_task(task_id: int) -> Task | None`: Retrieve a task by its ID
- `update_task(task_id: int, **kwargs)`: Update specific fields of a task
- `delete_task(task_id: int) -> bool`: Remove a task by its ID (returns True if successful)
- `get_all_tasks() -> list[Task]`: Retrieve all tasks in the list
- `get_next_id() -> int`: Get the next available ID for a new task

## Storage Model

### InMemoryStorage
The InMemoryStorage class manages the collection of tasks in memory.

**Attributes**:
- `tasks`: list[Task] - Internal storage of Task objects
- `next_id`: int - The next ID to assign to a new task (starts at 1)

**Methods**:
- `add_task(title: str, description: str | None = None) -> Task`: Create and add a new task
- `list_tasks() -> list[Task]`: Return all tasks
- `update_task(task_id: int, title: str | None = None, description: str | None = None) -> Task | None`: Update a task
- `delete_task(task_id: int) -> bool`: Delete a task by ID
- `complete_task(task_id: int) -> bool`: Mark a task as complete
- `incomplete_task(task_id: int) -> bool`: Mark a task as incomplete
- `get_task(task_id: int) -> Task | None`: Get a specific task by ID

## Relationships
- Each Task exists independently within the TaskList
- Task IDs are unique within the application session
- No complex relationships between tasks are required