from .utils import *
from .compiler import compile
from .ParallelComputationsHandler import ParallelComputationsHandler

# TO DO 
# in fun compiler_in_assembly in compiler.py
#   make the FileStream interface general to all users 
#   (The FileStream class has been modified locally, reverse the modification)
# GET_AARGS & CLEAN_AARGS
#    __ID/num will be passed by copy, and the value in the ar will be thrown away
#    const ID/num will be passed by copy, and the value in the ar will be reversed
#    ID/num& will be passed by swap, the modified value in the ar will be put in the original val
# optional: build the program memory in binary 
# optional: encode the entry point in the program memory.
# problem: the variable gets added in the enviroment also if the if branch in which they are
# declared is not executed 

def execute():
    SourceFileName, ExeFileName = get_files()
    entry_point = compile(SourceFileName, ExeFileName)
    pch = ParallelComputationsHandler()
    results = pch.run_parallel_computations(entry_point, ExeFileName)