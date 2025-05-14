from utils.io import print_info

def cmd_cpu(_args, shell):
    usage = shell.system_stats.get_cpu_usage()
    print_info(f"CPU Usage: {usage}%")