# Command Contracts: Todo App CLI

## Overview
This document defines the command contracts for the command-line Todo application.

## Command Structure
All commands follow the format: `[command] [arguments]`

## Commands

### 1. Add Command
**Command**: `add`
**Arguments**: `title` (required), `description` (optional)
**Format**: `add "title" ["description"]`
**Description**: Creates a new task with the given title and optional description.
**Response**: 
- Success: "Task added successfully with ID [ID]"
- Error: "Error: [error message]"

**Examples**:
- `add "Buy groceries" "Milk, bread, eggs"`
- `add "Finish report"`

### 2. List Command
**Command**: `list`
**Arguments**: None
**Format**: `list`
**Description**: Displays all tasks with their ID, Title, Description (if any), and Status.
**Response**: 
- Success: Formatted table of all tasks
- Error: "No tasks found." (if no tasks exist)

### 3. Update Command
**Command**: `update`
**Arguments**: `id` (required), `new_title` (optional), `new_description` (optional)
**Format**: `update <id> ["new_title"] ["new_description"]`
**Description**: Updates the title and/or description of the task with the given ID.
**Response**: 
- Success: "Task [ID] updated successfully"
- Error: "Error: [error message]"

**Examples**:
- `update 1 "Buy groceries and cook dinner"`
- `update 2 "Buy groceries" "Milk, bread, eggs, chicken"`

### 4. Delete Command
**Command**: `delete`
**Arguments**: `id` (required)
**Format**: `delete <id>`
**Description**: Permanently removes the task with the given ID.
**Response**: 
- Success: "Task [ID] deleted successfully"
- Error: "Error: [error message]"

**Example**: `delete 1`

### 5. Complete Command
**Command**: `complete`
**Arguments**: `id` (required)
**Format**: `complete <id>`
**Description**: Marks the task with the given ID as complete.
**Response**: 
- Success: "Task [ID] marked as complete"
- Error: "Error: [error message]"

**Example**: `complete 1`

### 6. Incomplete Command
**Command**: `incomplete`
**Arguments**: `id` (required)
**Format**: `incomplete <id>`
**Description**: Marks the task with the given ID as incomplete.
**Response**: 
- Success: "Task [ID] marked as incomplete"
- Error: "Error: [error message]"

**Example**: `incomplete 1`

### 7. Help Command
**Command**: `help`
**Arguments**: None
**Format**: `help`
**Description**: Displays all available commands with brief descriptions.
**Response**: 
- Success: List of all commands with descriptions

### 8. Exit/Quit Commands
**Commands**: `exit` or `quit`
**Arguments**: None
**Format**: `exit` or `quit`
**Description**: Terminates the application gracefully.
**Response**: 
- Success: Application exits