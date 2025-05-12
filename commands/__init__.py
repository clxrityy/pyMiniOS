from commands.cat import cmd_cat
from commands.cd import cmd_cd
from commands.echo import cmd_echo
from commands.exit import cmd_exit
from commands.ls import cmd_ls
from commands.clear import cmd_clear

COMMANDS = {
    "cd": cmd_cd,
    "ls": cmd_ls,
    "cat": cmd_cat,
    "echo": cmd_echo,
    "exit": cmd_exit,
    "clear": cmd_clear,
}