from utils.colors import Colors, color_text

def prompt(cwd):
    """
    Returns a formatted prompt string with the current working directory.
    """
    return color_text("pyMiniOS ", Colors.BOLD) + color_text(cwd, Colors.INFO) + color_text(" > ", Colors.BOLD)  # Returns a formatted prompt string

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
    
def print_info(message):
    """
    Prints an info message in blue color.
    """
    print(color_text(message, Colors.OKBLUE))  # Prints an info message in blue color
    
def print_heading(message):
    """
    Prints a heading message in bold.
    """
    print(color_text(message, Colors.HEADER))  # Prints a heading message in bold and blue color
    
def print_magenta(message):
    """
    Prints a message in magenta color.
    """
    print(color_text(message, Colors.MAGENTA))  # Prints a message in magenta color
    
def print_grey(message):
    """
    Prints a message in coral color.
    """
    print(color_text(message, Colors.GREY))  # Prints a message in coral color