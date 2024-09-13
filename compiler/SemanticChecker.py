from builtins import *
from .antlr_files.GramVisitor import GramVisitor 
from .antlr_files.GramParser import GramParser 
from antlr4.tree.Tree import TerminalNodeImpl

# !!!!!!THAT SHIT DOESN'T WORK, FIX IT BEFORE USING IT!!!!!!!!! 


class SemanticChecker(GramVisitor):
    
    def check_errors(self, tree):
        self.parser = tree.parser
        self.declared_functions = {}
        self.initizialed_variables = []
        self.assigning_variable  = None
        self.visit(tree)
        error_message = ""
        for F_ID in self.declared_functions.keys():
            if not self.declared_functions[F_ID]["implemented"]:
                error_message += f"{F_ID} was never implemented\n"
        if error_message != "":
            raise NameError(error_message)
        return {F_ID : self.declared_functions[F_ID]["fargs"] for F_ID in self.declared_functions.keys()}


    def get_fargs(self, ctx, F_ID):
        #ctx : FunctionDeclContext | FunctionImplContext
        #F_ID: Function_ID, passed for error handling purposes
        if not ctx.fargs():
            return []
        ctx = ctx.fargs()
        formal_arguments = []
        while ctx:
            arr_size = 0
            tipo = ctx.TYPE().getText()
            V_ID = ctx.ID().getText()
            if ctx.INT(): # TYPE ID[INT]
                arr_size = int(ctx.INT().getText())    
            if any(var['ID'] == V_ID for var in formal_arguments):
                raise NameError(f"{V_ID} is declared more than once in function {F_ID}")
            formal_arguments.append({
                "ID" : V_ID,
                "TYPE" : tipo,
                "ARR_SIZE" : arr_size
            })

            ctx = ctx.fargs()
            # if ctx.fargs():
            #     ctx = ctx.fargs()
            #     continue
            # else:
            #     break
        return formal_arguments.copy()
        
    
    def get_aargs(self, ctx:GramParser.FunctionCallContext):
        if not ctx.aargs():
            return []
        ctx = ctx.aargs()
        actual_arguments = []
        while ctx:
            if ctx.ID():
                var = self.get_var(ctx.ID().getText())
                a_type = var["TYPE"]
                arr_size = var["ARR_SIZE"]
            elif ctx.expr():
                a_type = self.get_expr_type(ctx.expr())
                arr_size = 0
            elif ctx.num():
                a_type = self.get_num_type(ctx.num())
                arr_size = 0
            else:
                raise EOFError("What is happening ?")
            
            
            actual_arguments.append({
                "TYPE" : a_type,
                "ARR_SIZE" : arr_size
            })
            ctx = ctx.aargs()
    
        return actual_arguments.copy()
    
    def get_var(self, ID: str):
        for var in self.initizialed_variables:
            if var['ID'] == ID:
                return var
        raise NameError(f"used unknown var {ID}")

    def get_expr_type(self, expr: GramParser.ExprContext):
        return "int" # to implement
    
    def get_num_type(self, num: GramParser.NumContext):
        if num.INT():
            return "int"
        elif num.FLOAT():
            return "float"
        else:
            raise NotADirectoryError("Interesting error")

    
    def visitFunctionDecl(self, ctx: GramParser.FunctionDeclContext):
        F_ID = ctx.ID().getText()
        if F_ID in self.declared_functions.keys():
            raise NameError(f"can't redeclare function {F_ID}")
        formal_arguments = self.get_fargs(ctx, F_ID)
        self.declared_functions[F_ID] = {}
        self.declared_functions[F_ID]["fargs"] = formal_arguments.copy()
        self.declared_functions[F_ID]["implemented"] = False
        return 0

    def visitFunctionImpl(self, ctx: GramParser.FunctionImplContext):
        F_ID = ctx.ID().getText()
        formal_args = self.get_fargs(ctx, F_ID)
        if F_ID in self.declared_functions.keys():
            saved_args = self.declared_functions[F_ID]["fargs"]
            if formal_args != saved_args:
                raise NameError(f"Arguments of function {F_ID} don't match between declaration and implemenation") 
        else:
            self.declared_functions[F_ID] = {}
        self.initizialed_variables = formal_args.copy()
        self.declared_functions[F_ID]["fargs"] = formal_args.copy()
        self.declared_functions[F_ID]["implemented"] = True
        if ctx.body():
            self.visit(ctx.body())
        return 0 

    def visitFunctionCall(self, ctx: GramParser.FunctionCallContext):
        F_ID = ctx.ID().getText()
        if not F_ID in self.declared_functions.keys():
            raise NameError(f"called unknown function {F_ID}")
        aargs = self.get_aargs(ctx)
        fargs = self.declared_functions[F_ID]["fargs"]
        if len(aargs) != len(fargs):
            raise NameError(f"{F_ID} expcted {len(fargs)} arguments, {len(aargs)} given instead") 
        counter = 1
        for aarg, farg in zip(aargs, fargs):
            if aarg["TYPE"] != farg["TYPE"]:
                raise NameError(f"var n{counter} has type {aarg['TYPE']}, was expected: {farg['TYPE']}")
            if aarg["ARR_SIZE"] != farg["ARR_SIZE"]:
                if aarg["ARR_SIZE"] == 0:
                    raise NameError(f"var n{counter} is an {aarg['TYPE']}, but was expected {farg['TYPE']}[{farg['ARR_SIZE']}] instead")
                elif farg["ARR_SIZE"] == 0:
                    raise NameError(f"var n{counter} is {aarg['TYPE']}[{aarg['ARR_SIZE']}], but was expected {farg['TYPE']} instead")
                else:
                    raise NameError(f"var n{counter} is {aarg['TYPE']}[{aarg['ARR_SIZE']}], but was expected {farg['TYPE']}[{farg['ARR_SIZE']}] instead") 
            counter += 1

        return 0
    
    def visitVarDecl(self, ctx: GramParser.VarDeclContext):
        # self.initizialed_variables += [ID]
        ID = ctx.ID().getText()
        arr_size = 0
        tipo = ctx.TYPE().getText()
        if ctx.getChildCount() == 2: # TYPE ID;
            pass
        elif ctx.EQUAL_SIGN(): # TYPE ID = expr
            self.visit(ctx.expr())
            pass # you need to implement expr type checking
        elif ctx.OPENSQUARE(): # TYPE ID '['INT']' 
            arr_size = int(ctx.INT().getText())
            if arr_size <= 0:
                raise ValueError(f"in decl of {ID}: arr {ID} can't have a size of {arr_size} ")
        else:
            Warning("uknown declaration: ", ctx.getText())
        if any(var['ID'] == ID for var in self.initizialed_variables):
            raise NameError(f"redeclaration of var {ID}")
        self.initizialed_variables.append({
            "ID" : ID,
            "TYPE" : tipo,
            "ARR_SIZE" : arr_size
        })
        return 0
    
    def visitExpr(self, ctx: GramParser.ExprContext):
        if ctx.ID():
            ID = ctx.ID().getText()
            if not  any(var['ID'] == ID for var in self.initizialed_variables):
                raise NameError(f"using var {ID} before declaration") 
            if ID == self.assigning_variable:
                self.ip_assign_to_replace = True
        self.visitChildren(ctx)
        return 0
    
    def visitIpAssign(self, ctx: GramParser.IpAssignContext):

        self.assigning_variable = ctx.ID().getText()
        self.ip_assign_to_replace = False
        if ctx.OPENSQUARE():
            self.visit(ctx.expr(1))
        else:
            self.visit(ctx.expr(0))
        if self.ip_assign_to_replace:
            ctx.to_substitute = True
        else:
            ctx.to_substitute = False
    def visitTerminal(self, node):
        if node.getSymbol().type == self.parser.ID:
            if not any(var['ID'] == node.getText() for var in self.initizialed_variables):
                raise NameError(f"{node.getText()} used before declaratrion")
            

        
