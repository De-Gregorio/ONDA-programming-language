from builtins import *
from .antlr_files.GramVisitor import GramVisitor
from .antlr_files.GramParser import GramParser 
from antlr4.tree.Tree import TerminalNodeImpl
from .PlaceHolderAssigner import PlaceHolderAssigner
from .SemanticChecker import SemanticChecker
# TO DO 
# ___CLEAN AR
# GET_AARGS & CLEAN_AARGS
#    __ID/num will be passed by copy, and the value in the ar will be thrown away
#    const ID/num will be passed by copy, and the value in the ar will be reversed
#    ID/num& will be passed by swap, the modified value in the ar will be put in the original var
# ___tell the engine the entry point of the program
# ___return a value
# ___assignment
# ifCond
# doWhile
# high level way to access garbage
class IncreadiblyCapableString():
    "this object just count at which line you are at the moment"
    def __init__(self, debug = False):
        self.value = ""
        self.current_line = -1
        self.debug = debug

    def __iadd__(self, stringa):
        if stringa == "eop\n":
            self += "outr 31\n"
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
        

class CodeGenerator(GramVisitor):
    def __init__(self):
        self.sign_to_instruction = {
            "+" : "add",
            "-" : "sub",
            "*" : "mul"
        }
        self.sign_to_rinstruction = {
            "+" : "sub",
            "-" : "add",
            "*" : "mul"
        }

    def generate_code(self, tree):
        self.output = IncreadiblyCapableString(debug=True)
        self.enviroment = {}
        self.vars_sizes = {}
        self.current_block_id = 0
        self.fp_offset = 0 
        self.assigning_variable = {"ID" : None}
        self.parser = tree.parser
        self.pha = PlaceHolderAssigner()
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
        fargs = self.functions_fargs[ctx.ID().getText()]
        old_env = self.enviroment.copy()
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
            self.enviroment[farg["ID"]] = self.fp_offset
            self.vars_sizes[farg["ID"]] = 1 if farg["ARR_SIZE"] == 0 else farg["ARR_SIZE"]
            self.fp_offset -= 1 if farg["ARR_SIZE"] == 0 else farg["ARR_SIZE"]

        self.blocks_info[F_ID] = {}
        self.blocks_info[F_ID]["ENTRY_LINE"] = self.output.current_line + 1
        if ctx.body():
            self.output += "swre $u, $tur\n"
            temporaries_needed = self.pha.visit(ctx.body()) 
            self.blocks_info[F_ID]["TEMPORARIES_NEEDED"] = temporaries_needed
            if temporaries_needed != 0:
                self.output += "addi $sp, -" + str(temporaries_needed) + "\n"
            self.fp_offset = -temporaries_needed
            self.visit(ctx.body())
            self.blocks_info[F_ID]["LENGTH"] = self.output.current_line - self.blocks_info[F_ID]["ENTRY_LINE"] + 1
        else:
            raise NameError("write a body, MOVE")
            # self.output += "nop\n" # WRONG YOU MUST RETURN ANYWAYS  
        
        print(self.fp_offset, self.enviroment, self.current_F_ID)
        self.enviroment = old_env
        self.fp_offset = old_fp_offset 
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
        self.output += "sw $tur, $fp\n"
        self.output += f"addi $tur, #{F_ID}@ENTRY_LINE\n" 
        self.output += f"subi $tur, {self.output.current_line + 2}\n" 
        self.output += f"swre $tur, $u\n" # actual jump (that line is the c_pc)
        # tur -= c_pc - f_pc - fun_len + 1
        self.output += f"subi $tur, {self.output.current_line+1}\n" # - fp_pc - fun_len 
        self.output += f"addi $tur, #{F_ID}@ENTRY_LINE\n"           # - fun_len 
        self.output += f"addi $tur, #{F_ID}@LENGTH\n"               # 0
        self.output += "sw $tur, $fp\n"
        # CLEAN AR
        self.output += "addi $sp, 1\n"
        self.output += "sub $fp, $sp\n"
        self.output += "sw $fp, " + str(fargs_size + 1) + "($sp)\n" # reload old fp
        self.output += "addi $sp, " + str(fargs_size + 1) + "\n"
        self.clean_aargs(ctx)
        # SET THE RA IN THE SPOT POINTED BY THE FP
        return 0
    
    def visitReturnStmt(self, ctx: GramParser.ReturnStmtContext):
        # tur = f_pc - c_pc

        # tur *= -1            = c_pc - f_pc
        # tur -= fun_len       = c_pc - fp_pc - fun_len
        # tur += 1             = c_pc - fp_pc - fun_len + 1
        # swap ur tur          (fp_pc + fun_len) + c_pc - fp_c - fun_len  = c_pc + 1
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
        temporaries_needed = self.blocks_info[self.current_F_ID]["TEMPORARIES_NEEDED"]
        if temporaries_needed != 0:
            self.output += "addi $sp, " + str(temporaries_needed) + "\n"
        if self.current_F_ID == "main":
            self.output += "eop\n"
            return 0
        self.output += "neg $tur\n"
        self.output += f"subi $tur, #{self.current_F_ID}@LENGTH\n"
        self.output += "addi $tur, 1\n"
        self.output += "swre $u, $tur\n"
        self.output += f"# end return of {self.current_F_ID}\n"
        return 0
 
    def clean_local_vars(self):
        locals_vars = [V_ID for V_ID in self.enviroment.keys() if self.enviroment[V_ID] < 0]
        if len(locals_vars) == 0:
            return 
        first_var = locals_vars[0]
        last_var = locals_vars[-1]
        last_offset=  self.enviroment[last_var] - self.vars_sizes[last_var] + 1
        first_offset = self.enviroment[first_var]
        self.output += "addi $sp, " + str(first_offset-last_offset + 1) + "\n"
        while last_offset != (first_offset + 1):
            self.output += "sw $a0, " + str(last_offset) + "($fp)\n"
            self.output += "ta $a0\n"
            last_offset += 1

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
            fp_offset = self.enviroment[ctx.ID().getText()]
            self.output += "sw $t1, " + fp_offset + "($fp)\n"
            self.output += "add $a0, $t1"
            self.output += "sw $a0, " + sp_offset + "($sp)\n" 
            self.output += "sw $t1, " + fp_offset + "($fp)\n"
            sp_offset -= 1
            if farg["ARR_SIZE"] != 0:
                for i in range(1, farg["ARR_SIZE"]):
                    fp_offset -= 1
                    self.output += "sw $t1, " + fp_offset + "($fp)\n"
                    self.output += "add $a0, $t1"
                    self.output += "sw $a0, " + sp_offset + "($sp)\n" 
                    self.output += "sw $t1, " + fp_offset + "($fp)\n"
                    sp_offset -= 1
        elif ctx.num():
            self.visit(ctx.num()) # not really a copy but it's ok
            self.output += "sw $a0, " + str(sp_offset) + "($sp)\n" 
            sp_offset -= 1
        elif ctx.expr():
            self.visit(ctx.expr())
            self.output += "add $t1, $a0\n"
            self.output += "sw $t1, " + sp_offset + "($sp)\n" 
            self.output += "sw $a0, -" + str(ctx.expr().placeholder) + "($fp)\n"
            self.rvisitExpr(ctx.expr())
            sp_offset -= 1 
        return sp_offset
    
    def clean_aargs(self, ctx: GramParser.FunctionCallContext):
        fargs = self.functions_fargs[ctx.ID().getText()]
        ctx = ctx.aargs()
        sp_offset = -1
        for farg in fargs:
            farg = fargs
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
        old_env = self.enviroment.copy()
        self.visitChildren(ctx)
        self.enviroment = old_env
        return 0
    
    def visitStmt(self, ctx: GramParser.StmtContext):
        return super().visitStmt(ctx)

    def visitVarDecl(self, ctx:GramParser.VarDeclContext):
        ID = ctx.ID().getText()
        self.vars_sizes[ID] = 1
        if ID in self.enviroment.keys(): # to remove since MemoryCalculator already does this check
            raise NameError(f"redeclaration of {ID} isn't allowed") 
        if ctx.getChildCount() == 2: # TYPE ID
            self.output += "addi $sp, -1\n"
            self.fp_offset -= 1
            self.enviroment[ID] = self.fp_offset
        elif ctx.EQUAL_SIGN(): # TYPE ID = expr
            self.output += "addi $sp, -1\n"
            self.fp_offset -= 1
            self.enviroment[ID] = self.fp_offset
            self.visit(ctx.expr())
            self.output += "add $t1, $a0\n" # copy a0 in t1
            self.output += "sw $t1, 1($sp)\n" # save the value in the ID var
            offset_temp = ctx.expr().placeholder
            self.output += "sw $a0, -" + str(offset_temp) + "($fp)\n"
            self.rvisitExpr(ctx.expr())
        elif ctx.OPENSQUARE(): # TYPE ID '['INT']' 
            arr_size = int(ctx.INT().getText())
            self.vars_sizes[ID] = arr_size
            self.output += "addi $sp, -" + str(arr_size) + "\n"   
            self.fp_offset -= 1
            self.enviroment[ID] = self.fp_offset
            self.fp_offset -= (arr_size - 1) 
        else:
            Warning("uknown declaration: ", ctx.getText())

    def visitExpr(self, ctx:GramParser.ExprContext):
        """
        CHANGE THIS COMMENT!!!!
        in the forward pass, every (new) temporary is put in his placeholder except for
        the last result, that will be put in $a0
        """
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
        if ctx.OP_MULTIPLICATIVE(): # expr OP_MULTIPLICATIVE expr
            op = ctx.OP_MULTIPLICATIVE().getText()
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
        if ctx.num(): # num
            self.visit(ctx.num())
            return 0
        if ctx.ID() and (not ctx.OPENSQUARE()): # ID
            fp_offset = self.enviroment[ctx.ID().getText()]
            self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
            self.output += "add $a0, $t1\n"
            self.output += "sw $t1, " + str(fp_offset) + "($fp)\n"
        if ctx.functionCall(): # functionCall
            self.output += "# start functionCall\n"
            self.visit(ctx.functionCall())
            self.output += "swre $a0, $v0\n"
            self.output += "# end functionCall\n"
        if ctx.OPENSQUARE(): # ID '[' expr ']'
            var_offset = self.enviroment[ctx.ID().getText()]
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
        if ctx.getChildCount() == 4: # case ID '[' expr ']'
            offset = self.get_ID_offset(ctx.getChild(0))
            self.output += "li $a0, " + str(offset) + "\n"
            self.output += "addiu $sp, $sp, -4\n"
            self.output += "sw $a0, 4($sp)\n"
            self.visit(ctx.getChild(2))
            self.output += "lw $t1, 4($sp)\n"
            self.output += "addiu $t2, t1, $a0\n"
            self.output += "lw $a0, ($t2)($fp)\n"
            self.output += "addiu $sp, $sp, 4\n"
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == "(": # case '(' expr ')'
                self.visit(ctx.getChild(1))
                return 0
        elif ctx.getChildCount() == 1: # case NUM / ID
            if type(ctx.getChild(0)) == TerminalNodeImpl: # ID
                self.get_ID_value(ctx.getChild(0))
            else: # NUM
                self.visit(ctx.getChild(0))

        return 0

    def rvisitExpr(self, ctx:GramParser.ExprContext):
        """
        CHANGE THIS COMMENT!!!!
        in the reverse pass, every temporary is in his placeholder at the 
        start and at the end
        """
        if ctx.OP_ADDITIVE(): # expr OP_ADDITIVE expr
            op = ctx.OP_ADDITIVE().getText()
            inst = self.sign_to_rinstruction[op]
            expr1, expr2 = ctx.expr()
            offset1 = -expr1.placeholder
            offset2 = -expr2.placeholder
            self.output += "sw $t1, " + str(offset1) + "($fp)\n"
            self.output += "sw $t2, " + str(offset2) + "($fp)\n"
            self.output += inst + " $t1, $t2\n"
            self.output += "sw $t2, " + str(offset2) + "($fp)\n"
            self.output += "sw $t1, " + str(offset1) + "($fp)\n"
            self.rvisitExpr(expr1)
            self.rvisitExpr(expr2)
        if ctx.OP_MULTIPLICATIVE(): # expr OP_MULTIPLICAIVE expr
            op = ctx.OP_MULTIPLICATIVE().getText()
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
            if self.assigning_variable["ID"] == ctx.ID().getText():
                expr_offset = -ctx.placeholder
                self.output += "sw $a0, " + str(expr_offset) + "($fp)\n"    
                self.output += "ta $a0\n"
                pass
            fp_offset = self.enviroment[ctx.ID().getText()]
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
        if ctx.functionCall(): # functionCall
            pass
        if ctx.OPENSQUARE(): # ID '[' expr ']'
            var_offset = self.enviroment[ctx.ID().getText()]
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
        var_offset = self.enviroment[V_ID]
        self.assigning_variable["ID"] = V_ID
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
        self.assigning_variable["ID"] = None
        return 0

    def visitIpAssign(self, ctx: GramParser.IpAssignContext):
        op = ctx.OP_INPLACE().getText()[0]
        inst = self.sign_to_instruction[op] 
        var_offset = self.enviroment[ctx.ID().getText()]

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

    def visitCond(self, ctx: GramParser.CondContext):
        if len(ctx.expr()) == 2: # expr == expr
            self.visit(ctx.expr(0))
            self.output += "sw $a0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
            self.visit(ctx.expr(1))            
            self.output += "swre $t1, $a0\n"
            self.output += "sw $t0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
            self.output += "feq $a0, $t0, $t1\n"
            self.output += "sw $t0, " + str(-ctx.expr(0).placeholder) + "($fp)\n"
            self.output += "sw $t1, " + str(-ctx.expr(1).placeholder) + "($fp)\n"
            self.rvisitExpr(ctx.expr(0))
            self.rvisitExpr(ctx.expr(1))
        else: # expr 
            self.visit(ctx.expr(0))
        return 0
    
    def visitCondStat(self, ctx: GramParser.CondStatContext):
        self.visit(ctx.cond())
        self.current_block_id += 1
        self.blocks_info[self.current_block_id] = {} 
        self.output += f"caddi $a0, $u, #{self.current_block_id}@LENGTH\n"
        self.blocks_info[self.current_block_id]["ENTRY_LINE"] = self.output.current_line + 1 
        self.save_in_stack("$a0") 
        self.visit(ctx.body(0))
        self.load_from_stack("$a0")
        self.blocks_info[self.current_block_id]["LENGTH"] = (self.output.current_line + 1) -\
                        self.blocks_info[self.current_block_id]["ENTRY_LINE"] 
            
        self.output += f"caddi $a0, $u, -#{self.current_block_id}@LENGTH\n"
        if ctx.ELSE():
            self.current_block_id += 1
            self.blocks_info[self.current_block_id] = {} 
            self.output += f"caddi $a0, $u, #{self.current_block_id}@LENGTH\n"
            self.blocks_info[self.current_block_id]["ENTRY_LINE"] = self.output.current_line + 1 
            self.save_in_stack("$a0") 
            self.visit(ctx.body(1))
            self.load_from_stack("$a0")
            self.blocks_info[self.current_block_id]["LENGTH"] = (self.output.current_line + 1) -\
                        self.blocks_info[self.current_block_id]["ENTRY_LINE"] 
            self.output += f"caddi $a0, $u, -#{self.current_block_id}@LENGTH\n"
        self.output += "ta $a0\n"

    def visitPrint(self, ctx: GramParser.PrintContext):
        self.visit(ctx.expr())
        self.output += "outr $a0\n"
        self.output += "sw $a0, -" + str(ctx.expr().placeholder) + "($fp)\n"
        self.rvisitExpr(ctx.expr())
        return 0

    def visitNum(self, ctx: GramParser.NumContext):
        if ctx.INT():
            self.output += "xori $a0, " + ctx.getText() + "\n"
        if ctx.FLOAT():
            Warning("float literal not implemented yet, no code generated")
        return 0
    
    def visitTerminal(self, node):
        return 0
        symbol = node.getSymbol()
        if symbol.type == self.parser.INT: #or symbol.type == self.parser.FLOAT: float not supported yet
            self.output += "li $a0, " + symbol.text + "\n"
        # elif symbol.type == self.parser.ID:
        #     if not (symbol.text in self.enviroment.keys()): # to remove since MemoryCalculator already does this check
        #         raise NameError(f"use of {symbol.text} before declaration") 
            
        else:
            print(symbol.text, "encountered, didn't produce any instrucion")
        return 

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
            F_ID = str(F_ID)
            self.output.value = self.output.value.replace("#"+F_ID+"@ENTRY_LINE", ENTRY_LINE)
            self.output.value = self.output.value.replace("#"+F_ID+"@LENGTH", LENGTH)
