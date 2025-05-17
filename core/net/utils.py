import subprocess
import socket
import platform
from utils.loader import LoaderBar

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
    """Safely get the local IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("10.255.255.255", 1)) # Use a dummy address to force the socket to connect
        ip = s.getsockname()[0]
        s.close()
        return ip
    except socket.error as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"
    

def trace_route(host):
    """
    DEPRECATED: Use trace_route_live instead.
    Trace the route to a host.
    """
    os = get_os()
    if os == 'darwin':
        cmd = f"traceroute -m 15 -w 2 {host}"
    elif os == 'linux':
        cmd = f"traceroute -m 15 -w 2 {host}"
    elif os == 'windows':
        cmd = f"tracert -h 15 {host}"
    else:
        return "Unsupported OS"
    
    return run_cmd(cmd)

def trace_route_live(host):
    """
    Trace the route to a host and display the output live.
    """
    loader = LoaderBar(f"Tracing route to {host}...", delay=0.1)
    loader.start()
    
    try:
        output = subprocess.check_output(
            ["traceroute", "-m", "15", "-w", "2", host],
            stderr=subprocess.STDOUT,
            text=True
        )
    except subprocess.CalledProcessError as e:
        output = f"Error running traceroute:\n{e.output}"
    finally:
        loader.stop()
    
    return output

def list_open_ports():
    """
    Show all open/listening ports with process info
    """
    os_type = get_os()
    # macOS/Linux: use lsof or ss; prefer netstat fallback
    if os_type in ["linux", "darwin"]:
        return run_cmd("lsof -i -P -n | grep LISTEN")
    elif os_type == "windows":
        return run_cmd("netstat -ano | findstr LISTENING")
    else:
        return "Unsupported OS"