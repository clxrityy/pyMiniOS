import subprocess
import socket
import platform

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