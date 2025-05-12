from utils.colors import Colors

def error(label, error):
    print(f"{Colors.FAIL}{Colors.BOLD}{label}: {error}{Colors.ENDC}")