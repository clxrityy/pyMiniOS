# Command reference

- [General commands](#general-commands)
- [File management commands](#file-management-commands)
- [Process management commands](#process-management-commands)
- [System commands](#system-commands)
- [Audio commands](#audio-commands)
- [Network commands](#network-commands)

## General commands

| Command | Description | Arguments | Example | Category |
| ------- | ----------- | :---------: | :------- | :-------: |
| **`help`** | **Display help information for commands.** | **`<command>`** | **`help ls`** | **General** |
| `echo` | Print text to the terminal. | `<text>` | `echo Hello, World!` | General |
| `exit` | Exit the shell. | | `exit` | General |
| `clear` | Clear the terminal screen. | | `clear` | General |


## File management commands
| Command | Description | Arguments | Example | Category |
| ------- | ----------- | :---------: | :------- | :-------: |
| `pwd` | Print the current working directory. | | `pwd` | File Management |
| `ls` | List files and directories in the current directory. | `<directory>` | `ls utils/`  | File Management |
| `cat` | Display the contents of a file. | `<file>` | `cat README.md` | File Management |
| `touch` | Create a new file or update the timestamp of an existing file. | `<file>` | `touch new_file.txt` | File Management |
| `rm` | Remove a file. | `<file>` | `rm old_file.txt` | File Management |
| `rmdir` | Remove an empty directory. | `<directory>` | `rmdir old_folder` | File Management |
| `cp` | Copy files or directories. | `<source> <destination>` | `cp file.txt backup/` | File Management |
| `mv` | Move or rename files or directories. | `<source> <destination>` | `mv old_file.txt new_file.txt` | File Management |
| `mkdir` | Create a new directory. | `<directory>` | `mkdir new_folder` | File Management |


## Process management commands

| Command | Description | Arguments | Example | Category |
| ------- | ----------- | :---------: | :------- | :-------: |
| `run` | Start a new process. | `<process_name>` | `run dummy_task` | Process Management |
| `ps` | List all running processes. | | `ps` | Process Management |
| `kill` | Terminate a process. | `<pid>` | `kill 1234` | Process Management |

## System commands

| Command | Description | Arguments | Example | Category |
| ------- | ----------- | :---------: | :------- | :-------: |
| `uptime` | Display system uptime. | | `uptime` | System Information |
| `mem` | Display memory usage. | | `mem` | System Information |
| `cpu` | Display CPU usage. | | `cpu` | System Information |
| `df` | Display disk space usage. | | `df` | System Information |
| `top` | Display system processes and resource usage (realtime). | | `top` | System Information |

## Audio commands

| Command | Description | Arguments | Example | Category |
| ------- | ----------- | :---------: | :------- | :-------: |
| `audio info` | Display audio information. | <audio_file> | `audio info https://github.com/rafaelreis-hotmart/Audio-Sample-files/raw/master/sample.wav` | Audio |
| `audio convert` | Convert audio files to different formats. | `<input_file> <output_file>` | `audio convert input.wav output.mp3` | Audio |

## Network commands
| Command | Description | Arguments | Example | Category |
| ------- | ----------- | :---------: | :------- | :-------: |
| `net test` | Test your network diagnostics. | | `net test` | Network |
| `net speed` | Test your internet speed. | | `net speed` | Network |
| `net dns` | Display DNS information. | | `net dns` | Network |
