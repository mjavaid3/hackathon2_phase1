"""
Models module for the Todo App CLI.
Contains the Task dataclass definition.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item in the application.
    
    Attributes:
        id: Unique incremental identifier for the task (starting from 1)
        title: The title or name of the task
        description: Optional detailed description of the task (default: None)
        completed: Status indicator showing if the task is completed (default: False)
    """
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False