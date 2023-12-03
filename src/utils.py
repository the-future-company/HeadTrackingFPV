import subprocess


def run_bash(script_path, cwd=None) -> str:
    """
    Executes a Bash script located in the 'scripts' directory.
    :param script_path: The path of the Bash script to run.
    :param cwd: The current working directory to run the script in.
    :return: The stdout from the executed script.
    """
    # Ensure the script exists
    if not script_path.is_file():
        raise FileNotFoundError(f"The script at {script_path} does not exist.")

    # Execute the script
    try:
        result = subprocess.run([str(script_path)],
                                cwd=cwd or script_path.parent,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, check=True)
        print(f"Script {script_path.name} executed successfully.")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path.name}: {e.stderr.strip()}")
        raise
