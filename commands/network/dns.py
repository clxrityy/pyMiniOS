from core.net.dns import get_dns_servers
from utils.io import print_info, print_grey, print_error, print_warning

def cmd_dns(_args, _shell):
    try:
        dns_servers = get_dns_servers()
    
        for server in dns_servers:
            print_info(server)
        print_grey("=========")
        print_grey("DNS servers retrieved successfully.")
    except Exception as e:
        print_error(f"An error occurred while retrieving DNS servers: {e}")
        print_warning("Please ensure you have an active internet connection and try again.")