from utils.io import print_magenta


def cmd_pwd(_args, shell):
    print_magenta(shell.cwd)