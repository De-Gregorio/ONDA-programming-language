# Generated from Gram.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramParser import GramParser
else:
    from GramParser import GramParser

# This class defines a complete generic visitor for a parse tree produced by GramParser.

class GramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramParser#program.
    def visitProgram(self, ctx:GramParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#functionDecl.
    def visitFunctionDecl(self, ctx:GramParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#functionImpl.
    def visitFunctionImpl(self, ctx:GramParser.FunctionImplContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#functionCall.
    def visitFunctionCall(self, ctx:GramParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#fargs.
    def visitFargs(self, ctx:GramParser.FargsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#aargs.
    def visitAargs(self, ctx:GramParser.AargsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#body.
    def visitBody(self, ctx:GramParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt.
    def visitStmt(self, ctx:GramParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#varDecl.
    def visitVarDecl(self, ctx:GramParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#assignment.
    def visitAssignment(self, ctx:GramParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#reAssign.
    def visitReAssign(self, ctx:GramParser.ReAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#ipAssign.
    def visitIpAssign(self, ctx:GramParser.IpAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#reAssignS.
    def visitReAssignS(self, ctx:GramParser.ReAssignSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#ipAssignS.
    def visitIpAssignS(self, ctx:GramParser.IpAssignSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#condStat.
    def visitCondStat(self, ctx:GramParser.CondStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#doWhile.
    def visitDoWhile(self, ctx:GramParser.DoWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#reversingBody.
    def visitReversingBody(self, ctx:GramParser.ReversingBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#returnStmt.
    def visitReturnStmt(self, ctx:GramParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#num.
    def visitNum(self, ctx:GramParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#special_ID.
    def visitSpecial_ID(self, ctx:GramParser.Special_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#expr.
    def visitExpr(self, ctx:GramParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#print.
    def visitPrint(self, ctx:GramParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#swap.
    def visitSwap(self, ctx:GramParser.SwapContext):
        return self.visitChildren(ctx)



del GramParser