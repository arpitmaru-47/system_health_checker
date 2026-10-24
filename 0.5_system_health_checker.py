import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as error:
        return f"ERROR: {error.stderr.strip()}"

checks ={
    "Current user": ["whoami"],
    "Disk usage": ["df", "-h"],
    "Python version": ["python3", "--version"]
}

for name, command in checks.items():
    print(f"\n=== {name} ===")
    print(run_command(command))