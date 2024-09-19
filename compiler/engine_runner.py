from .utils import *
from .compiler import compile
import subprocess

def execute(print_stderr = True):
    arg, OutFileName = compile()
    execution =  subprocess.run(["./compiler/run_engine.exe", str(arg), OutFileName], capture_output=True, text=True)
    print("STDOUT:\n", execution.stdout)
    if print_stderr: print("STDERR:\n", execution.stderr)
    print("computation returned:", execution.returncode)