# pyMiniOS

A minimal Python-based pseudo-operating system with a command-line shell. Simulates core OS behaviors like file management, process handling, environment variables, and user-defined commands — all without external dependencies.

[![Static Badge](https://img.shields.io/badge/commands-show?style=for-the-badge&logo=gnometerminal&logoColor=%23111111&color=%234B8BBE&link=https%3A%2F%2Fgithub.com%2Fclxrityy%2FpyMiniOS%2Fblob%2Fmaster%2FCOMMANDS.md)](./COMMANDS.md)

---

## Usage
```bash
git clone https://github.com/clxrityy/pyMiniOS.git # Clone the repository
cd pyMiniOS # Navigate to the directory
pip install -r requirements.txt # Install dependencies
python3 main.py # Run the simulation
```

#### Running in a Virtual Environment
```bash
python3 -m venv venv # Create a virtual environment
source venv/bin/activate # Activate the virtual environment
python3 main.py # Run the simulation
deactivate # Deactivate the virtual environment
```

---

## Installation
> Installs the required dependencies and sets up the environment for running the interface globally.

```bash
chmod +x install.sh # Make the script executable
./install.sh # Run the installation script

pymini # Run the simulation
```

---

## Features
- Minimal shell
- Command interpreter loop
    - Basic command handling
- Runs in terminal or command line
- No external libraries required
- Process management *simulation*
    - Process creation and termination
    - Process listing
    - Process killing
- System information
    - Uptime
    - Memory usage
    - CPU usage
- Audio interaction commands
- Network/WiFi commands

## Planned Features
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
- [ ] System management
    - [ ] System calls
    - [x] View system information
    - [x] System monitoring
    - [ ] System logging
- [ ] Basic networking
    - [ ] Socket programming
    - [ ] Network protocols
    - [ ] Network security
- [ ] Web scraping
    - [ ] Basic web scraping
    - [ ] Data extraction and parsing
    - [ ] Data storage and retrieval