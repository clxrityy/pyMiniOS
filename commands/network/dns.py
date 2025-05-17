from core.net.dns import get_dns_servers
from utils.io import print_info, print_success, print_error, print_warning, print_faint

def cmd_dns(_args, _shell):
    try:
        dns_servers = get_dns_servers()
    
        for server in dns_servers:
            print_info(server)
        print_faint("=========")
        print_success("DNS servers retrieved successfully.")
    except Exception as e:
        print_error(f"An error occurred while retrieving DNS servers: {e}")
        print_warning("Please ensure you have an active internet connection and try again.")