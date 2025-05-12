import os
import platform


def cmd_clear(_args, _shell):
    # Check if the user is on Windows
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")