import os # Provides OS-level file and directory operations
import shlex # Parses shell-like syntax into Python objects
from utils.colors import color_text, Colors # Imports a custom Colors class for colored terminal output
from utils.io import prompt, print_error, print_warning, print_success # Imports a custom prompt function for displaying the command line prompt
from utils.fs import is_dir, list_dir, read_file # Imports custom functions for file and directory operations
from commands import COMMANDS, handle_command

class PyKernel: # Defines a class to represent the kernel
    def __init__(self): # Constructor to initialize the kernel
        self.running = True # Controls the shell/main loop
        self.cwd = os.getcwd() # Stores the current working directory (starts in the directory where the script is run)

    def run(self): # REPL loop (Read-Eval-Print Loop)
        while self.running: # Continuously runs until the user exits
            try:
                cmd = input(prompt(self.cwd))
                self.execute(cmd)
            except (KeyboardInterrupt, EOFError): # Handles Ctrl+C and EOF (Ctrl+D) gracefully
                print_warning("\nExiting...") # Prints a warning message when exiting
                break # Exits the loop
            except Exception as e: # Catches any other exceptions
                print_error(e) # Prints a generic error message
                break # Exits the loop
            
    def execute(self, cmd):
        handle_command(cmd, shell=self) # Handles the command execution
                 
            

if __name__ == "__main__": # Ensures the script runs only when executed directly
    PyKernel().run() # Create an instance of the PyKernel class and run it
