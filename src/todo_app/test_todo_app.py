#!/usr/bin/env python3
"""
Test script for the Todo App CLI.
This script tests the main functionality of the application.
"""

import sys
import os

# Add the current directory to the path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli import TodoAppCLI
from models import Task
from storage import InMemoryStorage


def test_basic_functionality():
    """Test the basic functionality of the TodoAppCLI."""
    print("Testing basic functionality...")
    
    # Create a CLI instance
    cli = TodoAppCLI()
    
    # Test adding a task
    print("\n1. Testing add command:")
    cli.handle_add(["Sample Task", "This is a sample task description"])
    
    # Test listing tasks
    print("\n2. Testing list command:")
    cli.handle_list([])
    
    # Test adding another task
    print("\n3. Testing add command with just title:")
    cli.handle_add(["Another Task"])
    
    # Test listing tasks again
    print("\n4. Testing list command again:")
    cli.handle_list([])
    
    # Test updating a task
    print("\n5. Testing update command:")
    cli.handle_update(["1", "Updated Sample Task", "Updated description"])
    
    # Test listing tasks after update
    print("\n6. Testing list command after update:")
    cli.handle_list([])
    
    # Test marking a task as complete
    print("\n7. Testing complete command:")
    cli.handle_complete(["1"])
    
    # Test listing tasks after marking as complete
    print("\n8. Testing list command after marking complete:")
    cli.handle_list([])
    
    # Test deleting a task
    print("\n9. Testing delete command:")
    cli.handle_delete(["2"])
    
    # Test listing tasks after deletion
    print("\n10. Testing list command after deletion:")
    cli.handle_list([])
    
    print("\nAll tests completed successfully!")


if __name__ == "__main__":
    test_basic_functionality()