import time
import os
from utils.io import print_heading, print_info, print_grey
from core.system_stats import SystemStats

def cmd_top(_args, shell):
    stats = SystemStats()
    
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_heading("=== pyMiniOS Monitor ===")
            print_grey("Press Ctrl+C to exit")
            print_info(f"Uptime: {int(stats.get_uptime())}s")
            print_info(f"CPU Load: {stats.get_cpu_usage()}%")
            mem = stats.get_memory_stats()
            print_info(f"Memory: {mem['used']} / {mem['total']} MB used")
            
            procs = shell.process_manager.list_processes()
            
            if (procs is None) or (len(procs) == 0):
                print_grey("No processes running.")
                time.sleep(1)
                continue
            else:
                print_grey("==========================")
                print_info("PID\tName\t\tCPU\tMemory")
                for proc in procs:
                    print_info(f"{proc['pid']}\t{proc['name']}\t{proc['cpu']}%\t{proc['memory']} MB")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print_grey("\nExiting pyMiniOS Monitor...")