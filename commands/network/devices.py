from utils.io import print_error, print_heading, print_info, print_faint, print_magenta, print_success, print_warning
from core.net.utils import list_lan_devices

def cmd_devices(_args, _shell):
    """
    Usage:
        net devices
    Example:
        net devices
    """
    print_heading("Network Devices")
    print_faint("===============")

    try:
        # Assuming get_network_devices() is a function that retrieves network devices
        devices = list_lan_devices().split("\n")
        
        if not devices:
            print_warning("No network devices found.")
            return
        
        for device in devices:
            print_info(f"{device}")
            print_faint("-" * len(device))

        print_success("Network devices retrieved successfully.")
    except Exception as e:
        print_error(f"An error occurred while retrieving network devices: {e}")
        print_warning("Please ensure you have an active internet connection and try again.")