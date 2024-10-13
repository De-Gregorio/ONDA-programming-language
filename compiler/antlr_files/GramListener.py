# Generated from Gram.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramParser import GramParser
else:
    from GramParser import GramParser

# This class defines a complete listener for a parse tree produced by GramParser.
class GramListener(ParseTreeListener):

    # Enter a parse tree produced by GramParser#program.
    def enterProgram(self, ctx:GramParser.ProgramContext):
        pass

    # Exit a parse tree produced by GramParser#program.
    def exitProgram(self, ctx:GramParser.ProgramContext):
        pass


    # Enter a parse tree produced by GramParser#functionDecl.
    def enterFunctionDecl(self, ctx:GramParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by GramParser#functionDecl.
    def exitFunctionDecl(self, ctx:GramParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by GramParser#functionImpl.
    def enterFunctionImpl(self, ctx:GramParser.FunctionImplContext):
        pass

    # Exit a parse tree produced by GramParser#functionImpl.
    def exitFunctionImpl(self, ctx:GramParser.FunctionImplContext):
        pass


    # Enter a parse tree produced by GramParser#functionCall.
    def enterFunctionCall(self, ctx:GramParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by GramParser#functionCall.
    def exitFunctionCall(self, ctx:GramParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by GramParser#fargs.
    def enterFargs(self, ctx:GramParser.FargsContext):
        pass

    # Exit a parse tree produced by GramParser#fargs.
    def exitFargs(self, ctx:GramParser.FargsContext):
        pass


    # Enter a parse tree produced by GramParser#aargs.
    def enterAargs(self, ctx:GramParser.AargsContext):
        pass

    # Exit a parse tree produced by GramParser#aargs.
    def exitAargs(self, ctx:GramParser.AargsContext):
        pass


    # Enter a parse tree produced by GramParser#body.
    def enterBody(self, ctx:GramParser.BodyContext):
        pass

    # Exit a parse tree produced by GramParser#body.
    def exitBody(self, ctx:GramParser.BodyContext):
        pass


    # Enter a parse tree produced by GramParser#stmt.
    def enterStmt(self, ctx:GramParser.StmtContext):
        pass

    # Exit a parse tree produced by GramParser#stmt.
    def exitStmt(self, ctx:GramParser.StmtContext):
        pass


    # Enter a parse tree produced by GramParser#varDecl.
    def enterVarDecl(self, ctx:GramParser.VarDeclContext):
        pass

    # Exit a parse tree produced by GramParser#varDecl.
    def exitVarDecl(self, ctx:GramParser.VarDeclContext):
        pass


    # Enter a parse tree produced by GramParser#assignment.
    def enterAssignment(self, ctx:GramParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GramParser#assignment.
    def exitAssignment(self, ctx:GramParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GramParser#reAssign.
    def enterReAssign(self, ctx:GramParser.ReAssignContext):
        pass

    # Exit a parse tree produced by GramParser#reAssign.
    def exitReAssign(self, ctx:GramParser.ReAssignContext):
        pass


    # Enter a parse tree produced by GramParser#ipAssign.
    def enterIpAssign(self, ctx:GramParser.IpAssignContext):
        pass

    # Exit a parse tree produced by GramParser#ipAssign.
    def exitIpAssign(self, ctx:GramParser.IpAssignContext):
        pass


    # Enter a parse tree produced by GramParser#reAssignS.
    def enterReAssignS(self, ctx:GramParser.ReAssignSContext):
        pass

    # Exit a parse tree produced by GramParser#reAssignS.
    def exitReAssignS(self, ctx:GramParser.ReAssignSContext):
        pass


    # Enter a parse tree produced by GramParser#ipAssignS.
    def enterIpAssignS(self, ctx:GramParser.IpAssignSContext):
        pass

    # Exit a parse tree produced by GramParser#ipAssignS.
    def exitIpAssignS(self, ctx:GramParser.IpAssignSContext):
        pass


    # Enter a parse tree produced by GramParser#condStat.
    def enterCondStat(self, ctx:GramParser.CondStatContext):
        pass

    # Exit a parse tree produced by GramParser#condStat.
    def exitCondStat(self, ctx:GramParser.CondStatContext):
        pass


    # Enter a parse tree produced by GramParser#doWhile.
    def enterDoWhile(self, ctx:GramParser.DoWhileContext):
        pass

    # Exit a parse tree produced by GramParser#doWhile.
    def exitDoWhile(self, ctx:GramParser.DoWhileContext):
        pass


    # Enter a parse tree produced by GramParser#reversingBody.
    def enterReversingBody(self, ctx:GramParser.ReversingBodyContext):
        pass

    # Exit a parse tree produced by GramParser#reversingBody.
    def exitReversingBody(self, ctx:GramParser.ReversingBodyContext):
        pass


    # Enter a parse tree produced by GramParser#returnStmt.
    def enterReturnStmt(self, ctx:GramParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by GramParser#returnStmt.
    def exitReturnStmt(self, ctx:GramParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by GramParser#num.
    def enterNum(self, ctx:GramParser.NumContext):
        pass

    # Exit a parse tree produced by GramParser#num.
    def exitNum(self, ctx:GramParser.NumContext):
        pass


    # Enter a parse tree produced by GramParser#expr.
    def enterExpr(self, ctx:GramParser.ExprContext):
        pass

    # Exit a parse tree produced by GramParser#expr.
    def exitExpr(self, ctx:GramParser.ExprContext):
        pass


    # Enter a parse tree produced by GramParser#print.
    def enterPrint(self, ctx:GramParser.PrintContext):
        pass

    # Exit a parse tree produced by GramParser#print.
    def exitPrint(self, ctx:GramParser.PrintContext):
        pass


    # Enter a parse tree produced by GramParser#swap.
    def enterSwap(self, ctx:GramParser.SwapContext):
        pass

    # Exit a parse tree produced by GramParser#swap.
    def exitSwap(self, ctx:GramParser.SwapContext):
        pass



del GramParser