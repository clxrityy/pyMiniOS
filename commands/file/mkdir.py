from utils.errors import error
import os
from utils.io import print_success

def cmd_mkdir(args, shell):
    if not args:
        error("mkdir", "No directory name provided")
        return
    for dir_name in args:
        try:
            os.mkdir(os.path.join(shell.cwd, dir_name))
        except FileExistsError:
            error("mkdir", f"Directory '{dir_name}' already exists")
        except PermissionError:
            error("mkdir", f"Permission denied to create directory '{dir_name}'")
        except OSError as e:
            error("mkdir", f"Error creating directory '{dir_name}': {e}")
        else:
            print_success(f"Directory '{dir_name}/' created successfully")