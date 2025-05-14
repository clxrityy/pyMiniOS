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
from commands.help import cmd_help
from commands.pwd import cmd_pwd
from commands.cp import cmd_cp
from commands.mv import cmd_mv
from commands.process.kill import cmd_kill
from commands.process.run import cmd_run
from commands.process.ps import cmd_ps
from commands.system.uptime import cmd_uptime
from commands.system.cpu import cmd_cpu
from commands.system.mem import cmd_mem



from utils.errors import error
from utils.io import print_info

COMMANDS = {
    # GENERAL COMMANDS
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
    "pwd": {
        "func": cmd_pwd,
        "description": "Print the current working directory",
        "usage": "pwd",
        "example": "pwd",     
    },
    "cp": {
        "func": cmd_cp,
        "description": "Copy files and directories",
        "usage": "cp <source> <destination>",
        "example": "cp file.txt /home/user/new_file.txt",
    },
    "mv": {
        "func": cmd_mv,
        "description": "Move or rename files and directories",
        "usage": "mv <source> <destination>",
        "example": "mv file.txt /home/user/new_file.txt",  
    },
    "help": {
        "func": cmd_help,
        "description": "Display help information for commands",
        "usage": "help [command]",
        "example": "help",
    },
    # PROCESS COMMANDS
    "run": {
        "func": cmd_run,
        "description": "Run a process",
        "usage": "run <command>",
        "example": "run dummy_task",
    },
    "ps": {
        "func": cmd_ps,
        "description": "List running processes",
        "usage": "ps",
        "example": "ps",
    },
    "kill": {
        "func": cmd_kill,
        "description": "Terminate a process",
        "usage": "kill <pid>",
        "example": "kill 1234",
    },
    # SYSTEM COMMANDS
    "uptime": {
        "func": cmd_uptime,
        "description": "Display system uptime",
        "usage": "uptime",
        "example": "uptime",
    },
    "cpu": {
        "func": cmd_cpu,
        "description": "Display CPU usage",
        "usage": "cpu",
        "example": "cpu",
    },
    "mem": {
        "func": cmd_mem,
        "description": "Display memory usage",
        "usage": "mem",
        "example": "mem",
    },
    
}

def handle_command(input_line, shell, commands):
    args = input_line.strip().split()
    if not args:
        return
    
    cmd_name = args[0]
    cmd_args = args[1:]
    
    if cmd_name in COMMANDS:
        cmd_obj = COMMANDS[cmd_name]
        cmd_func = cmd_obj["func"]
        if cmd_name == "help":
            cmd_func(cmd_args, shell, commands)
        else:
            cmd_func(cmd_args, shell)
    else:
        error("Unknown command", cmd_name)
        print_info("Run 'help' to see the list of available commands.")
        