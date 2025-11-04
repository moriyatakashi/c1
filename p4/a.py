import subprocess
def aa():
    return subprocess.check_output(["./a.out"], text=True)
