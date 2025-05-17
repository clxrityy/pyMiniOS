from core.net.connectivity import ping_host

from utils.io import print_info, print_success, print_error, print_warning, print_grey

def cmd_ping(args, _shell):
    """
    Usage:
        net ping <host> [count]
    Example:
        net ping 1.1.1.1 4
    """
    host = '1.1.1.1'
    count = 4
    
    if not args or args[0] == 'ping':
        print_success(f"Pinging default host {host} with default count {str(count)}...")
        try:
            print_info(ping_host(host, count))
            print_warning("    Usage: net ping <host> [count]")
        except Exception as e:
            print_error(f"Error occured:\n{str(e)}")
        return
    
    host = args[0]
    
    # Try to parse the (optional) count
    if len(args) > 1:
        try:
            count = int(args[1])
        except ValueError:
            print_error(f"Invalid count '{args[1]}', defaulting to 4")
    
    print_success(f"Pinging host '{host}' with count: {count}...")
    
    try:
        output = ping_host(host, count)
        print_info(output)
    except Exception as e:
        print_error(f"Error pinging {host} with {count} count...\n{e}")
        print_warning("Ensure you have an internet connection and try again.")
    