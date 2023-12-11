import logging
import subprocess
from pathlib import Path


def setup_logs(log_name: str):
    log_file_path = Path.home() / '.logs' / f'{log_name}.log'
    log_file_path.parent.mkdir(exist_ok=True)

    logging.basicConfig(filename=log_file_path, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


def run_bash(script_path: str, cwd=None) -> (bool, str):
    """
    Executes a Bash script located in the 'scripts' directory.
    :param script_path: The path of the Bash script to run.
    :param cwd: The current working directory to run the script in.
    :return: The stdout from the executed script.
    """
    script_path = Path(script_path)

    # Get cwd
    if not cwd:
        cwd = Path.cwd()

    # Ensure the script exists
    if not script_path.is_file():
        raise FileNotFoundError(f"The script at {script_path} does not exist.")

    # Execute the script
    try:
        result = subprocess.run([str(script_path)],
                                cwd=cwd,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, check=True)
        print(f"Script {script_path.name} executed successfully.")
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path.name}: {e.stderr.strip()}")
        return False
