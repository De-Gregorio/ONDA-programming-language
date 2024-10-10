import subprocess
intructions_info = {
    "add"   : (0, (5, 5, -16)),
    "addi"  : (1, (5, 21)),
    "cadd"  : (2, (5, 5, 5, -11)),
    "caddi" : (3, (5, 5, 16)),
    "sub"   : (4, (5, 5, -16)),
    "subi"  : (5, (5, 21)),
    "csub"  : (6, (5, 5, 5, -11)),
    "csubi" : (7, (5, 5, 16)),
    "div"   : (8, (5, 5, 5, -11)),
    "divi"  : (9, (5, 5, 16)),
    "cdiv"  : (10, (5, 5, 5, 5, -6)),
    "cdivi" : (11, (5, 5, 5, 11)),
    "mul"   : (12, (5, 5, 5, -11)),
    "muli"  : (13, (5, 5, 16)),
    "cmul"  : (14, (5, 5, 5, 5, -6)),
    "cmuli" : (15, (5, 5, 5, 11)),
    "sw"  : (16, (5, 5, 16)),
    "xorsi"  : (17, (5, 21)),
    "lu"    : (18, (-26,)),
    "lui"   : (19, (-26,)),
    "feq"   : (20, (5, 5, 5, -11)),
    "feqi"  : (21, (5, 5, 16)),
    "fne"   : (22, (5, 5, 5, -11)),
    "fnei"  : (23, (5, 5, 16)),
    "flt"   : (24, (5, 5, 5, -11)),
    "flti"  : (25, (5, 5, -16)),
    "nop"   : (26, (-26,)),
    "neg"   : (27, (5, -21)),
    "tcsu"  : (28, (5, 5, 5, 5, -6)),
    "rebi"  : (29, (5, 5, 5, -11)),
    "flip"  : (30, (5, -21)),
    "outr"  : (31, (5, -21)),
    "swre"  : (32, (5, 5, -16)),
    "ta"    : (33, (5, -21)),
    "lg"    : (34, (5, -21)), 
    "neg"   : (35, (5, -21)), 
    "rg"    : (36, (5, 5, -16)),
    "eop"   : (63, (-26,))
}


def register_to_index(register):
    # Define the register mapping
    registers_map = {
        "$zero": 0,
        "$u": 1,
        "$tur1": 2,
        "$v0": 3,
        "$v1": 4,
        "$a0": 5,
        "$a1": 6,
        "$a2": 7,
        "$a3": 8,
        "$s0": 9,
        "$s1": 10,
        "$s2": 11,
        "$s3": 12,
        "$s4": 13,
        "$s5": 14,
        "$s6": 15,
        "$s7": 16,
        "$s8": 17,
        "$s9": 18,
        "$t0": 19,
        "$t1": 20,
        "$t2": 21,
        "$t3": 22,
        "$t4": 23,
        "$t5": 24,
        "$t6": 25,
        "$t7": 26,
        "$t8": 27,
        "$grp": 28,
        "$sp": 29,
        "$fp": 30,
        "$tur2": 31
    }

    if register.isnumeric():
        return int(register)
    if register[1:].isnumeric():
        return int(register)
    result = registers_map.get(register, f"invalid register")
    if result == "invalid register":
        raise NameError(f"invalid register: {register}")
    return result


def index_to_register(index):
    # Define the register mapping reversed
    index_map = {
        0: "$zero",
        1: "$u",
        2: "$tur",
        3: "$v0",
        4: "$v1",
        5: "$a0",
        6: "$a1",
        7: "$a2",
        8: "$a3",
        9: "$s0",
        10: "$s1",
        11: "$s2",
        12: "$s3",
        13: "$s4",
        14: "$s5",
        15: "$s6",
        16: "$s7",
        17: "$s8",
        18: "$s9",
        19: "$t0",
        20: "$t1",
        21: "$t2",
        22: "$t3",
        23: "$t4",
        24: "$t5",
        25: "$t6",
        26: "$t7",
        27: "$t8",
        28: "$grp",
        29: "$sp",
        30: "$fp",
        31: "$ra"
    }
    
    return index_map.get(index, "Unknown index")

def negate(bin_str : str):
    new_str = ""
    for char in bin_str:
        if char == "0":
            new_str += "1"
        else:
            new_str += "0"
    return to_binary(int(new_str, 2) + 1, len(bin_str))

def to_binary(num, n_bit : int):
    if type(num) == str:
        num = int(num)
    if num < 0:
        num = -num
        if num > 2**(n_bit-1):
             raise ValueError(f"-{num} doesn't fit in {n_bit} bit")
        num = bin(num)[2:]
        return negate("0" * (n_bit-len(num)) + num)
    if num >= (2**n_bit):
        raise ValueError(f"{num} doesn't fit in {n_bit} bit")
    num = bin(num)[2:]
    return "0" * (n_bit-len(num)) + num

def build_inst(assem_line: str):
    
    words = assem_line.split()
    if words[0] not in intructions_info.keys():
        raise KeyError(f"{words[0]} is not a keyword")
    info = intructions_info[words[0]]
    n_param = 0
    for el in info[1]:
        if el > 0:
            n_param +=1

    if len(words)-1 != n_param:
        raise SyntaxError(f"in {assem_line}:\n{words[0]} needs {n_param} params, {len(words)-1} were given")
    instruction = to_binary(info[0], 6)
    for i, el in enumerate(info[1]):
        if el > 0:
            instruction += to_binary(words[i+1], el)
        else:
            instruction += "0" * (-el)
            
    return instruction

def replace_aliases(line:str):
    parts = line.split() 
    registers = [part.split(",")[0] for part in parts[1:]]
    registers_idxs = [str(register_to_index(r)) for r in registers]
    # registers = [str(register_to_index(parts[i].split(',')[0])) for i in range(1, len(parts))]
    new_line = parts[0]
    for idx in registers_idxs:
        new_line += " " + idx
    return new_line

def re_format_line(line:str):
    parts = line.split()
    inst = parts[0]
    if parts[0] != "sw":
        return replace_aliases(line)
    #sw $r1, $r2
    #sw $r1, offset($r2) 
    if not ("(" in line):
        # print(line + ", 0")
        # print(line.rstrip() + ", 0")
        return replace_aliases(line.rstrip() + ", 0")
    new_line = inst    
    reg1 = str(register_to_index(parts[1][:-1])) 
    reg2 = str(register_to_index(parts[-1].split("(")[1].split(")")[0]))
    offset = parts[-1].split('(')[0] 
    new_line += " " + reg1
    new_line += " " + reg2
    new_line += " " + offset
    if offset == "":
        new_line += "0"
    return new_line

def build_program(program : str):
    instructions = program.split("\n")[1:] # everything except the entry line instruction
    binary = ""
    for inst in instructions:
        inst = inst.split("#")
        if inst[0] != len(inst[0]) * " ":
            line = re_format_line(inst[0])
            binary += build_inst(line)
    return binary


def assemble(source_code : str, OutFileName : str = None):
    def get_entry_line(program):
        return int(program.split("\n")[0].split()[-1])

    if not OutFileName:
        OutFileName = "out.exe"
    with open(OutFileName, "w") as file:
        file.write(build_program(source_code))

    return get_entry_line(source_code)

    
def assemble_and_execute(source_code, debug = False):
    arg = assemble(source_code)
    if debug:
        print("..compiled..", arg)
    return subprocess.run(["./run_engine.exe", str(arg)], capture_output=True, text=True)

