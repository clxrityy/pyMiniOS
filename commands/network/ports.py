from utils.io import print_info, print_success, print_error, print_warning, print_grey
from core.net.utils import list_open_ports

def cmd_ports(_args, _shell):
    try:
        print_success("Listing open ports...")
        print_info(list_open_ports())
    except Exception as e:
        print_error(f"Error occurred:\n{str(e)}")
        print_warning("Ensure you have the necessary permissions to view open ports and/or a valid network connection.")
        print_grey("If you are using a virtual machine, ensure that the network settings are configured correctly.")
        print_grey("If you are using a VPN/Proxy, ensure that it is connected and configured correctly.")
        print_grey("If you are using a firewall, ensure that it is not blocking the connection.")