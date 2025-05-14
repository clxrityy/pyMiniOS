# Command reference

- [General commands](#general-commands)
- [Process management commands](#process-management-commands)
- [System commands](#system-commands)

## General commands

| Command | Description | Arguments | Example | Category |
| ------- | ----------- | :---------: | :------- | :-------: |
| **`help`** | **Display help information for commands.** | **`<command>`** | **`help ls`** | **General** |
| `ls` | List files and directories in the current directory. | `<directory>` | `ls utils/` | General |
| `cd` | Change the current directory. | `<directory>` | `cd utils/` | General |
| `cat` | Display the contents of a file. | `<file>` | `cat README.md` | General |
| `echo` | Print text to the terminal. | `<text>` | `echo Hello, World!` | General |
| `exit` | Exit the shell. | | `exit` | General |
| `clear` | Clear the terminal screen. | | `clear` | General |
| `mkdir` | Create a new directory. | `<directory>` | `mkdir new_folder` | General |
| `touch` | Create a new file or update the timestamp of an existing file. | `<file>` | `touch new_file.txt` | General |
| `rm` | Remove a file. | `<file>` | `rm old_file.txt` | General |
| `rmdir` | Remove an empty directory. | `<directory>` | `rmdir old_folder` | General |
| `pwd` | Print the current working directory. | | `pwd` | General |
| `cp` | Copy files or directories. | `<source> <destination>` | `cp file.txt backup/` | General |
| `mv` | Move or rename files or directories. | `<source> <destination>` | `mv old_file.txt new_file.txt` | General |


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