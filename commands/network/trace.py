from core.net.utils import trace_route_live
from utils.io import print_info, print_success, print_error, print_warning, print_grey

def cmd_trace(args, _shell):
    """
    Usage:
        net trace <host>
    Example:
        net trace example.com
    """
    host = 'google.com'
    if not args or args[0] == 'trace':
        print_success(f"Tracing default host {host}...")
        try:
            print_info(trace_route_live(host))
            print_warning("    Usage: net trace <host>")
        except Exception as e:
            print_error(f"Error occurred:\n{str(e)}")
        return
    
    host = args[0]
    
    print_success(f"Tracing host '{host}'...")
    
    try:
        print_info(trace_route_live(host))
    except Exception as e:
        print_error(f"Error occurred:\n{str(e)}")