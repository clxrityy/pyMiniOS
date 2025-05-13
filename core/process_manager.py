import time
import uuid

class Process:
    def __init__(self, name, pid=None):
        self.pid = pid or str(uuid.uuid4())[:8]
        self.name = name
        self.start_time = time.time()
        self.status = "running"
        
    def uptime(self):
        return round(time.time() - self.start_time, 2)
    

class ProcessManager:
    def __init__(self):
        self.processes = []
        
    def spawn(self, name):
        proc = Process(name)
        self.processes.append(proc)
        return proc
    
    def list_processes(self):
        return self.processes
    
    def kill(self, pid):
        for proc in self.processes:
            if proc.pid == pid:
                proc.status = "terminated"
                return True
        return False
    
    def uptime(self):
        return round(time.time() - self._start_time, 2)
    
    def reset(self):
        self._start_time = time.time()