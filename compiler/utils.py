import os
import subprocess
import shutil
from antlr4 import CommonTokenStream
from antlr4.tree.Tree import TerminalNodeImpl
import pydot
import sys


def clean_dir(path  = ".\\antlr_files",
               file_da_salvare = []):
    if not os.path.exists(path):
        print(path, "doesn't not exist, no cleaning performed")
        return
    for file in os.listdir(path):
        if (not file in file_da_salvare) and os.path.isfile(os.path.join(path, file)): 
            os.remove(os.path.join(path, file))
    return 0

def build_grammar(path = ".\\antlr_files", main_gram = "Gram.g4", 
                  other_grams = ["GrammaticaLessico.g4"]):
    original_dir = os.getcwd()
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    print(os.getcwd())
    other_grams += [main_gram]
    for gram in other_grams:
        shutil.move(os.path.join(original_dir, gram), 
                    '.')
    command = ["antlr4", "-Dlanguage=Python3", main_gram, "-visitor"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.stderr + result.stdout != "" or result.returncode != 0:
        print("during compilation of grammar: ")
        print(result.stderr +  result.stdout)
    for gram in other_grams:
        shutil.move(gram,
                    original_dir)

    os.chdir(original_dir)
    return 1

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

def riconfigura_engine(file_path = "run_engine.cpp"):
    name_length = file_path.find(".")
    compilation = subprocess.run(["g++", file_path, "-o", file_path[:name_length] + ".exe"], capture_output=True, text=True)
    return compilation 

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