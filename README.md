# pyMiniOS

A minimalistic operating system simulation written in Python. It provides a basic command-line interface for simulating process management, system information retrieval, networking, and audio interaction. The project is designed to be lightweight and easy to use, making it suitable for educational purposes and as a starting point for more complex operating system simulations.

###### [![View all commands](https://img.shields.io/badge/commands-show?style=for-the-badge&logo=gnometerminal&logoColor=%23111111&color=%234B8BBE&link=https%3A%2F%2Fgithub.com%2Fclxrityy%2FpyMiniOS%2Fblob%2Fmaster%2FCOMMANDS.md)](./COMMANDS.md)

[![Example](https://i.gyazo.com/90bb9cc6e7e885a60527757948932349.gif)](https://gyazo.com/90bb9cc6e7e885a60527757948932349)

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
    - Convert audio file to a different format
    - Audio file metadata extraction
- Network/WiFi commands
    - Ports, trace, ping, DNS, etc.
- File system commands
    - File operations (create, read, write, delete)
    - Directory operations (create, list, delete)

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
- [x] Basic networking
    - [ ] Socket programming
    - [ ] Network protocols
    - [ ] Network security
    - [ ] Network performance monitoring
- [ ] Web scraping
    - [ ] Basic web scraping
    - [ ] Data extraction and parsing
    - [ ] Data storage and retrieval
- [x] File system management
    - [x] File operations (create, read, write, delete)
    - [x] Directory operations (create, list, delete)
    - [ ] File permissions and ownership
    - [x] File system navigation
    - [ ] File system monitoring