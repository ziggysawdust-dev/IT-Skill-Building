#
#
import subprocess
import sys

def run_command(command):
    """Executes a shell command and prints its output."""
    try:
        process = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(process.stdout)
        if process.stderr:
            print(f"Error output:\n{process.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1) # Exit if a command fails

        run_command(sudo ./Hauspartytools)
