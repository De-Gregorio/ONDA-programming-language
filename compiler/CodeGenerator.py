from builtins import *
from .antlr_files.GramVisitor import GramVisitor
from .antlr_files.GramParser import GramParser 
from antlr4.tree.Tree import TerminalNodeImpl
from .PlaceHolderAssigner import PlaceHolderAssigner
from .SemanticChecker import SemanticChecker

class IncreadiblyCapableString():
    """this object just count at which line of the 
    assembly program  you are at the moment"""
    def __init__(self, debug = False):
        self.value = ""
        self.current_line = -1
        self.debug = debug

    def __iadd__(self, stringa):
        self.value += stringa
        if stringa[0] != "#":
            self.current_line += 1
            if self.debug:
                self.value = self.value[:-1] + "\t# " + str(self.current_line) + "\n"
            # self.value += "outr 31"
            # self.current_line += 1
            # if self.debug:
            #     self.value = self.value + "\t\t# " + str(self.current_line) + "\n"
        return self

class IdGrabber(GramVisitor):
    def __init__(self, parser:GramParser):
        self.parser = parser
    
    def get_ids(self, ctx):
        self.ids = []
        self.visit(ctx)
        return self.ids

    def visitTerminal(self, node):
        if node.getSymbol().type == self.parser.ID:
            self.ids.append(node.getText())

