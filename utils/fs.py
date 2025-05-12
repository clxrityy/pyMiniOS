import os
from utils.io import print_error, print_warning, print_success # Imports custom functions for printing messages

def is_dir(path):
    """
    Checks if the given path is a directory.
    """
    return os.path.isdir(path) # Checks if the path is a directory

def list_dir(path):
    """
    Lists the contents of the given directory.
    """
    try:
        return print_success(os.listdir(path)) # Lists the contents of the directory
    except FileNotFoundError:
        return print_error(f"Directory not found: {path}") # Prints an error message if the directory is not found
    except PermissionError:
        return print_error(f"Permission denied: {path}") # Prints an error message if permission is denied
    except Exception as e:
        return print_error(f"Error listing directory {path}: {e}") # Prints a generic error message for any other exceptions
    
def read_file(path):
    """
    Reads the contents of a file and prints it.
    """
    try:
        with open(path, "r") as f:
            return print_success(f.read()) # Reads and prints the file contents
    except FileNotFoundError:
        return print_error(f"File not found: {path}") # Prints an error message if the file is not found
    except PermissionError:
        return print_error(f"Permission denied: {path}") # Prints an error message if permission is denied
    except Exception as e:
        return print_error(f"Error reading file {path}: {e}") # Prints a generic error message for any other exceptions