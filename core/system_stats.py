import os
import platform
import time
import shutil

class SystemStats:
    def __init__(self):
        self.boot_time = time.time() - self.get_uptime()
        
    
    def get_uptime(self):
        if platform.system() == "Linux":
            with open("/proc/uptime", "r") as f:
                return float(f.readline().split()[0])
        elif platform.system() == "Darwin":
            return float(os.popen("sysctl -n kern.boottime").read().split("=")[1].split(",")[0].strip())
        elif platform.system() == "Windows":
            return float(os.popen("wmic os get lastbootuptime").read().split()[1].strip())
        else:
            raise NotImplementedError("Uptime retrieval not implemented for this OS")
    
    def get_memory_stats(self):
        if platform.system() == "Linux":
            with open("/proc/meminfo", "r") as f:
                lines = f.readlines()
                mem_total = float(lines[0].split()[1]) / 1024
                mem_free = float(lines[1].split()[1]) / 1024
                return {
                    "total": mem_total,
                    "free": mem_free,
                    "used": mem_total - mem_free
                }
        elif platform.system() == "Darwin":
            total = float(os.popen("sysctl -n hw.memsize").read()) // (1024**2)
            vm_stats = os.popen("vm_stat").read()
            free_pages = sum(float(line.split(":")[1].strip().split()[0]) for line in vm_stats.split("\n") if "free" in line.lower())
            page_size = float(os.popen("sysctl -n hw.pagesize").read())
            free = (free_pages * page_size) // (1024**2)
            return {
                "total": total,
                "free": free,
                "used": total - free
            }
        elif platform.system() == "Windows":
            import psutil
            mem = psutil.virtual_memory()
            return {
                "total": mem.total / (1024 ** 2),
                "free": mem.free / (1024 ** 2),
                "used": mem.used / (1024 ** 2)
            }
        else:
            raise NotImplementedError("Memory stats retrieval not implemented for this OS")
    
    def get_cpu_usage(self):
        if platform.system() == "Linux":
            with open("/proc/loadavg", "r") as f:
                return float(f.read().split()[0])
        elif platform.system() == "Darwin":
            load = os.popen("sysctl -n vm.loadavg").read().strip().strip("{}").split()
            return float(load[0])
        elif platform.system() == "Windows":
            import psutil
            return psutil.cpu_percent(interval=1)
        else:
            raise NotImplementedError("CPU usage retrieval not implemented for this OS")