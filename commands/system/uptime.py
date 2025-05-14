from utils.io import print_info

def cmd_uptime(_args, shell):
    uptime = shell.system_stats.get_uptime()
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    print_info(f"Uptime: {hours}h {minutes}m {seconds}s")