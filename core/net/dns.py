from core.net.utils import get_os, run_cmd
import re

def get_dns_servers():
    os_type = get_os()
    
    if os_type in ["linux", "darwin"]:
        # macOS uses scutil, Linux uses resolv.conf
        output = run_cmd('scutil --dns') if os_type == 'darwin' else run_cmd("cat /etc/resolv.conf")
        # Find all IP-like DNS entries
        servers = re.findall(r'(?:(?:nameserver|Server\[\d+\])\s*:? )?(\d{1,3}(?:\.\d{1,3}){3})', output)
        return list(set(servers)) if servers else ["No DNS servers found"]
    elif os_type == "windows":
        # Use netsh to get DNS servers on Windows
        output = run_cmd("netsh interface ip show config")
        servers = re.findall(r'DNS Servers\s+:\s+(\d{1,3}(?:\.\d{1,3}){3})', output)
        return list(set(servers)) if servers else ["No DNS servers found"]
    else:
        return ["Unsupported OS"]