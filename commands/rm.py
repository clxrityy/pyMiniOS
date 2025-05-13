from utils.errors import error
from utils.io import print_success
import os

def cmd_rm(args, shell):
    if not args:
        error("rm", "missing argument")
        return
    for filename in args:
        path = os.path.join(shell.cwd, filename)
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                error("rm", f"cannot remove '{filename}': Is a directory.\nUse 'rmdir' to remove directories.")
            else:
                error("rm", f"cannot remove '{filename}': No such file or directory.")
        except PermissionError:
            error("rm", f"cannot remove '{filename}': Permission denied.")
        except OSError as e:
            error("rm", f"cannot remove '{filename}': {e.strerror}.")
        except Exception as e:
            error("rm", f"cannot remove '{filename}': {str(e)}.")