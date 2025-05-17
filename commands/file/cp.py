import os
import shutil
from utils.io import print_info
from utils.errors import error

def cmd_cp(args, shell):
    if len(args) < 2:
        error("cp", "Not enough arguments provided")
        return

    src = os.path.join(shell.cwd, args[0]) if not os.path.isabs(args[0]) else args[0]
    dest = os.path.join(shell.cwd, args[1]) if not os.path.isabs(args[1]) else args[1]
    
    if not os.path.exists(src):
        error("cp", f"Source file '{src}' does not exist")
        return
    
    if os.path.exists(dest):
        error("cp", f"Destination '{dest}' already exists")
        return

    try:
        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy2(src, dest)
        print_info(f"Copied '{src}' to '{dest}'")
    except PermissionError:
        error("cp", f"Permission denied to copy '{src}' to '{dest}'")
    except Exception as e:
        error("cp", f"Error copying '{src}' to '{dest}': {e}")
    