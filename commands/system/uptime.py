from utils.io import print_info

def cmd_uptime(_args, shell):
    print_info(f"Uptime: {shell.process_manager.uptime()} seconds")