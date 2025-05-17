import sys          # For writing to stdout directly
import threading    # For running the spinner in a background thread
import time         # For delays between spinner frames
import itertools     # For cycling through spinner frames

class LoaderBar:
    """
    Displays a live spinner/loading bar in the terminal during a long-running task.
    This runs in a background thread and can be reused across commands like net trace, net range, etc.
    """
    
    def __init__(self, message="Working...", delay=0.1):
        """
        Initialize the loader bar.
        :param message: The status message to display next to the spinner.
        :param delay: The delay between spinner frames.
        """
        
        self.message = message  # Message to display
        self.delay = delay      # Delay between spinner frames
        self._running = False   # Interal flag to control the spinner loop
        self._thread = None     # Thread instance for running the spinner
        
    def _loader(self):
        """
        Internal method that runs in a separate thread to update the spinner.
        It cycles through characters like '|', '/', '-', and '\\' to create an animated effect.
        """
        spinner = itertools.cycle(['|', '/', '-', '\\'])
        while self._running:
            # Write the current frame with a carriage return to overwrite the previous line
            sys.stdout.write(f"\r{self.message} {next(spinner)}")
            sys.stdout.flush()
            time.sleep(self.delay) # Wait before showing the next frame
            
        # Clear the spinner line when done
        sys.stdout.write("\r" + " " * (len(self.message) + 2) + "\r")
        sys.stdout.flush()
        
    def start(self):
        """
        Start the loader bar in a separate thread.
        """
        self._running = True
        self._thread = threading.Thread(target=self._loader)
        self._thread.start()
    
    def stop(self):
        """
        Stop the loader bar and wait for the thread to finish.
        """
        self._running = False
        if self._thread:
            self._thread.join()