import os
import platform
from datetime import datetime, timedelta

def get_system_uptime():
    """
    Print the system uptime in a human-readable format.
    Works on Windows, macOS, and Linux.
    """
    try:
        if platform.system() == "Windows":
            # For Windows, use the 'net statistics' command
            result = os.popen('net statistics workstation').read()
            for line in result.splitlines():
                if 'Statistics since' in line:
                    print(f"System Uptime: {line}")
        else:
            # For macOS and Linux, use the 'uptime' command
            uptime_result = os.popen('uptime').read().strip()
            print(f"System Uptime: {uptime_result}")
    except Exception as e:
        print(f"Error retrieving uptime: {e}")

def get_uptime_seconds():
    """
    Get system uptime in seconds.
    Works on Windows, macOS, and Linux.
    """
    try:
        if platform.system() == "Windows":
            import subprocess
            result = subprocess.run(['net', 'statistics', 'workstation'], 
                                  capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if 'Statistics since' in line:
                    # Extract the datetime and calculate uptime
                    time_str = line.split('since')[-1].strip()
                    boot_time = datetime.strptime(time_str, '%m/%d/%Y %H:%M:%S %p')
                    uptime_delta = datetime.now() - boot_time
                    print(f"Uptime in seconds: {int(uptime_delta.total_seconds())}")
        else:
            # For Unix-based systems
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = int(float(f.readline().split()[0]))
                print(f"Uptime in seconds: {uptime_seconds}")
                
                # Convert to human-readable format
                uptime_time = timedelta(seconds=uptime_seconds)
                print(f"Uptime: {uptime_time}")
    except Exception as e:
        print(f"Error retrieving uptime in seconds: {e}")

if __name__ == "__main__":
    print("=== System Uptime Information ===")
    get_system_uptime()
    print()
    get_uptime_seconds()