import os
import subprocess
import sys
from utils import *
from antlr4 import *
from antlr_files.GramLexer import GramLexer # type: ignore
from antlr_files.GramParser import GramParser 
from CodeGenerator import CodeGenerator
from SemanticChecker import SemanticChecker

# original_dir = os.getcwd()
# fileName = os.path.join(original_dir + sys.argv[1])
# os.chdir("c:\\Users\\frajr\\OneDrive\\Desktop\\quantum_computation\\qcpuv0\\compiler")

antrl_files_path = ".\\antlr_files"
# clean_dir()
# build_grammar(antrl_files_path)
# sys.path.append(antrl_files_path)



print("Grammar Building complete..")

with open("input.txt", "r") as file:
    contenuto = file.read()
print(contenuto)
# input_stream = FileStream(read_from_file = True, fileName=fileName)
input_stream = FileStream(read_from_file=False, contenuto=contenuto)
lexer = GramLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = GramParser(stream)
tree = parser.program()
if parser.getNumberOfSyntaxErrors() > 0:
    print("syntax errors")
    exit()
else:
    print("Parsing Completed..")
    cg = CodeGenerator()  
    assembly = cg.generate_code(tree)
    assembly = "entry point: " + str(cg.blocks_info["main"]["ENTRY_LINE"] + 1) + "\n" + assembly 
    create_graph(tree, parser.ruleNames)


# os.chdir(original_dir)
out_file_path = "out.qas"
# try:
#     out_file_path = sys.argv[2]
# except IndexError:
#     out_file_path = "out.qas"

with open(out_file_path, "w") as file:
    file.write(assembly)


 
