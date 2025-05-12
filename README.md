# pyMiniOS

A toy operating system simulation written in Python. `pyMiniOS` is **not** a real kernel or OS — instead, it's a learning playground that mimics a shell environment with basic command handling, a virtual filesystem, and simulated OS behaviors.

## Features
- Minimal shell (`cd`, `ls`, `cat`, `echo`, `exit`)
- Command interpreter loop
- Runs in terminal or command line
- No external libraries required

## Planned Features
- File system simulation
    - File permissions & access control
- User accounts & login simulation
- Shell history, command chaining, and piping
- Process/task management
- Basic networking simulation

---

## Usage
```bash
git clone https://github.com/clxrityy/pyMiniOS.git # Clone the repository
cd pyMiniOS # Navigate to the directory
python3 main.py # Run the simulation

# With Python Virtual Environment
python3 -m venv venv # Create a virtual environment
source venv/bin/activate # Activate the virtual environment
python3 main.py # Run the simulation
# Deactivate the virtual environment
deactivate
 ```