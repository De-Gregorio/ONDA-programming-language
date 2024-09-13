from builtins import *
from antlr_files.GramVisitor import GramVisitor
from antlr_files.GramParser import GramParser 
from antlr4.tree.Tree import TerminalNodeImpl

class PlaceHolderInitializer(GramVisitor):
    def visitExpr(self, ctx:GramParser.ExprContext):
        ctx.placeholder = None
        self.visitChildren(ctx)
        return 0
    
class PlaceHolderAssigner(GramVisitor):
    def visitFunctionImpl(self, ctx: GramParser.FunctionImplContext):
        return super().visitFunctionImpl(ctx)
    
    def visitBody(self, ctx: GramParser.BodyContext):
        initializer = PlaceHolderInitializer()
        initializer.visit(ctx)
        del initializer
        self.last_placeholder_assigned = 0
        self.max_placeholder = 0
        self.visitChildren(ctx)
        return self.max_placeholder

    def visitStmt(self, ctx: GramParser.StmtContext):
        save = self.last_placeholder_assigned
        self.visitChildren(ctx)
        self.max_placeholder = max(self.max_placeholder, self.last_placeholder_assigned)
        self.last_placeholder_assigned = save
        return 0

    def visitExpr(self, ctx: GramParser.ExprContext):
        if ctx.placeholder is None:
            ctx.placeholder = self.last_placeholder_assigned + 1
            self.last_placeholder_assigned += 1 
        if ctx.OP_ADDITIVE(): # expr OPERATOR expr
            expr1, expr2 = ctx.expr()
            expr1.placeholder = ctx.placeholder
        if ctx.num(): # num
            pass
        if ctx.ID() and (not ctx.OPENSQUARE()): # ID
            pass
        if ctx.functionCall(): # functionCall
            pass
        if ctx.OPENSQUARE(): # ID '[' expr ']'
            pass
        if ctx.OPENPAREN(): # '(' expr ')'
            expr = ctx.expr()[0]
            expr.placeholder = ctx.placeholder
        self.visitChildren(ctx)
        return 0