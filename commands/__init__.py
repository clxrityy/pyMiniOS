from commands.cat import cmd_cat
from commands.cd import cmd_cd
from commands.echo import cmd_echo
from commands.exit import cmd_exit
from commands.ls import cmd_ls
from commands.clear import cmd_clear
from commands.mkdir import cmd_mkdir
from commands.touch import cmd_touch
from commands.rm import cmd_rm
from commands.rmdir import cmd_rmdir

from utils.errors import error
from utils.io import print_info

COMMANDS = {
    "cd": {
        "func": cmd_cd,
        "description": "Change the current directory",
        "usage": "cd <directory>",
        "example": "cd /home/user",
    },
    "ls": {
        "func": cmd_ls,
        "description": "List directory contents",
        "usage": "ls [directory]",
        "example": "ls /home/user",
    },
    "cat": {
        "func": cmd_cat,
        "description": "Concatenate and display file content",
        "usage": "cat <file>",
        "example": "cat file.txt",  
    },
    "echo": {
        "func": cmd_echo,
        "description": "Display a line of text",
        "usage": "echo <text>",
        "example": "echo Hello, World!",
    },
    "exit": {
        "func": cmd_exit,
        "description": "Exit the shell",
        "usage": "exit",
        "example": "exit",
    },
    "clear": {
        "func": cmd_clear,
        "description": "Clear the terminal screen",
        "usage": "clear",
        "example": "clear",
    },
    "mkdir": {
        "func": cmd_mkdir,
        "description": "Create a new directory",
        "usage": "mkdir <directory>",
        "example": "mkdir new_folder",
    },
    "touch": {
        "func": cmd_touch,
        "description": "Create an empty file or update the timestamp of an existing file",
        "usage": "touch <file>",
        "example": "touch new_file.txt",
    },
    "rm": {
        "func": cmd_rm,
        "description": "Remove files",
        "usage": "rm <file>",
        "example": "rm old_file.txt",
    },
    "rmdir": {
        "func": cmd_rmdir,
        "description": "Remove a directory",
        "usage": "rmdir <directory>",
        "example": "rmdir old_folder",
    },
}

def handle_command(input_line, shell):
    args = input_line.strip().split()
    if not args:
        return
    
    cmd_name = args[0]
    cmd_args = args[1:]
    
    if cmd_name in COMMANDS:
        cmd_obj = COMMANDS[cmd_name]
        cmd_func = cmd_obj["func"]
        cmd_func(cmd_args, shell)
    else:
        error("Unknown command", cmd_name)
        print_info("Run 'help' to see the list of available commands.")