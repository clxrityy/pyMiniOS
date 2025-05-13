from utils.errors import error
from utils.io import print_info
import os

def cmd_mv(args, shell):
    if len(args) < 2:
        error("mv", "Missing source and/or destination arguments")
        return
    
    src = os.path.join(shell.cwd, args[0]) if not os.path.isabs(args[0]) else args[0]
    dest = os.path.join(shell.cwd, args[1]) if not os.path.isabs(args[1]) else args[1]
    
    if not os.path.exists(src):
        error("mv", f"Source '{src}' does not exist")
        return
    if os.path.exists(dest):
        error("mv", f"Destination '{dest}' already exists")
        return
    
    try:
        os.rename(src, dest)
        print_info(f"Moved '{src}' to '{dest}'")
    except PermissionError:
        error("mv", f"Permission denied to move '{src}' to '{dest}'")
    except FileNotFoundError:
        error("mv", f"File not found: '{src}'")
    except Exception as e:
        error("mv", f"Error moving '{src}' to '{dest}': {e}")
