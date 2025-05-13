# pyMiniOS

A toy operating system simulation written in Python. `pyMiniOS` is **not** a real kernel or OS — instead, it's a learning playground that mimics a shell environment with basic command handling, a virtual filesystem, and simulated OS behaviors.

[![Static Badge](https://img.shields.io/badge/commands-show?style=for-the-badge&logo=gnometerminal&logoColor=%23111111&color=%234B8BBE&link=https%3A%2F%2Fgithub.com%2Fclxrityy%2FpyMiniOS%2Fblob%2Fmaster%2FCOMMANDS.md)](./COMMANDS.md)

## Features
- Minimal shell
- Command interpreter loop
    - Basic command handling
- Runs in terminal or command line
- No external libraries required
- Process management simulation
    - Process creation and termination
    - Process listing
    - Process killing

## Planned Features
- File system simulation
    - File permissions & access control
- Shell history, command chaining, and piping
- [x] Process/task management
    - [x] Process creation and termination
    - [ ] Process scheduling
    - [ ] Inter-process communication
    - [ ] Process synchronization
- [ ] Memory management
    - [ ] Virtual memory
    - [ ] Paging and segmentation
    - [ ] Memory allocation and deallocation
    - [ ] Memory protection
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