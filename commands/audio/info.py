import wave
import contextlib
import os
from utils.io import print_info, print_heading
from utils.errors import error
from utils.is_url import is_url
from utils.download_temp_file import download_temp_file

def cmd_audio_info(args, _shell):
    cmd_name = "audio info"
    
    if not args:
        error(cmd_name, "Usage: audio info <audio_file>")
        return
    
    file_path = args[0]
    is_temp = False
    
    if is_url(file_path):
        temp_file = download_temp_file(file_path)
        if not temp_file:
            error(cmd_name, "Failed to download the audio file.")
            return
        file_path = temp_file
        is_temp = True
        
    elif not os.path.isfile(file_path):
        error(cmd_name, f"File '{file_path}' does not exist.")
        return
    
    try:
        with contextlib.closing(wave.open(file_path, "r")) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            print_heading(f"Audio File Info: {file_path}")
            print_info(f"Channels: {f.getnchannels()}")
            print_info(f"Sample rate: {rate} Hz")
            print_info(f"Duration: {duration:.2f} seconds")
            print_info(f"Sample width: {f.getsampwidth()} bytes")
    except wave.Error as e:
        error(cmd_name, f"Error reading audio file: {str(e)}")
    finally:
        if is_temp:
            os.remove(file_path)