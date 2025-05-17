import subprocess
import platform
import socket
import re
from utils.io import print_heading, print_info, print_magenta

# Run a shell command and return its output, or an error string if it fails
def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
    
    
# Determine the operating system: 'darwin' = macOS, 'linux' = Linux, 'windows' = Windows
def get_os():
    return platform.system().lower()

# Get the local IP address by resolving the machine's hostname
def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror as e:
        return f"Error: {e}"
    
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
def ping_host(host="1.1.1.1", cout=4):
    os_type = get_os()
    
    cmd = f"ping -{'c' if os_type != 'windows' else 'n'} {cout} {host}"
    return run_cmd(cmd)

# Resolve a domain name to its IP using dig
def resolve_dns(domain="google.com"):
    return run_cmd(f"dig +short {domain}")

def test_connectivity():
    print_heading("=== Connectivity Report ===")
    print_info(f"Local IP      : {get_local_ip()}")
    print_info(f"Gateway IP    : {get_gateway_ip()}")
    print_info(f"Public IP     : {get_public_ip()}")
    
    print_heading("\n--- Ping Test (1.1.1.1) ---")
    print_magenta(ping_host())
    
    print_heading("\n--- DNS Resolution (google.com) ---")
    print_magenta(resolve_dns())