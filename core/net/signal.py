import platform
import subprocess
import re
from core.net.utils import run_cmd, get_os
from utils.io import print_heading, print_info, print_magenta

# Get Wi-Fi signal strength, noise, and channel information
def get_signal_info():
    os_type = get_os()
    if os_type == 'darwin':
        return _get_signal_info_darwin()
    elif os_type == 'linux':
        return _get_signal_info_linux()
    elif os_type == 'windows':
        return _get_signal_info_windows()
    else:
        return "Unsupported OS"

def _get_signal_info_darwin():
    # Use Apple's private `airport` CLI to get detailed wifi metrics
    output = run_cmd('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I')
    # Extract signal details using regex
    rssi = re.search(r'agrCtlRSSI:\s*(-\d+)', output)
    noise = re.search(r'agrCtlNoise:\s*(-\d+)', output)
    snr = int(rssi.group(1)) - int(noise.group(1)) if rssi and noise else None
    channel = re.search(r'channel:\s*(\d+)', output)
    return {
        "RSSI (Signal Strength)": rssi.group(1) if rssi else "N/A",
        "Noise": noise.group(1) if noise else "N/A",
        "SNR (Signal-to-Noise Ratio)": snr,
        "Channel": channel.group(1) if channel else "N/A"
    }

def _get_signal_info_linux():
    # Use `iwconfig` to get signal strength and link quality
    output = run_cmd('iwconfig 2>/dev/null | grep -i --color signal')
    signal_level = re.search(r'Signal level=(-?\d+)', output)
    quality = re.search(r'Link Quality=(\d+/\d+)', output)
    return {
        "Signal Level": signal_level.group(1) if signal_level else "N/A",
        "Link Quality": quality.group(1) if quality else "N/A"
    }

def _get_signal_info_windows():
    # Use `netsh` to get Wi-Fi signal information
    output = run_cmd('netsh wlan show interfaces')
    signal_strength = re.search(r'Signal\s+:\s+(\d+)%', output)
    channel = re.search(r'Channel\s+:\s+(\d+)', output)
    return {
        "Signal Strength": signal_strength.group(1) if signal_strength else "N/A",
        "Channel": channel.group(1) if channel else "N/A"
    }
    

# Perform a basic internet speed test using speedtest-cli
def run_speed_test():
    try:
        import speedtest
        
        st = speedtest.Speedtest()
        st.get_best_server()
        
        download = st.download() / 1_000_000  # Convert from bits to Mbps
        upload = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        
        return {
            "Download Speed (Mbps)": round(download, 2),
            "Upload Speed (Mbps)": round(upload, 2),
            "Ping (ms)": round(ping, 2)
        }
        
    except ImportError:
        return "speedtest-cli is not installed. Please install it using 'pip install speedtest-cli'."

# Show both signal and speed stats in out output
def net_status():
    print_heading("=== WiFi Signal Information ===")
    signal = get_signal_info()
    
    for key, value in signal.items():
        print_info(f"{key:30}: {value}")
        
    print_heading("\n=== Internet Speed Test ===")
    print_info(run_speed_test())