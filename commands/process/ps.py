from utils.io import print_info, print_heading, print_grey

def cmd_ps(_args, shell):
    procs = shell.process_manager.list_processes()
    
    if not procs:
        print_info("No processes running.")
        return
    
    print_heading("PID       NAME            STATUS     UPTIME(s)")
    print_grey("===============================================")
    for p in procs:
        print(f"{p.pid:<9} {p.name:<15} {p.status:<10} {p.uptime():<10}")