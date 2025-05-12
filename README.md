# pyMiniOS

A toy operating system simulation written in Python. `pyMiniOS` is **not** a real kernel or OS — instead, it's a learning playground that mimics a shell environment with basic command handling, a virtual filesystem, and simulated OS behaviors.

## Features
- Minimal shell
- Command interpreter loop
- Runs in terminal or command line
- No external libraries required

## Planned Features
- File system simulation
    - File permissions & access control
- Shell history, command chaining, and piping
- Process/task management
- Basic networking simulation

---

## Usage
```bash
git clone https://github.com/clxrityy/pyMiniOS.git # Clone the repository
cd pyMiniOS # Navigate to the directory
python3 main.py # Run the simulation
```

#### Running in a Virtual Environment
```bash
python3 -m venv venv # Create a virtual environment
source venv/bin/activate # Activate the virtual environment
python3 main.py # Run the simulation
deactivate # Deactivate the virtual environment
```

----

## Commands
| Command | Description | Arguments |
| :------- | ----------- | :---------: |
| `cd` | Change directory | `<directory>` |
| `ls` | List files in the current directory | `<directory>` |
| `cat` | Display file contents | `<file>` |
| `echo` | Print text to the console | `<text>` |
| `exit` | Exit the shell | `N/A` |
| `clear` | Clear the console | `N/A` |