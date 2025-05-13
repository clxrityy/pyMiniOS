from utils.errors import error
from utils.io import print_info

def cmd_run(args, shell):
    if not args:
        error("run", "no process specified")
        return
    
    proc = shell.process_manager.spawn(args[0])
    print_info(f"Process '{proc.name}' started with PID: {proc.pid}")