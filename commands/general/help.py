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
            print_heading(f"Command: {cmd_name}\n")
            meta = commands[cmd_name]
            if 'subcommands' in meta:
                subcommands = meta['subcommands']
                print_magenta(f"Subcommands for '{cmd_name}':")
                for sub_name, sub_meta in sorted(subcommands.items()):
                    print_info(f"    {sub_name}: {sub_meta['description']}")
                    print_info(f"        Usage: {sub_meta['usage']}")
                    print_info(f"        Example: {sub_meta['example']}\n")
                    print_grey("--------------------------------------------------")
            else:
                print_magenta(f"Description: {meta['description']}")
                print_info(f"    Usage: {meta['usage']}")
                print_info(f"    Example: {meta['example']}\n")
                print_grey("--------------------------------------------------")
        