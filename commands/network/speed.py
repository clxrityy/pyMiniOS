from core.wifi.diagnostics.signal import run_speed_test
from utils.io import print_info, print_success, print_error, print_warning

def cmd_speed(_args, _shell):
    try:
        print_success("Running speed test...")
        result = run_speed_test()
        for key, value in result.items():
            print_info(f"{key}: {value}")
        print_success("Speed test completed successfully.")
    except Exception as e:
        print_error(f"An error occurred while running the speed test: {e}")
        print_warning("Please ensure you have an active internet connection and try again.")