from utils.colors import Colors, color_text

def prompt(cwd):
    """
    Returns a formatted prompt string with the current working directory.
    """
    return color_text("pyMiniOS ", Colors.BOLD) + color_text(cwd, Colors.OKCYAN) + color_text(" > ", Colors.BOLD)  # Returns a formatted prompt string

def print_error(message):
    """
    Prints an error message in red color.
    """
    print(color_text(message, Colors.FAIL))  # Prints an error message in red color

def print_warning(message):
    """
    Prints a warning message in orange color.
    """
    print(color_text(message, Colors.WARNING))  # Returns a formatted warning message string

def print_success(message):
    """
    Prints a success message in green color.
    """
    print(color_text(message, Colors.OKGREEN))  # Prints a success message in green color