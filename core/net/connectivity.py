import platform
import re
from utils.io import print_heading, print_info, print_magenta
from core.net.utils import run_cmd, get_os, get_local_ip
    
# Get the default gateway IP address (i.e. the router's local address)
def get_gateway_ip():
    os_type = get_os()
    
    if os_type == 'darwin':
        output = run_cmd("netstat -nr | grep default")
        match = re.search(r'default\s+(\d+\.\d+\.\d+\.\d+)', output)
    else: # Linux: use ip route to find the gateway after 'default via'
        output = run_cmd("ip route | grep default")
        match = re.search(r'default via (\d+\.\d+\.\d+\.\d+)', output)
        
    # Return the matched ip address or an error message
    return match.group(1) if match else "Error: No gateway found"

# Get the public-facing IP address using an external service (ifconfig.me)
def get_public_ip():
    try:
        return run_cmd("curl -s ifconfig.me")
    except Exception as e:
        return f"Error: {e}"
    
# Run a ping test to a specified host and return the result
def ping_host(host, count=4):
    os_type = get_os()
    
    cmd = f"ping -{'c' if os_type != 'windows' else 'n'} {count} {host}"
    return run_cmd(cmd)

# Resolve a domain name to its IP using dig
def resolve_dns(domain):
    return run_cmd(f"dig +short {domain}")

def test_connectivity():
    print_heading("=== Connectivity Report ===")
    print_info(f"Local IP      : {get_local_ip()}")
    print_info(f"Gateway IP    : {get_gateway_ip()}")
    print_info(f"Public IP     : {get_public_ip()}")