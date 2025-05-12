import os # Provides OS-level file and directory operations
import shlex # Parses shell-like syntax into Python objects
from utils.colors import color_text, Colors # Imports a custom Colors class for colored terminal output


class PyKernel: # Defines a class to represent the kernel
    """
    A simple Python kernel that provides a command-line interface for basic shell commands.
    It supports commands like 'cd', 'ls', 'echo', and 'cat'.
    """
    def __init__(self): # Constructor to initialize the kernel
        self.running = True # Controls the shell/main loop
        self.cwd = os.getcwd() # Stores the current working directory (starts in the directory where the script is run)

    def run(self): # REPL loop (Read-Eval-Print Loop)
        while self.running: # Continuously runs until the user exits
            try:
                cmd = input(color_text(self.cwd, Colors.OKCYAN) + color_text(" > ", Colors.BOLD)) # Prompts the user for input and displays the current working directory
                self.execute(cmd) # Executes the command
            except (KeyboardInterrupt, EOFError): # Handles Ctrl+C and EOF (Ctrl+D) gracefully
                print(color_text("\nExiting...", Colors.WARNING)) # Prints a message when exiting
                break # Exits the loop
            except Exception as e: # Catches any other exceptions
                print(color_text("ERROR: ", Colors.FAIL) + color_text(e, Colors.WARNING)) # Prints the error message
                break # Exits the loop

    def execute(self, cmd): # Executes the command entered by the user
        if not cmd.strip(): # Checks if the command is empty
            return # If empty, do nothing
        tokens = shlex.split(cmd) # Splits the command into tokens (words) using shell-like syntax
        command = tokens[0] # The first token is the command
        args = tokens[1:] # The rest are the arguments

        # Match the command and execute the corresponding function
        match command:
            case "exit":
                self.running = False
            case "cd": # Change directory
                self.cd(args)
            case "ls": # List directory contents
                self.ls(args)
            case "echo": # Print arguments to the console
                print(" ".join(args))
            case "cat": # Concatenate and display file contents
                self.cat(args)
            case _: # Default case for unknown commands
                print(color_text("Unknown command: ", Colors.FAIL) + color_text(command, Colors.WARNING)) # Prints an error message for unknown commands

    def cd(self, args): # Change directory function
        if not args: # Checks if no arguments are provided
            print(color_text("cd: ", color=Colors.OKCYAN) + color_text("missing operand", Colors.WARNING)) # Prints an error message
            return
        try: # Attempts to change the directory
            new_dir = os.path.abspath(os.path.join(self.cwd, args[0])) # Converts the relative path to an absolute path
            os.chdir(new_dir) # Changes the current working directory
            self.cwd = new_dir # Updates the cwd attribute
        except Exception as e: # Catches any exceptions (like directory not found)
            print(color_text("cd: ", Colors.OKCYAN), color_text(e, Colors.FAIL)) # Prints the error message
            self.cwd = os.getcwd() # Resets cwd to the original directory if an error occurs

    def ls(self, args): # List directory contents function
        try:
            path = self.cwd if not args else args[0] # If no arguments, use current directory
            for f in os.listdir(path): # Lists files in the directory
                print(color_text(f, Colors.OKBLUE)) # Prints each file
        except Exception as e: # Catches any exceptions (like directory not found)
            print(color_text(f"ls: {e}", Colors.FAIL)) # Prints the error message

    def cat(self, args): # Concatenate and display file contents function
        if not args: # Checks if no arguments are provided
            print(color_text("cat: ", Colors.OKCYAN), color_text("missing operand", Colors.WARNING)) # Prints an error message
            return
        for filename in args: # Iterates through each file provided
            try:
                with open(filename, "r") as f: # Attempts to open the file
                    print(color_text(f, Colors.OKBLUE)) # Reads and prints the file contents
            except Exception as e: # Catches any exceptions (like file not found)
                print(color_text("cat: ", Colors.OKCYAN), color_text(e, Colors.FAIL))

if __name__ == "__main__": # Ensures the script runs only when executed directly
    PyKernel().run() # Create an instance of the PyKernel class and run it
