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

def update_kali():
    """Updates and upgrades Kali Linux."""
    print("Starting Kali Linux update and upgrade process...")

    # Update package lists
    print("\nUpdating package lists...")
    run_command("sudo apt update")

    # Upgrade installed packages
    print("\nUpgrading installed packages...")
    run_command("sudo apt full-upgrade -y")

    # Clean up unnecessary packages
    print("\nCleaning up unnecessary packages...")
    run_command("sudo apt autoremove -y")
    run_command("sudo apt clean")

    print("\nKali Linux update and upgrade complete.")

if __name__ == "__main__":
    update_kali()