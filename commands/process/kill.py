from utils.io import print_info, print_success
from utils.errors import error

def cmd_kill(args, shell):
    if not args:
        error("kill", "no process specified")
        print_info("Usage: kill <pid>")
        return
    
    success = shell.process_manager.kill(args[0])
    if success:
        print_success(f"Terminated process: {args[0]}")
    else:
        error("kill", f"failed to terminate process: {args[0]}")