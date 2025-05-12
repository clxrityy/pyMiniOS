class Colors:
    """
    A class to define color codes for terminal output.
    """

    # ANSI escape sequences for colors
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def color_text(text, color):
    """
    Wraps the text with the specified color.
    """
    return f"{color}{text}{Colors.ENDC}"  # Wraps the text with the specified color and resets the color at the end
