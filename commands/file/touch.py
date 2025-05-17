from utils.errors import error
from utils.io import print_success
import os

def cmd_touch(args, shell):
    if not args:
        error("touch", "No file name provided")
        return
    for file_name in args:
        path = os.path.join(shell.cwd, file_name)
        try:
            with open(path, "a"):
                os.utime(path, None)
        except FileExistsError:
            error("touch", f"File '{file_name}' already exists")
        except PermissionError:
            error("touch", f"Permission denied to create file '{file_name}'")
        except OSError as e:
            error("touch", f"Error creating file '{file_name}': {e}")
        else:
            print_success(f"File '{file_name}' created successfully")