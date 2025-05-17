from commands.file.cat import cmd_cat
from commands.file.cd import cmd_cd
from commands.general.echo import cmd_echo
from commands.general.exit import cmd_exit
from commands.file.ls import cmd_ls
from commands.general.clear import cmd_clear
from commands.file.mkdir import cmd_mkdir
from commands.file.touch import cmd_touch
from commands.file.rm import cmd_rm
from commands.file.rmdir import cmd_rmdir
from commands.general.help import cmd_help
from commands.file.pwd import cmd_pwd
from commands.file.cp import cmd_cp
from commands.file.mv import cmd_mv
from commands.process.kill import cmd_kill
from commands.process.run import cmd_run
from commands.process.ps import cmd_ps
from commands.system.uptime import cmd_uptime
from commands.system.cpu import cmd_cpu
from commands.system.mem import cmd_mem
from commands.system.df import cmd_df
from commands.system.top import cmd_top
from commands.audio.info import cmd_audio_info
from commands.audio.convert import cmd_audio_convert
from commands.network.test import cmd_test
from commands.network.speed import cmd_speed


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
    "df": {
        "func": cmd_df,
        "description": "Display disk usage",
        "usage": "df [directory]",
        "example": "df /home/user",
    },
    "top": {
        "func": cmd_top,
        "description": "Display system resource usage",
        "usage": "top",
        "example": "top",
    },
    
    # AUDIO COMMANDS
    "audio": {
        "subcommands": {
            "info": {
                "func": cmd_audio_info,
                "description": "Display metadata for an audio file",
                "usage": "audio info <audio>",
                "example": "audio info https://audio.com/example.wav"
            },
            "convert": {
                "func": cmd_audio_convert,
                "description": "Convert an audio file to a different format",
                "usage": "audio convert <input_file> <output_file>",
                "example": "audio convert input.wav output.mp3"
            }
        }
    },
    
    # NETWORK COMMANDS
    "net": {
        "subcommands": {
            "test": {
                "func": cmd_test,
                "description": "Test network connectivity",
                "usage": "net test",
                "example": "net test"
            },
            "speed": {
                "func": cmd_speed,
                "description": "Run a speed test",
                "usage": "net speed",
                "example": "net speed"
            },
        }
    }
}

def handle_command(input_line, shell, commands):
    args = input_line.strip().split()
    if not args:
        return
    
    cmd_name = args[0]
    subcommand = args[1] if len(args) > 1 else None
    cmd_args = args[2:] if len(args) > 2 else args[1:]
    
    
    if cmd_name in COMMANDS:
        cmd_obj = COMMANDS[cmd_name]
        
        if "subcommands" in cmd_obj:
            if subcommand in cmd_obj["subcommands"]:
                cmd_func = cmd_obj["subcommands"][subcommand]["func"]
            else:
                error("Unknown subcommand", subcommand)
                print_info(f"Run 'help {cmd_name}' to see the list of available subcommands.")
                return
        else:
            cmd_func = cmd_obj["func"]
        if cmd_name == "help":
            cmd_func(cmd_args, shell, commands)
        else:
            cmd_func(cmd_args, shell)
    else:
        error("Unknown command", cmd_name)
        print_info("Run 'help' to see the list of available commands.")
        