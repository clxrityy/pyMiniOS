import tempfile
import urllib.request
import os
from utils.errors import error

def download_temp_file(url):
    try:
        response = urllib.request.urlopen(url)
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        temp.write(response.read())
        temp.close()
        return temp.name
    except Exception as e:
        error("Download file error: ", str(e))
        return None