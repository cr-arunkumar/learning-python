import subprocess
import time
from datetime import datetime
import os

def get_system_info():
    """Get detailed system information using top command"""
    try:
        # First try without the -w option (for older versions of top)
        cmd = ['top', '-b', '-n', '1']
        result = subprocess.run(cmd, 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True,
                              check=False)  # Changed to False to handle errors manually
        
        if result.returncode != 0:
            # If first attempt failed, try with different options
            cmd = ['top', '-b', '-n', '1', '-c']  # Added -c for command line
            result = subprocess.run(cmd,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  text=True,
                                  check=False)
            
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error running top. Exit code: {result.returncode}\nError message: {result.stderr}"
            
    except Exception as e:
        return f"Unexpected error: {e}"

def monitor_system():
    output_file = 'system_monitoring.txt'
    print(f"Starting system monitoring. Writing to {output_file}")
    print("Press Ctrl+C to stop monitoring")

    try:
        while True:
            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Get system information
            system_info = get_system_info()
            
            # Write to file
            with open(output_file, 'a') as file:
                file.write(f"\n{'='*80}\n")
                file.write(f"System Status at {timestamp}\n")
                file.write(f"{'='*80}\n")
                file.write(system_info)
                file.write(f"\n{'='*80}\n")
            
            print(f"Information written at {timestamp}")
            
            # Wait for 5 seconds
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user")
    except Exception as e:
        print(f"Error occurred: {e}")
        
def check_top_installed():
    """Check if top is installed and available"""
    try:
        result = subprocess.run(['which', 'top'], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True)
        return result.returncode == 0
    except:
        return False

if __name__ == "__main__":
    # Check if top is installed
    if not check_top_installed():
        print("Error: 'top' command not found. Please install procps package.")
        exit(1)
        
    # Create new file or clear existing one
    with open('system_monitoring.txt', 'w') as file:
        file.write("System Monitoring Started\n")
    
    monitor_system()