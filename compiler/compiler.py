import sys
from .utils import *
from antlr4 import *
from .antlr_files.GramLexer import GramLexer # type: ignore
from .antlr_files.GramParser import GramParser 
from .CodeGenerator import CodeGenerator
from .assembler import build_program


def compile_in_assembly(FileName : str, to_build_graph = False):
    input_stream = FileStream(read_from_file=True, fileName=FileName)
    lexer = GramLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GramParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxError()
    else:
        cg = CodeGenerator()  
        assembly = cg.generate_code(tree)
        if to_build_graph:
            create_graph(tree, parser.ruleNames)   
    return assembly

def assemble(source_code : str):
    def get_program_entry_line(program):
        return int(program.split("\n")[0].split()[-1])
    binary = build_program(source_code)
    return binary, get_program_entry_line(source_code)

def compile():
    # python main.py input.* outfilename
    SourceFileName = sys.argv[1]
    if len(sys.argv) < 3:
        OutFileName = "out.exe"
    else:
        OutFileName = sys.argv[2]  
    if OutFileName[-4:] != ".exe":
        OutFileName += ".exe"
    assembly = compile_in_assembly(SourceFileName)
    binary, arg = assemble(assembly)
    with open(OutFileName, "w") as out_file:
        out_file.write(binary)            
    return arg, OutFileName
