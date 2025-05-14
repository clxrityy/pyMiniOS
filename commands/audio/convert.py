import subprocess
from utils.io import print_info
from utils.errors import error

def cmd_audio_convert(args, _shell):
    cmd_name = "audio convert"
    
    if len(args) != 2:
        error(cmd_name, "Usage: audio convert <input_file> <output_file>")
        return
    
    input_file, output_file = args
    
    try:
        subprocess.run(
            ["ffmpeg", "-i", input_file, output_file],
            check=True
        )
        print_info(f"Converted {input_file} -> {output_file}")
    
    except FileNotFoundError:
        error(cmd_name, "ffmpeg is not installed. Please install it to use this command.")
        return
        
    except subprocess.CalledProcessError as e:
        error(cmd_name, f"Error converting audio file: {e}")
        return