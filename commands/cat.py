from utils.errors import error
from utils.fs import read_file
from utils.io import print_info
from misc.constants import NO_ARGUMENTS_PROVIDED

def cmd_cat(args, _shell):
    if not args:
        print(error("cat", NO_ARGUMENTS_PROVIDED))
        return
    for file in args:
        result = read_file(file)
        print_info(result)    