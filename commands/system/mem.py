from utils.io import print_info, print_grey, print_heading

def cmd_mem(_args, shell):
    stats = shell.system_stats.get_memory_stats()
    print_heading("Memory Stats")
    print_info(f"  Total: {stats['total']} MB")
    print_info(f"  Used:  {stats['used']} MB")
    print_info(f"  Free:  {stats['free']} MB")