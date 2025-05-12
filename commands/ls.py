from utils.fs import is_dir, list_dir
from utils.io import print_info
import os

def cmd_ls(args, shell):

    path = shell.cwd if not args else args[0]
    files = list_dir(path)

    for f in files:
        full_path = os.path.join(path, f)
        if is_dir(full_path):
            print_info(f + "/")
        else:
            print_info(f)