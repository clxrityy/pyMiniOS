from utils.errors import error
from utils.io import print_success
import os

def cmd_rmdir(args, shell):
    if not args:
        error("rmdir", "missing argument")
        return
    for dirname in args:
        path = os.path.join(shell.cwd, dirname)
        try:
            os.rmdir(path)
        except FileNotFoundError:
            error("rmdir", f"cannot remove '{dirname}/': No such file or directory.")
        except PermissionError:
            error("rmdir", f"cannot remove '{dirname}/': Permission denied.")
        except OSError as e:
            error("rmdir", f"cannot remove '{dirname}/': {e.strerror}.")
        except Exception as e:
            error("rmdir", f"cannot remove '{dirname}/': {str(e)}.")
        else:
            print_success(f"Removed directory '{dirname}/'")