class Colors:
    """
    A class to define color codes for terminal output.
    """

    # ANSI escape sequences for colors
    HEADER = "\033[92m"
    OKBLUE = "\033[34m"
    INFO = "\033[36m"
    OKGREEN = "\033[32m"
    WARNING = "\033[33m"
    FAIL = "\033[31m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    MAGENTA = "\033[95m"
    GREY = "\033[37m"
    FAINT = "\033[2m"

def color_text(text, color):
    """
    Wraps the text with the specified color.
    """
    return f"{color}{text}{Colors.ENDC}"  # Wraps the text with the specified color and resets the color at the end
