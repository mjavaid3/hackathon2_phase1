# Research: Todo App CLI Implementation

## Overview
This document captures the research and design decisions for implementing the command-line Todo application with in-memory storage.

## Key Design Decisions

### 1. Data Model: Task Dataclass
**Decision**: Use a Python dataclass for the Task entity
**Rationale**: Dataclasses provide a clean, readable way to define structured data with type hints. They automatically generate `__init__`, `__repr__`, and other methods, which aligns with the requirement for type hints and PEP 8 compliance.
**Alternatives considered**:
- Regular class: More verbose, requires manual implementation of `__init__` and other methods
- Named tuple: Immutable, which would complicate update operations
- Dictionary: Less structured, no type hints, more error-prone

### 2. Storage Implementation: InMemoryStorage Class
**Decision**: Implement a dedicated InMemoryStorage class to manage tasks
**Rationale**: Encapsulation of storage logic in a single class provides a clean interface for all CRUD operations. It maintains the in-memory requirement while providing a structured approach to data management.
**Alternatives considered**:
- Global variable: Poor encapsulation, harder to test, not object-oriented
- Module-level functions: Less organized than a dedicated class
- Multiple storage classes: Over-engineering for this simple application

### 3. Command Parsing: Manual String Splitting
**Decision**: Use manual string parsing rather than argparse or similar libraries
**Rationale**: The constitution specifies using only the Python standard library and avoiding CLI frameworks. Manual parsing with string operations is sufficient for the simple command structure required.
**Alternatives considered**:
- argparse: Would require more complex setup than needed for this simple CLI
- Regular expressions: Overkill for the simple parsing requirements
- Third-party libraries like Click or Typer: Explicitly prohibited by constitution

### 4. Command Dispatch: Dictionary-Based Router
**Decision**: Use a dictionary mapping command names to handler functions
**Rationale**: Provides a clean, extensible way to map user commands to functionality. Easy to understand and maintain.
**Alternatives considered**:
- If/elif chains: More difficult to extend and maintain
- Switch statements (Python 3.10+): Not available in all Python 3.12+ versions
- Class-based command pattern: Over-engineering for this simple application

### 5. CLI Loop: Interactive REPL
**Decision**: Implement a simple REPL (Read-Eval-Print Loop) in the main function
**Rationale**: Provides the interactive command prompt required by the specification. Simple to implement and understand.
**Alternatives considered**:
- Separate input processing modules: Would add unnecessary complexity
- Event-driven architecture: Overkill for this simple application

## Architecture Overview

### Module Structure
```
src/
└── todo_app/
    ├── __init__.py
    ├── main.py          # entry point with command loop
    ├── models.py        # Task class/dataclass
    ├── storage.py       # InMemoryStorage class
    └── cli.py           # Command parsing and handling
```

### Data Flow
1. User enters command at prompt in `main.py`
2. Command is parsed in `cli.py`
3. Appropriate handler function is called
4. Storage operations performed via `storage.py`
5. Results formatted and displayed to user

## Technology Constraints Compliance

### Python Standard Library Only
- All functionality implemented using built-in Python modules
- No external dependencies beyond stdlib
- Compatible with Python 3.12+

### Type Hints
- All functions, methods, and class attributes include type hints
- Uses Union types where appropriate (e.g., `str | None`)
- Follows PEP 484 type hinting standards

### PEP 8 Compliance
- Proper naming conventions (snake_case for functions/variables)
- Appropriate line lengths and whitespace
- Proper import organization
- Meaningful docstrings for modules, classes, and functions

## Error Handling Strategy

### Input Validation
- Validate command syntax before processing
- Check for required arguments
- Validate task IDs exist before operations
- Handle empty strings and special characters appropriately

### User-Friendly Messages
- Clear error messages for invalid commands
- Specific feedback for operations (e.g., "Task 1 updated successfully")
- Help text for available commands

## Testing Strategy

### Manual Verification Checklist
- [ ] Add task → list shows it with correct ID and status
- [ ] List command shows all tasks with proper formatting
- [ ] Update task → changes reflect in list
- [ ] Delete task → task no longer appears in list
- [ ] Complete/incomplete → status changes correctly
- [ ] Help command → shows all available commands
- [ ] Exit/quit command → application terminates cleanly
- [ ] Invalid command → shows error message
- [ ] Non-existent task ID → shows appropriate error
- [ ] Empty title/description → handles appropriately

### Edge Cases
- Very long task titles or descriptions
- Special characters in task content
- Commands with missing arguments
- Invalid command formats
- Attempting operations on non-existent tasks