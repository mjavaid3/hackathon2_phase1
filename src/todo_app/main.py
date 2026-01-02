"""
Main module for the Todo App CLI.
Implements the interactive REPL loop.
"""
from cli import TodoAppCLI


def main():
    """
    Entry point for the Todo App CLI.
    Starts the interactive command loop.
    """
    cli = TodoAppCLI()
    cli.run()


if __name__ == "__main__":
    main()