class CodeGenerator(GramVisitor):    
    def __init__(self):
        self.sign_to_instruction = {
            "+" : "add",
            "-" : "sub",
            "*" : "mul", 
            "^" : "xor",
            "#" : "z",
            "@" : "had",
            "==" : "feq", 
            "<" : "flt", 
            "!=" : "fne"
        }
        self.sign_to_rinstruction = {
            "+" : "sub",
            "-" : "add",
            "*" : "mul", 
            "^" : "xor",
            "#" : "nop",
            "@" : "nop",
            "==" : "feq", 
            "<" : "flt", 
            "!=" : "fne"   
        }

    def generate_code(self, tree):
        self.output = IncreadiblyCapableString(debug=True)
        self.enviroment = {"ACCESABLE" : {}, "INACCESABLE" : {}}
        self.vars_sizes = {"ACCESABLE" : {}, "INACCESABLE" : {}}
        self.current_block_id = 0
        self.fp_offset = 0 
        self.active_expr = 0
        self.not_const_vars = [] # list of IDs
        self.parser = tree.parser
        self.pha = PlaceHolderAssigner()
        self.idg = IdGrabber(self.parser)
        self.functions_fargs = SemanticChecker().check_errors(tree)
        self.blocks_info = {} # [block(or function)_id].key() = ["ENTRY_LINE", "LENGTH"] 
        self.visitProgram(tree)
        self.replace_labels()
        self.output.value = "entry point: " + \
            str(self.blocks_info["main"]["ENTRY_LINE"] + 1) + "\n" + \
            self.output.value 
        return self.output.value
  
    def get_fargs_size(self, fargs):
        fargs_size = 0 
        for farg in fargs:
            fargs_size += 1 if farg["ARR_SIZE"] == 0 else farg["ARR_SIZE"]
        return fargs_size

    def visitProgram(self, ctx:GramParser.ProgramContext):
        self.visitChildren(ctx)
        return self.output

    def visitFunctionImpl(self, ctx: GramParser.FunctionImplContext):
        F_ID = ctx.ID().getText()
        self.current_F_ID = F_ID
        self.current_block_id += 1
        fargs = self.functions_fargs[ctx.ID().getText()]
        old_active_expr = self.active_expr
        old_env = self.get_env_copy()
        old_vars_size = self.get_vars_sizes_copy()
        old_fp_offset = self.fp_offset

        # STACK COMPOSITION AT CALL
        # old_fp
        # x1
        # ..
        # x_n
        # ra $fp
        # 0  $sp
        # 0 
        fargs_size = self.get_fargs_size(fargs)
        self.fp_offset = fargs_size

        for farg in fargs:
            self.enviroment["ACCESABLE"][farg["ID"]] = self.fp_offset
            self.vars_sizes["ACCESABLE"][farg["ID"]] = 1 if farg["ARR_SIZE"] == 0 else farg["ARR_SIZE"]
            self.fp_offset -= 1 if farg["ARR_SIZE"] == 0 else farg["ARR_SIZE"]

        self.blocks_info[F_ID] = {}
        self.blocks_info[F_ID]["ENTRY_LINE"] = self.output.current_line + 1
        if ctx.body():
            self.output += "swre $u, $tur1\n"
            self.pha.reset_values()
            temporaries_needed = self.pha.visit(ctx.body()) 
            self.blocks_info[F_ID]["TEMPORARIES_NEEDED"] = temporaries_needed
            self.declare("INACCESABLE", "temporaries"+str(self.current_block_id), size = temporaries_needed)
            self.set_top_of_the_stack() 
            self.visit(ctx.body())
            self.blocks_info[F_ID]["LENGTH"] = self.output.current_line - self.blocks_info[F_ID]["ENTRY_LINE"] + 1
        else:
            raise NameError("write a body, MOVE")
            # self.output += "nop\n" # WRONG YOU MUST RETURN ANYWAYS  
        
        # self.current_block_id -= 1
        self.enviroment = old_env
        self.vars_sizes = old_vars_size
        self.fp_offset = old_fp_offset 
        self.active_expr = old_active_expr
        return 0  
    
    def visitFunctionCall(self, ctx: GramParser.FunctionCallContext):
        F_ID = ctx.ID().getText()
        # AR BUILDING
        fargs_size = self.get_fargs_size(self.functions_fargs[F_ID])
        self.load_aargs(ctx)
        self.output += "addi $sp, -" + str(fargs_size + 1) + "\n" # it's offsetted by 1 because it also  
                                                                  # needs to store the old_fp by default
        self.output += "sw $fp, " + str(fargs_size + 1) + "($sp)\n" # store old fp
        self.output += "add $fp, $sp\n"
        self.output += "addi $sp, -1\n" 
        # JUMP TO FUNCTION BODY
        self.output += "sw $tur1, $fp\n"
        self.output += f"addi $tur1, #{F_ID}@ENTRY_LINE\n" 
        self.output += f"subi $tur1, {self.output.current_line + 2}\n" 
        self.output += f"swre $tur1, $u\n" # actual jump (that line is the c_pc)
        # tur -= c_pc - f_pc - fun_len + 1
        self.output += f"subi $tur1, {self.output.current_line+1}\n" # - fp_pc - fun_len 
        self.output += f"addi $tur1, #{F_ID}@ENTRY_LINE\n"           # - fun_len 
        self.output += f"add $tur1, $v1\n"               # 0
        self.output += f"ta $v1\n"
        self.output += "sw $tur1, $fp\n"
        # CLEAN AR
        self.output += "addi $sp, 1\n"
        self.output += "sub $fp, $sp\n"
        self.output += "sw $fp, " + str(fargs_size + 1) + "($sp)\n" # reload old fp
        self.output += "addi $sp, " + str(fargs_size + 1) + "\n"
        self.output += f"# start of cleaning of {self.current_F_ID}\n"
        self.clean_aargs(ctx)
        # SET THE RA IN THE SPOT POINTED BY THE FP
        return 0
    
    def visitReturnStmt(self, ctx: GramParser.ReturnStmtContext):
        # tur = f_pc - c_pc

        # tur *= -1            = c_pc - f_pc
        # tur -= fun_len       = c_pc - fp_pc - fun_len
        # tur += 1             = c_pc - fp_pc - fun_len + 1
        # swap ur tur          (fp_pc + fun_len) + c_pc - fp_c - fun_len  = c_pc + 1
        save_env = self.get_env_copy()
        save_vars_sizes = self.get_vars_sizes_copy()
        save_fp_offset = self.fp_offset
        if ctx.expr():
            self.visit(ctx.expr())
            self.output += "add $t1, $a0\n"
            self.output += "addi $sp, -1\n"
            self.output += "sw $t1, 1($sp)\n"
            self.output += "sw $a0, -"  + str(ctx.expr().placeholder) + "($fp)\n"
            self.rvisitExpr(ctx.expr())
            self.output += "sw $v0, 1($sp)\n"
            self.output += "addi $sp, 1\n"
        self.output += f"# start return of {self.current_F_ID}\n"
        self.clean_local_vars()
        if self.current_F_ID == "main":
            self.output += "eop\n"
            self.enviroment = save_env
            self.vars_sizes = save_vars_sizes
            self.fp_offset = save_fp_offset
            self.set_top_of_the_stack()
            return 0
        self.output += "neg $tur1\n"
        self.output += f"addi $v1, #{self.current_F_ID}@DISTANCE_TO_{self.output.current_line+4}\n"
        self.output += f"subi $tur1, #{self.current_F_ID}@DISTANCE_TO_{self.output.current_line+3}\n"
        self.output += "addi $tur1, 1\n"
        self.output += "swre $u, $tur1\n"
        self.blocks_info[self.current_F_ID]["ENTRY_LINE"]
        self.output += f"# end return of {self.current_F_ID}\n"
        self.enviroment = save_env
        self.vars_sizes = save_vars_sizes
        self.fp_offset = save_fp_offset
        self.set_top_of_the_stack()

        return 0
 
    def clean_local_vars(self):
        keys = list(self.enviroment["ACCESABLE"].keys())
        for V_ID in keys:
            if self.enviroment["ACCESABLE"][V_ID] < 0:
                self.deallocate("ACCESABLE", V_ID, with_ta=True)
        keys = list(self.enviroment["INACCESABLE"].keys())
        for V_ID in keys:
            if self.enviroment["INACCESABLE"][V_ID] < 0:
                if "temporaries" in V_ID:
                    if self.active_expr != 0:
                        self.deallocate("INACCESABLE", V_ID, with_ta=True)
                    else:
                        self.deallocate("INACCESABLE", V_ID, with_ta=False)
                else:
                    self.deallocate("INACCESABLE", V_ID, with_ta=True)

    def load_aargs(self, ctx : GramParser.FunctionCallContext):
        fargs = self.functions_fargs[ctx.ID().getText()]
        ctx = ctx.aargs()
        sp_offset = -1 # reserve place for the old fp
        for farg in fargs:
            if True: # if passed in copy mode
                sp_offset = self.load_copy_aarg(ctx, farg, sp_offset)
                ctx = ctx.aargs()
            else: # if passed in reference or const mode
                pass
    
    def load_const_aarg():
        pass 

    def load_reference_aarg():
        pass

    def load_copy_aarg(self, ctx: GramParser.AargsContext, farg, sp_offset):
        if ctx.ID():
            fp_offset = self.enviroment["ACCESABLE"][ctx.ID().getText()]
            self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
            self.output += "add $a0, $t1\n"
            self.output += "sw $a0, " + str(sp_offset) + "($sp)\n" 
            self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
            sp_offset -= 1
            if farg["ARR_SIZE"] != 0:
                for i in range(1, farg["ARR_SIZE"]):
                    fp_offset -= 1
                    self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
                    self.output += "add $a0, $t1\n"
                    self.output += "sw $a0, " + str(sp_offset) + "($sp)\n" 
                    self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
                    sp_offset -= 1
        elif ctx.num():
            self.visit(ctx.num()) # not really a copy but it's ok
            self.output += "sw $a0, " + str(sp_offset) + "($sp)\n" 
            sp_offset -= 1
        elif ctx.expr():
            self.visit(ctx.expr())
            self.output += "add $t1, $a0\n"
            self.output += "sw $t1, " + str(sp_offset) + "($sp)\n" 
            self.output += "sw $a0, -" + str(ctx.expr().placeholder) + "($fp)\n"
            self.rvisitExpr(ctx.expr())
            sp_offset -= 1 
        return sp_offset
    
    def clean_aargs(self, ctx: GramParser.FunctionCallContext):
        fargs = self.functions_fargs[ctx.ID().getText()]
        ctx = ctx.aargs()
        sp_offset = -1
        for farg in fargs:
            if True: # if passed in copy mode
                sp_offset = self.clean_copy_aarg(ctx, farg, sp_offset)
                ctx = ctx.aargs()
            else: # if passed in reference or const mode
                pass

    def clean_const_aarg():
        pass 

    def clean_reference_aarg():
        pass

    def clean_copy_aarg(self, ctx: GramParser.AargsContext, farg, sp_offset):
        if ctx.ID():
            self.output += "sw $a0, " + str(sp_offset) + "($sp)\n" 
            self.output += "ta $a0\n"
            sp_offset -= 1
            if farg["ARR_SIZE"] != 0:
                for _ in range(1, farg["ARR_SIZE"]):
                    self.output += "sw $a0, " + str(sp_offset) + "($sp)\n" 
                    self.output += "ta $a0\n"
                    sp_offset -= 1
        elif ctx.num():
            self.output += "sw $a0, " + str(sp_offset) + "($sp)\n" 
            self.output += "ta $a0\n"
            sp_offset -= 1
        elif ctx.expr():
            self.output += "sw $a0, " + str(sp_offset) + "($sp)\n" 
            self.output += "ta $a0\n"
            sp_offset -= 1
        return sp_offset
    
    def visitBody(self, ctx: GramParser.BodyContext):
        # old_env = self.get_env_copy()
        self.visitChildren(ctx)
        # TO IMPLEMENT
        # keys = list(self.enviroment["ACCESABLE"].keys())
        # # print("old_env = ", old_env)
        # # print("new_env = ", self.enviroment)
        # for V_ID in keys:
        #     if not (V_ID in old_env["ACCESABLE"].keys()):
        #         # print(V_ID, "removed")
        #         self.deallocate("ACCESABLE", V_ID)
        # self.enviroment = old_env
        return 0
    
    def visitVarDecl(self, ctx:GramParser.VarDeclContext):
        ID = ctx.ID().getText()
        self.vars_sizes["ACCESABLE"][ID] = 1
        if ID in self.enviroment["ACCESABLE"].keys(): # to remove since MemoryCalculator already does this check
            raise NameError(f"redeclaration of {ID} isn't allowed") 
        if ctx.getChildCount() == 2: # TYPE ID
            self.output += "addi $sp, -1\n"
            self.fp_offset -= 1
            self.enviroment["ACCESABLE"][ID] = self.fp_offset
        elif ctx.EQUAL_SIGN(): # TYPE ID = expr
            self.output += "addi $sp, -1\n"
            self.fp_offset -= 1
            self.enviroment["ACCESABLE"][ID] = self.fp_offset
            self.visit(ctx.expr())
            self.output += "add $t1, $a0\n" # copy a0 in t1
            self.output += "sw $t1, 1($sp)\n" # save the value in the ID var
            offset_temp = ctx.expr().placeholder
            self.output += "sw $a0, -" + str(offset_temp) + "($fp)\n"
            self.rvisitExpr(ctx.expr())
        elif ctx.OPENSQUARE(): # TYPE ID '['INT']' 
            arr_size = int(ctx.INT().getText())
            self.vars_sizes["ACCESABLE"][ID] = arr_size
            self.output += "addi $sp, -" + str(arr_size) + "\n"   
            self.fp_offset -= 1
            self.enviroment["ACCESABLE"][ID] = self.fp_offset
            self.fp_offset -= (arr_size - 1) 
        else:
            Warning("uknown declaration: ", ctx.getText())
        privacy, name = self.get_top_of_the_stack()
        self.top_of_the_stack_privacy = privacy
        self.top_of_the_stack_name = name
        self.top_of_the_stack_value = self.enviroment[privacy][name]

    def visitExpr(self, ctx:GramParser.ExprContext):
        """
        CHANGE THIS COMMENT!!!!
        in the forward pass, every (new) temporary is put in his placeholder except for
        the last result, that will be put in $a0
        """
        self.active_expr += 1
        if ctx.OP_ADDITIVE(): # expr OP_ADDITIVE expr
            op = ctx.OP_ADDITIVE().getText()
            inst = self.sign_to_instruction[op]
            expr1, expr2 = ctx.expr()
            self.visit(expr2) #cgen(e2|right branch) 
            offset = -expr2.placeholder
            self.output += "sw $a0, " + str(offset) + "($fp)\n"  
            self.visit(expr1) #cgen(e1|left branch)
            self.output += "sw $t1, " + str(offset) + "($fp)\n"
            self.output += inst + " $a0, $t1\n"
            self.output += "sw $t1, " + str(offset) + "($fp)\n"
            return 0
        if ctx.OP_MULTIPLICATIVE() or ctx.OP_COMPARATIVE(): # expr OP_MULTIPLICATIVE/ expr
            op = ctx.OP_MULTIPLICATIVE().getText() if ctx.OP_MULTIPLICATIVE() else \
                 ctx.OP_COMPARATIVE().getText()
            if op in ['>', '<=', '>=']:
                raise NameError("operator", op, "not implemented yet")
            inst = self.sign_to_instruction[op]
            expr1, expr2 = ctx.expr()
            self.visit(expr1)
            offset1 = -expr1.placeholder
            self.output += "sw $a0, " + str(offset1) + "($fp)\n"  
            self.visit(expr2)
            offset2 = -expr2.placeholder
            self.output += "sw $t1, " + str(offset1) + "($fp)\n" 
            self.output += "swre $a0, $t2\n"  
            self.output +=  inst + " $a0, $t1, $t2\n"
            self.output += "sw $t2, " + str(offset2) + "($fp)\n"
            self.output += "sw $t1, " + str(offset1) + "($fp)\n" 
        if ctx.TILDE():
            self.visit(ctx.expr(0))
            self.output += "flia $a0\n"
        if ctx.num(): # num
            self.visit(ctx.num())
            return 0
        if ctx.ID() and (not ctx.OPENSQUARE()): # ID
            fp_offset = self.enviroment["ACCESABLE"][ctx.ID().getText()]
            self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
            self.output += "add $a0, $t1\n"
            self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
        if ctx.GARBAGEPOINTER():
            self.output += "add $a0, $grp\n"
        if ctx.functionCall(): # functionCall
            self.output += "# start functionCall\n"
            self.visit(ctx.functionCall())
            self.output += "swre $a0, $v0\n"
            self.output += "# end functionCall\n"
        if ctx.OPENSQUARE(): # ID '[' expr ']'
            var_offset = self.enviroment["ACCESABLE"][ctx.ID().getText()]
            self.visit(ctx.expr(0)) 
            self.output += "swre $a0, $t0\n" # t0 = offset, a0 = 0
            # self.output += "sw $t1, (-$t0+var_offset)($fp)"
            self.output += "sub $fp, $t0\n"
            self.output += "sw $t1, " + str(var_offset) + "($fp)\n"
            self.output += "add $a0, $t1\n"
            self.output += "sw $t1, " + str(var_offset) + "($fp)\n"
            self.output += "add $fp, $t0\n"
            self.output += "sw $t0, -" + str(ctx.expr(0).placeholder) + "($fp)\n"
        if ctx.OPENPAREN(): # '(' expr ')'
            self.visit(ctx.expr(0))
            return 
        return 0

    def rvisitExpr(self, ctx:GramParser.ExprContext):
        """
        CHANGE THIS COMMENT!!!!
        in the reverse pass, every temporary is in his placeholder at the 
        start and at the end
        """
        self.active_expr -= 1
        if ctx == self.active_expr:
            self.active_expr = None
        if ctx.OP_ADDITIVE(): # expr OP_ADDITIVE expr
            op = ctx.OP_ADDITIVE().getText()
            inst = self.sign_to_rinstruction[op]
            expr1, expr2 = ctx.expr()
            offset1 = -expr1.placeholder
            offset2 = -expr2.placeholder
            if inst != "nop":
                self.output += "sw $t1, " + str(offset1) + "($fp)\n"
                self.output += "sw $t2, " + str(offset2) + "($fp)\n"
                self.output += inst + " $t1, $t2\n"
                self.output += "sw $t2, " + str(offset2) + "($fp)\n"
                self.output += "sw $t1, " + str(offset1) + "($fp)\n"
            self.rvisitExpr(expr1)
            self.rvisitExpr(expr2)
        if ctx.OP_MULTIPLICATIVE() or ctx.OP_COMPARATIVE(): # expr OP_MULTIPLICATIVE/COMPARATIVE expr
            op = ctx.OP_MULTIPLICATIVE().getText() if ctx.OP_MULTIPLICATIVE() else \
                 ctx.OP_COMPARATIVE().getText()
            inst = self.sign_to_rinstruction[op]
            expr1, expr2 = ctx.expr()
            offset0 = -ctx.placeholder
            offset1 = -expr1.placeholder
            offset2 = -expr2.placeholder
            self.output += "sw $t0, " + str(offset0) + "($fp)\n"
            self.output += "sw $t1, " + str(offset1) + "($fp)\n"
            self.output += "sw $t2, " + str(offset2) + "($fp)\n"
            self.output += inst + " $t0, $t1, $t2\n"
            self.output += "sw $t0, " + str(offset0) + "($fp)\n"
            self.output += "sw $t1, " + str(offset1) + "($fp)\n"
            self.output += "sw $t2, " + str(offset2) + "($fp)\n"
            self.rvisitExpr(expr1)
            self.rvisitExpr(expr2)
        if ctx.TILDE():
            offset = -ctx.placeholder
            self.output += "sw $t0, " + str(offset) + "($fp)\n"
            self.output += "flia $t0\n"
            self.output += "sw $t0, " + str(offset) + "($fp)\n"
            self.rvisitExpr(ctx.expr(0))
        if ctx.num(): # num
            offset = -ctx.placeholder
            self.output += "sw $a0, " + str(offset) + "($fp)\n"
            self.visit(ctx.num())
            # self.output += "sw $a0, " + str(offset) + "($fp)\n"  
            # since it is a leaf node you don't need to put 
            # the value back in the placeholder, because 
            # the expr placeholder is already 0 and there 
            # are no other reverse action to perform
            return 0
        if ctx.ID() and (not ctx.OPENSQUARE()): # ID
            if ctx.ID().getText() in self.not_const_vars:
                expr_offset = -ctx.placeholder
                self.output += "sw $a0, " + str(expr_offset) + "($fp)\n"    
                self.output += "ta $a0\n"
            else:
                fp_offset = self.enviroment["ACCESABLE"][ctx.ID().getText()]
                expr_offset = -ctx.placeholder
                self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
                self.output += "sw $a0, " + str(expr_offset) + "($fp)\n"
                self.output += "sub $a0, $t1\n"
                self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
            # self.output += "sw $a0, " + str(offset) + "($fp)\n"  
            # since it is a leaf node you don't need to put 
            # the value back in the placeholder, because 
            # the expr placeholder is already 0 and there 
            # are no other reverse action to perform
        if ctx.GARBAGEPOINTER():
            self.output += "sw $a0, " + str(-ctx.placeholder) + "($fp)\n"
            self.output += "sub $a0, $grp\n"
        if ctx.functionCall(): # functionCall
            expr_offset = -ctx.placeholder
            self.output += "sw $a0, " + str(expr_offset) + "($fp)\n"
            self.output += "ta $a0\n"
        if ctx.OPENSQUARE(): # ID '[' expr ']'
            var_offset = self.enviroment["ACCESABLE"][ctx.ID().getText()]
            self.output += "sw $t0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
            self.output += "sw $a0, " + str(-ctx.placeholder) + "($fp)\n"
            # self.output += "sw t1, (-$t0+var_offset)($fp)"
            self.output += "sub $fp, $t0\n"
            self.output += "sw $t1, " + str(var_offset) + "($fp)\n"
            self.output += "sub $a0, $t1\n"
            self.output += "sw $t1, " + str(var_offset) + "($fp)\n"
            self.output += "add $fp, $t0\n"
            self.output += "sw $t0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
            self.rvisitExpr(ctx.expr(0))
        if ctx.OPENPAREN(): #c '(' expr ')'
            self.rvisitExpr(ctx.expr(0)) 
        return 0

    def visitReAssign(self, ctx: GramParser.ReAssignContext):
        V_ID = ctx.ID().getText()
        var_offset = self.enviroment["ACCESABLE"][V_ID]
        self.not_const_vars.append(V_ID)
        if ctx.OPENSQUARE(): # ID '[' expr ']' = expr
            # a[a[0]] = a[0] + 1;
            self.visit(ctx.expr(1)) # $a0 = new_value
            self.output += "add $t0, $a0\n"
            self.output += "addi $sp, -1\n"
            self.output += "sw $t0, 1($sp)\n"
            self.output += "sw $a0, -" + str(ctx.expr(1).placeholder) + "($fp)\n"
            self.rvisitExpr(ctx.expr(1))
            self.output += "sw $t0, 1($sp)\n"
            self.output += "addi $sp, 1\n"
            self.visit(ctx.expr(0)) # $a0 = offset 
            # a0 = offset, t0 = new_value
            # self.output += "sw t0, (-$a0+var_offset)($fp)"
            self.output += "sub $fp, $a0\n"
            self.output += "sw $t0, " + str(var_offset) + "($fp)\n"
            self.output += "add $fp, $a0\n"
            self.output += "ta $t0\n"
            self.output += "sw $a0, -" + str(ctx.expr(0).placeholder) + "($fp)\n"
            self.rvisitExpr(ctx.expr(0))
        else: # ID = expr
            self.visit(ctx.expr(0))
            self.output += "add $t0, $a0\n"
            self.output += "sw $a0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
            self.output += "sw $t0, " + str(var_offset) + "($fp)\n"
            self.output += "ta $t0\n"
            self.rvisitExpr(ctx.expr(0))
        self.not_const_vars.remove(V_ID)
        return 0

    def visitReAssignS(self, ctx: GramParser.ReAssignSContext):
        # _gp = expr
        self.visit(ctx.expr())
        self.output += "add $t0, $a0\n"
        self.output += "swre $grp, $a0\n"
        self.output += "ta $a0\n"
        self.output += "sw $t0, " + str(-ctx.expr().placeholder) + "($fp)\n"
        self.rvisitExpr(ctx.expr())
        return 0

    def visitIpAssignS(self, ctx:GramParser.IpAssignSContext):
        # _gp OP_INPLACE expr
        op = ctx.OP_INPLACE().getText()[0]
        inst = self.sign_to_instruction[op]
        self.visit(ctx.expr())
        self.output += inst + " $grp, $a0\n"
        self.output += "sw $a0, " + str(-ctx.expr().placeholder) + "($fp)\n"
        self.rvisitExpr(ctx.expr())
        return 0

    def visitSwap(self, ctx:GramParser.SwapContext):
        # (ID | GARBAGEPOINTER) ',' (ID | GARBAGEPOINTER)
        V1_ID = ctx.getChild(1).getText()
        V2_ID = ctx.getChild(3).getText()
        def swap_vars():
            if V1_ID == "_gp":
                self.output += "swre $grp, $t0\n"
            else:
                self.swap_var_in("$t0", "ACCESABLE", V1_ID)
            if V2_ID == "_gp":
                self.output += "swre $grp, $t1\n"
            else:
                self.swap_var_in("$t1", "ACCESABLE", V2_ID)

        swap_vars()
        self.output += "swre $t0, $t1\n"
        swap_vars()
        return 0

    def visitIpAssign(self, ctx: GramParser.IpAssignContext):
        op = ctx.OP_INPLACE().getText()[0]
        inst = self.sign_to_instruction[op] 
        var_offset = self.enviroment["ACCESABLE"][ctx.ID().getText()]

        if ctx.to_substitute:
            if ctx.OPENSQUARE(): # # ID '[' expr ']' OP_INPLACE expr
                self.visit(ctx.expr(1)) # new value to add
                self.output += "add $t0, $a0\n"
                self.save_in_stack("$t0")
                self.output += "sw $a0, " + str(-ctx.expr(1).placeholder) + "($fp)\n"
                self.rvisitExpr(ctx.expr(1))
                
                self.visit(ctx.expr(0)) # offset
                self.output += "add $t0, $a0\n"
                self.save_in_stack("$t0")
                self.output += "sw $a0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
                self.rvisitExpr(ctx.expr(0))

                self.load_from_stack("$t0") # offset
                self.load_from_stack("$t1") # new value to add

                # self.output += "sw a0, (-$t0+var_offset)($fp)"
                self.output += "sub $fp, $t0\n"
                self.output += "sw $a0, " +  str(var_offset) + "($fp)\n"
                self.output += inst + " $a0, $t1\n"
                self.output += "sw $a0, " +  str(var_offset) + "($fp)\n"
                self.output += "add $fp, $t0\n"
                self.output += "ta $t0\n"
                self.output += "ta $t1\n"
            else:   # ID OP_INPLACE = expr
                self.visit(ctx.expr(0))
                self.output += "add $t0, $a0\n"
                self.output += "addi $sp, -1\n"
                self.output += "sw $t0, 1($sp)\n"
                self.output += "sw $a0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
                self.rvisitExpr(ctx.expr(0))
                self.output += "sw $t0, 1($sp)\n"
                self.output += "addi $sp, 1\n"
                self.output += "sw $t1, " + str(var_offset) + "($fp)\n"
                self.output += inst + " $t1, $t0\n"
                self.output += "sw $t1, " + str(var_offset) + "($fp)\n"
                self.output += "ta $t0\n"
        else:
            if ctx.OPENSQUARE(): # ID '['expr']' OP_INPLACE expr
                self.visit(ctx.expr(1)) # new value to add
                self.save_in_stack("$a0")
                
                self.visit(ctx.expr(0)) # offset
                # self.save_in_stack("$a0")
                self.output += "swre $a0, $t0\n"
                # self.load_from_stack("$t0") # offset
                self.load_from_stack("$t1") # new value to add

                # self.output += "sw a0, (-$t0+var_offset)($fp)"
                self.output += "sub $fp, $t0\n"
                self.output += "sw $a0, " +  str(var_offset) + "($fp)\n"
                self.output += inst + " $a0, $t1\n"
                self.output += "sw $a0, " +  str(var_offset) + "($fp)\n"
                self.output += "add $fp, $t0\n"
                self.output += "sw $t1, " + str(-ctx.expr(1).placeholder) + "($fp)\n"
                self.rvisitExpr(ctx.expr(1))
                self.output += "sw $t0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
                self.rvisitExpr(ctx.expr(0))
            else: # ID OP_INPLACE expr
                self.visit(ctx.expr(0))
                self.output += "sw $t0, " + str(var_offset) + "($fp)\n"
                self.output += inst + " $t0, $a0\n"
                self.output += "sw $t0, " + str(var_offset) + "($fp)\n"
                self.output += "sw $a0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
                self.rvisitExpr(ctx.expr(0))
        return 0
    
    def visitCondStat(self, ctx: GramParser.CondStatContext):
        self.visit(ctx.expr()) # condition
        self.current_block_id += 1
        if_id = str(self.current_block_id)
        self.blocks_info[if_id] = {} 
        # self.declare("INACCESABLE", "_if_cond"+if_id)
        self.output += f"flif $a0\n"
        self.output += f"caddi $a0, $u, #{if_id}@LENGTH\n"
        self.blocks_info[if_id]["ENTRY_LINE"] = self.output.current_line + 1 
        # self.swap_var_in("$a0", "INACCESABLE", "_if_cond"+if_id)
        self.output += "sw $a0, " + str(-ctx.expr().placeholder) + "($fp)\n"
        self.visit(ctx.body(0))
        # self.swap_var_in("$a0", "INACCESABLE", "_if_cond"+if_id)
        self.output += "sw $a0, " + str(-ctx.expr().placeholder) + "($fp)\n"
        self.blocks_info[if_id]["LENGTH"] = (self.output.current_line + 1) -\
                        self.blocks_info[if_id]["ENTRY_LINE"] 
            
        self.output += f"caddi $a0, $u, -#{if_id}@LENGTH\n"
        self.output += f"flif $a0\n"
        if ctx.ELSE():
            self.current_block_id += 1
            else_id = str(self.current_block_id)
            self.blocks_info[else_id] = {} 
            self.output += f"caddi $a0, $u, #{else_id}@LENGTH\n"
            self.blocks_info[else_id]["ENTRY_LINE"] = self.output.current_line + 1 
            # self.swap_var_in("$a0", "INACCESABLE", "_if_cond"+if_id)
            self.output += "sw $a0, " + str(-ctx.expr().placeholder) + "($fp)\n"
            self.visit(ctx.body(1))
            # self.swap_var_in("$a0", "INACCESABLE", "_if_cond"+str(if_id))            
            self.output += "sw $a0, " + str(-ctx.expr().placeholder) + "($fp)\n"
            self.blocks_info[else_id]["LENGTH"] = (self.output.current_line + 1) -\
                        self.blocks_info[else_id]["ENTRY_LINE"] 
            self.output += f"caddi $a0, $u, -#{else_id}@LENGTH\n"
        self.output += "sw $a0, " + str(-ctx.expr().placeholder) + "($fp)\n"
        if not ctx.CONST():
            not_const_vars = self.idg.get_ids(ctx.expr())
            self.not_const_vars.extend(not_const_vars)
            self.rvisitExpr(ctx.expr())
            self.not_const_vars = [var for var in self.not_const_vars if not (var in not_const_vars)]
        else:
            self.rvisitExpr(ctx.expr())

    def visitDoWhile(self, ctx: GramParser.DoWhileContext):
        self.current_block_id += 1
        loop_block_id = str(self.current_block_id) 
        self.blocks_info[loop_block_id] = {}
        self.declare("INACCESABLE", "oldTur1Save"+loop_block_id)
        self.declare("INACCESABLE", "oldTur2Save"+loop_block_id)
        self.declare("INACCESABLE", "counter"+loop_block_id)
        self.declare("INACCESABLE", "activationTcsu"+loop_block_id)
        self.declare("INACCESABLE", "innerCondition"+loop_block_id)

        self.swap_var_in("$tur1", "INACCESABLE", "oldTur1Save"+loop_block_id) # save the old turs and
        self.swap_var_in("$tur2", "INACCESABLE", "oldTur2Save"+loop_block_id) # load new ones
        # setup
     
        # you don't need to save tur1 or tur2 in the expr, because the only stmt that 
        # uses them is the functionCall that save and restore the old tur

        self.visit(ctx.expr())
        self.output += "addi $tur1, 1\n"
        self.output += f"addi $tur2, -#{loop_block_id}@LENGTH\n"
        self.blocks_info[loop_block_id]["ENTRY_LINE"] = self.output.current_line + 1
        self.output += "tcsu $tur1, $tur2, $t0, $t1\n"
        # tcai
        self.output += "rebi $t2, $t1, 0\n"
        self.output += f"caddi $t2, $tur1, #{loop_block_id}@LENGTH#1\n" # REMEMBER TO ADD THIS TO THE REPLACE LABEL FUNCTION
        self.output += "flif $t2\n"
        self.output += f"caddi $t2, $tur2 #{loop_block_id}@LENGTH#1\n"
        self.output += "flif $t2\n"
        self.output += "rebi $t2, $t1, 0\n"

        # set tur1 = 0
        self.output += "feq $t2, $t1, $zero\n"
        self.output += "caddi $t2, $tur1, -1\n"
        self.output += "feq $t2, $t1, $zero\n"
        
        # caller save
        self.swap_var_in("$tur1", "INACCESABLE", "oldTur1Save"+loop_block_id) 
        self.swap_var_in("$tur2", "INACCESABLE", "oldTur2Save"+loop_block_id)
        self.swap_var_in("$t0", "INACCESABLE", "activationTcsu"+loop_block_id)
        self.swap_var_in("$t1", "INACCESABLE", "counter"+loop_block_id)
        self.swap_var_in("$t2", "INACCESABLE", "innerCondition"+loop_block_id)
        self.output += "sw $a0, " + str(-ctx.expr().placeholder) + "($fp)\n"
        self.rvisitExpr(ctx.expr()) 
        self.visit(ctx.body())
        self.visit(ctx.expr())
        self.swap_var_in("$tur1", "INACCESABLE", "oldTur1Save"+loop_block_id)
        self.swap_var_in("$tur2", "INACCESABLE", "oldTur2Save"+loop_block_id)
        self.swap_var_in("$t0", "INACCESABLE", "activationTcsu"+loop_block_id)
        self.swap_var_in("$t1", "INACCESABLE", "counter"+loop_block_id)
        self.swap_var_in("$t2", "INACCESABLE", "innerCondition"+loop_block_id)

        self.output += "addi $t1, 1\n"
        self.output += f"caddi $a0, $u, -#{loop_block_id}@LENGTH#1\n"
        self.blocks_info[loop_block_id]["LENGTH"] = self.output.current_line -\
                                                    self.blocks_info[loop_block_id]["ENTRY_LINE"]
        self.output += "sw $a0, " + str(-ctx.expr().placeholder) + "($fp)\n"
        self.rvisitExpr(ctx.expr())
        # reversing
        self.output += "rebi $t2, $t1, 0\n"
        self.output += "caddi $t2, $tur2, -1\n"
        self.output += "flif $t2\n"
        self.output += "caddi $t2, $tur1, -1\n"
        self.output += "flif $t2\n"
        self.output += "rebi $t2, $t1, 0\n"
        
        self.output += "flif $t0\n"
        self.swap_var_in("$tur1", "INACCESABLE", "oldTur1Save"+loop_block_id)
        self.swap_var_in("$tur2", "INACCESABLE", "oldTur2Save"+loop_block_id)
        self.deallocate("INACCESABLE", "oldTur1Save"+loop_block_id)
        self.deallocate("INACCESABLE", "oldTur2Save"+loop_block_id)
        self.deallocate("INACCESABLE", "activationTcsu"+loop_block_id)
        self.deallocate("INACCESABLE", "innerCondition"+loop_block_id)
        if ctx.reversingBody():
            self.swap_var_in("$t1", "INACCESABLE", "counter"+loop_block_id)
            if "_counter" in self.enviroment["ACCESABLE"]: 
                save_value = self.enviroment["ACCESABLE"]["_counter"]
                save_size = self.vars_sizes["ACCESABLE"]["_counter"]
            else:
                save_value, save_size = None, None
            self.enviroment["ACCESABLE"]["_counter"] = self.enviroment["INACCESABLE"]["counter"+loop_block_id]
            self.vars_sizes["ACCESABLE"]["_counter"] = self.vars_sizes["INACCESABLE"]["counter"+loop_block_id]
            self.deallocate("INACCESABLE", "counter"+loop_block_id, only_update_env=True)
            self.visit(ctx.reversingBody()) # make counter accesable
            self.deallocate("ACCESABLE", "_counter")
            if save_value is not None:
                self.enviroment["ACCESABLE"]["_counter"] = save_value
                self.vars_sizes["ACCESABLE"]["_counter"] = save_size
        else:
            self.output += "ta $t1\n"
            self.deallocate("INACCESABLE", "counter"+loop_block_id)
        return 0
    
    def visitPrint(self, ctx: GramParser.PrintContext):
        if ctx.expr().getText() == "33":
            self.output += "outr 31\n"
            return
        else:
            self.visit(ctx.expr())
        self.output += "outr $a0\n"
        self.output += "sw $a0, -" + str(ctx.expr().placeholder) + "($fp)\n"
        self.rvisitExpr(ctx.expr())
        return 0

    def visitNum(self, ctx: GramParser.NumContext):
        if ctx.INT():
            self.output += "xorsi $a0, " + ctx.getText() + "\n"
        if ctx.FLOAT():
            Warning("float literal not implemented yet, no code generated")
        return 0
    
    def declare(self, privacy, name, initial_value_in_register = None, size = 1):
        self.vars_sizes[privacy][name] = size
        if initial_value_in_register is not None:
            self.save_in_stack(initial_value_in_register) 
        else: 
            self.output += f"addi $sp, -{size}\n"
        self.fp_offset -= 1
        self.enviroment[privacy][name] = self.fp_offset
        self.fp_offset += -size + 1
        # new_top_privacy, new_top_name = self.get_top_of_the_stack()
        self.top_of_the_stack_privacy = privacy
        self.top_of_the_stack_name = name
        self.top_of_the_stack_value = self.fp_offset

    def deallocate(self, privacy, name, with_ta = False, only_update_env = False):
        if not hasattr(self, "top_of_the_stack_value"):
            privacy, name = self.get_top_of_the_stack()
            if (privacy, name) == (None, None):
                raise NameError(f"while calling deallocate to var {privacy}:{name}, \
                                the stack has been found to be empty")
            self.top_of_the_stack_privacy = privacy
            self.top_of_the_stack_name = name
            self.top_of_the_stack_value = self.enviroment[privacy][name]
            
        if only_update_env: 
            """used in cases where you need 
            delete to the pointer, not the value"""
            del self.enviroment[privacy][name] 
            del self.vars_sizes[privacy][name]
            return 
        
        if with_ta: # if not with_ta the caller garantees that the memory is set to 0
            if only_update_env:
                raise NameError("you can't have with_ta and only_update_env both True")   
            first_offset = self.enviroment[privacy][name]
            last_offset = first_offset - self.vars_sizes[privacy][name] + 1
            while last_offset != (first_offset + 1):
                self.output += f"sw $a0, {last_offset}($fp)\n"
                self.output += "ta $a0\n" 
                last_offset += 1


        # the pointed memory is now made of all 0s
        offset = self.enviroment[privacy][name]
        last_offset = offset - self.vars_sizes[privacy][name] + 1
        del self.enviroment[privacy][name] 
        del self.vars_sizes[privacy][name]
        # this block accounts for holes in the stack, you can make them,
        # and then they will be removed when all the values on top
        # of them are deleted
        if offset ==  self.top_of_the_stack_value: # you were at the top of the stack
            new_top_privacy, new_top_name = self.get_top_of_the_stack()
            self.top_of_the_stack_privacy = new_top_privacy
            self.top_of_the_stack_name = new_top_name
            if new_top_name is not None:
                new_top_value = self.enviroment[new_top_privacy][new_top_name]  
                self.top_of_the_stack_value = new_top_value
                new_last_offset = new_top_value - self.vars_sizes[new_top_privacy][new_top_name] + 1
            else:
                new_top_value = None
                new_last_offset = 0
            self.output += f"addi $sp, {new_last_offset - last_offset}\n"
            self.fp_offset += new_last_offset - last_offset
        return 0

    def get_top_of_the_stack(self):
        env_a = self.enviroment["ACCESABLE"]
        env_ia = self.enviroment["INACCESABLE"]
        combined_env = {**env_a, **env_ia} 
        top_V_ID = min(combined_env, key = combined_env.get) \
                    if len(combined_env) > 0 else None 
        if top_V_ID is None: # only expr are in the stack        
            return (None, None)
        elif combined_env[top_V_ID] > 0: # only expr and aargs are in the stack
            return (None, None)
        elif (top_V_ID in env_ia) and (top_V_ID in env_a):
            if env_a[top_V_ID] < env_ia[top_V_ID]:
                return ("ACCESABLE", top_V_ID)
            else:
                return ("INACCESABLE", top_V_ID)
        elif top_V_ID in env_ia:
            return ("INACCESABLE", top_V_ID)
        elif top_V_ID in env_a:
            return ("ACCESABLE", top_V_ID)

    def set_top_of_the_stack(self):
        privacy, name = self.get_top_of_the_stack()
        self.top_of_the_stack_privacy = privacy
        self.top_of_the_stack_name = name
        self.top_of_the_stack_value = self.enviroment[privacy][name]

    def get_env_copy(self):
        return {"ACCESABLE" : self.enviroment["ACCESABLE"].copy(), 
                "INACCESABLE" : self.enviroment["INACCESABLE"].copy()}
    
    def get_vars_sizes_copy(self):
        return {"ACCESABLE" : self.vars_sizes["ACCESABLE"].copy(), 
                "INACCESABLE" : self.vars_sizes["INACCESABLE"].copy()}

    def swap_var_in(self, register, privacy, name):
        fp_offset = self.enviroment[privacy][name]
        self.output += "sw " + register + ", " +  str(fp_offset) + "($fp)\n"

    def visitTerminal(self, node):
        return 0

    def save_in_stack(self, register):
        self.output += "addi $sp, -1\n"
        self.output += "sw " + register + ", 1($sp)\n"

    def load_from_stack(self, register, update_sp = True):
        self.output += "sw " +  register +  ", 1($sp)\n"
        if update_sp:
            self.output += "addi $sp, 1\n"

    def replace_labels(self):
        for F_ID in self.blocks_info.keys():
            ENTRY_LINE = str(self.blocks_info[F_ID]["ENTRY_LINE"])
            LENGTH = str(self.blocks_info[F_ID]["LENGTH"])
            LENGTH_ = str(self.blocks_info[F_ID]["LENGTH"]+1)
            F_ID = str(F_ID)
            self.output.value = self.output.value.replace("#"+F_ID+"@ENTRY_LINE", ENTRY_LINE)
            self.output.value = self.output.value.replace("#"+F_ID+"@LENGTH#1", LENGTH_)
            self.output.value = self.output.value.replace("#"+F_ID+"@LENGTH", LENGTH)
            while self.output.value.find("#"+F_ID+"@DISTANCE_TO_") != -1:
                i = self.output.value.find("#" + F_ID + "@DISTANCE_TO_")
                i  += len("#" + F_ID + "@DISTANCE_TO_")
                num = ""
                while self.output.value[i] not in ["\t", "\n"]:
                    num += self.output.value[i]
                    i += 1
                LENGTH_TO = str(int(num) - int(ENTRY_LINE) + 1)
                self.output.value = \
                    self.output.value.replace("#"+F_ID+"@DISTANCE_TO_"+num, LENGTH_TO)
