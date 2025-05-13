from utils.io import print_heading, print_magenta, print_grey, print_info
from utils.errors import error

def cmd_help(args, _shell, commands):
    if not args:
        print_heading("Available commands:\n")
        for name, meta in sorted(commands.items()):
            print_magenta(f"{name}: {meta['description']}")
            print_info(f"    Usage: {meta['usage']}")
            print_info(f"    Example: {meta['example']}\n")
            print_grey("--------------------------------------------------")
    else:
        cmd_name = args[0]
        if cmd_name in commands:
            meta = commands[cmd_name]
            print_heading(f"Command: {cmd_name}")
            print_info(f"Description: {meta['description']}")
            print_info(f"Usage: {meta['usage']}")
            print_info(f"Example: {meta['example']}")
        else:
            erorr(f"Command '{cmd_name}' not found.")