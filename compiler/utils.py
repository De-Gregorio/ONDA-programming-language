import os
import subprocess
import shutil
from antlr4 import CommonTokenStream
from antlr4.tree.Tree import TerminalNodeImpl
import pydot
import sys


def clean_dir(path, file_da_salvare = []):
    if not os.path.exists(path):
        print(path, "doesn't  exist, no cleaning performed")
        return
    for file in os.listdir(path):
        if (not (file in file_da_salvare))\
            and os.path.isfile(os.path.join(path, file)): 
            os.remove(os.path.join(path, file))
    return 0

def build_grammar(folder = "antlr_files", main_gram = "Gram.g4", 
                  other_grams = ["GrammaticaLessico.g4"]):
    
    main_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(main_dir, folder)):
        os.makedirs(os.path.join(main_dir, folder))
    else: 
        clean_dir(os.path.join(main_dir, folder))

    all_grams = [main_gram] + other_grams
    for gram in all_grams:
        shutil.move(os.path.join(main_dir, gram),
                    os.path.join(main_dir, folder))
    command = ["antlr4", "-Dlanguage=Python3", os.path.join(main_dir, folder, main_gram), "-visitor"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.stderr + result.stdout != "" or result.returncode != 0:
        print("during compilation of grammar: ")
        print(result.stderr + result.stdout)
    for gram in all_grams:
        shutil.move(os.path.join(main_dir, folder, gram), 
                    os.path.join(main_dir),)
    return 1

def compile_engine():
    main_dir = os.path.dirname(os.path.abspath(__file__))
    inp_file_path = os.path.join(main_dir, "run_engine.cpp")
    out_file_path = os.path.join(main_dir, "run_engine.exe")
    compilation = subprocess.run(["g++", inp_file_path, "-o", out_file_path], capture_output=True, text=True)
    return compilation 

def create_graph(tree, rule_names):
    # Creiamo il grafo
    from .antlr_files.GramParser import GramParser

    dot_graph = tree.toStringTree(ruleNames=rule_names, recog=tree.parser)
    
    # Inizializziamo l'oggetto pydot
    graph = pydot.Dot(graph_type='digraph')

    # Aggiungiamo i nodi e gli archi
    def add_node_and_edges(node, parent=None):
        label = rule_names[node.getRuleIndex()] #+ "\:" + str(node.getAltNumber())
        if isinstance(node, GramParser.ExprContext):
            label += "\:" + str(node.placeholder)
        if isinstance(node, GramParser.IpAssignContext):
            label += "\:" + str(node.to_substitute)
        node_id = str(id(node))
        graph.add_node(pydot.Node(node_id, label=label))

        if parent:
            graph.add_edge(pydot.Edge(parent, node_id))

        for child in node.getChildren():
            if isinstance(child, TerminalNodeImpl):
                child_label = child.getText()
                if child_label == ',': #using "," cause conflict error with graphviz
                    child_label = "-"
                child_id = str(id(child))
                graph.add_node(pydot.Node(child_id, label=child_label))
                graph.add_edge(pydot.Edge(node_id, child_id))
            else:
                add_node_and_edges(child, node_id)
    add_node_and_edges(tree)
    graph.write_png('parse_tree.png')
    return graph


def run_from_assem_file(): # usefull when manual changes have been made to the assembly
    from .compiler import assemble
    with open("out.qas", "r") as file:
        assembly = file.read()
    binary, arg = assemble(assembly)
    with open("out.exe", "w") as out_file:
        out_file.write(binary)
    print(arg)
    execution =  subprocess.run(["./compiler/run_engine.exe", str(arg), "out.exe"], capture_output=True, text=True)
    print("STDOUT:\n", execution.stdout)
    print("STDERR:\n", execution.stderr)
    print("computation returned:", execution.returncode)

def get_files():
    """used to get the file names from argv
    expected inp:
    python main.py input.onda outfilename
    """
    SourceFileName = sys.argv[1]
    if len(sys.argv) < 3:
        OutFileName = "out.exe"
    else:
        OutFileName = sys.argv[2]  
    if OutFileName[-4:] != ".exe":
        OutFileName += ".exe"
    return SourceFileName, OutFileName

def setup(only_compile_engine = False):
    print(compile_engine().stderr)
    if not only_compile_engine: build_grammar()