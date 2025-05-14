import shutil
from utils.io import print_info, print_heading

def cmd_df(args, shell):
    path = args[0] if args else shell.cwd
    usage = shutil.disk_usage(path)
    
    total = usage.total // (1024**2)
    used = (usage.total - usage.free) // (1024**2)
    free = usage.free // (1024**2)
    
    print_heading(f"Disk usage for: {path}")
    print_info(f"  Total: {total} MB")
    print_info(f"  Used:  {used} MB")
    print_info(f"  Free:  {free} MB")