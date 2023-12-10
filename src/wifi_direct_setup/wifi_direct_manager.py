import subprocess
import time
import logging
from pathlib import Path
from ..utils import run_bash


# Configuration
BASH_SCRIPT_PATH = "scripts/wifi_direct_setup.sh"
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# Setup logging
log_file_path = Path.home() / '.logs' / 'wifi_direct.log'
log_file_path.parent.mkdir(exist_ok=True)  # Ensure the log directory exists

logging.basicConfig(filename=log_file_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def check_and_install_wpa_supplicant():
    try:
        # Check if wpa_supplicant is installed using 'which wpa_cli'
        result = subprocess.run(['which', 'wpa_cli'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not result.stdout.strip():
            # wpa_cli not found, install wpa_supplicant
            logging.info("wpa_supplicant not found. Installing wpa_supplicant...")
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'wpasupplicant'], check=True)
            logging.info("wpa_supplicant installed successfully.")
        else:
            logging.info("wpa_supplicant is already installed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking/installing wpa_supplicant: {e.stderr.strip()}")


def run_bash_script():
    try:
        result = subprocess.run([BASH_SCRIPT_PATH], check=True, text=True, capture_output=True)
        logging.info("Bash script output: " + result.stdout)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Bash script error: {e.stderr.strip()}")
        return False, e.stderr.strip()


def main():
    # Check and install wpa_supplicant if necessary
    check_and_install_wpa_supplicant()

    retries = 0
    while retries < MAX_RETRIES:
        logging.info(f"Attempt {retries + 1} to set up Wi-Fi Direct")
        success, output = run_bash(BASH_SCRIPT_PATH)
        if success:
            logging.info("Wi-Fi Direct setup successful")
            print("Setup successful.")
            break
        else:
            logging.warning(f"Setup failed on attempt {retries + 1}. Retrying in {RETRY_DELAY} seconds...")
            print(f"Setup failed. Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
            retries += 1
    else:
        logging.error("Maximum retries reached. Setup failed.")
        print("Maximum retries reached. Setup failed.")


if __name__ == "__main__":
    main()
