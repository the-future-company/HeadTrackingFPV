import subprocess
import time
import logging
from pathlib import Path

from ..utils import run_bash, setup_logs

BASH_SCRIPT_PATH = "scripts/wifi_direct_setup.sh"
MAX_RETRIES = 3
RETRY_DELAY_IN_SECONDS = 5


def check_and_install_wpa_supplicant():
    try:
        result = subprocess.run(['which', 'wpa_cli'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not result.stdout.strip():
            logging.info("wpa_supplicant not found. Installing wpa_supplicant...")
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'wpasupplicant'], check=True)
            logging.info("wpa_supplicant installed successfully.")
        else:
            logging.info("wpa_supplicant is already installed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking/installing wpa_supplicant: {e.stderr.strip()}")


def setup_wifi_direct_with_retries():
    retries = 0
    while retries < MAX_RETRIES:
        logging.info(f"Attempt {retries + 1} to set up Wi-Fi Direct")
        success, output = run_bash(BASH_SCRIPT_PATH)
        if success:
            logging.info("Wi-Fi Direct setup successful")
            print("Setup successful.")
            break
        else:
            logging.warning(f"Setup failed on attempt {retries + 1}. Retrying in {RETRY_DELAY_IN_SECONDS} seconds...")
            print(f"Setup failed. Retrying in {RETRY_DELAY_IN_SECONDS} seconds...")
            time.sleep(RETRY_DELAY_IN_SECONDS)
            retries += 1
    else:
        logging.error("Maximum retries reached. Setup failed.")
        print("Maximum retries reached. Setup failed.")


def main():
    setup_logs(Path(__file__).name)
    check_and_install_wpa_supplicant()
    setup_wifi_direct_with_retries()


if __name__ == "__main__":
    main()
