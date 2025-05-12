from utils.io import print_heading, print_magenta, print_grey, print_info

def cmd_help(_args, _shell, commands):
    print_heading("Available commands:\n")
    for name, meta in sorted(commands.items()):
        print_magenta(f"{name}: {meta['description']}")
        print_info(f"    Usage: {meta['usage']}")
        print_info(f"    Example: {meta['example']}\n")
        print_grey("--------------------------------------------------")