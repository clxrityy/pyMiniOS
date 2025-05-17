import os
from utils.io import print_info, print_error, print_success
from misc.constants import NO_ARGUMENTS_PROVIDED
from utils.errors import error


def cmd_cd(args, shell):
    if not args:
        print(error("cd", NO_ARGUMENTS_PROVIDED))
        return
    try:
        new_path = os.path.abspath(os.path.join(shell.cwd, args[0]))
        os.chdir(new_path)
        shell.cwd = new_path
        print_success("Changed directory to: ")
        print_info(new_path)
    except FileNotFoundError:
        print_error(f"Directory not found: {args[0]}")
    except PermissionError:
        print_error(f"Permission denied: {args[0]}")
    except Exception as e:
        print_error(f"Error changing directory to {args[0]}: {e}")