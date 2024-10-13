# Generated from Gram.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,315,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,4,0,47,8,0,11,0,12,0,48,1,0,1,0,1,1,1,1,1,
        1,1,1,3,1,57,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,1,1,1,3,1,
        69,8,1,1,2,1,2,1,2,1,2,3,2,75,8,2,1,2,1,2,1,2,3,2,80,8,2,1,2,1,2,
        1,2,1,2,1,2,3,2,87,8,2,1,2,1,2,1,2,3,2,92,8,2,1,2,3,2,95,8,2,1,3,
        1,3,1,3,3,3,100,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,109,8,4,1,4,
        1,4,1,4,3,4,114,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,123,8,4,3,4,
        125,8,4,1,5,1,5,1,5,3,5,130,8,5,1,5,1,5,1,5,3,5,135,8,5,1,5,1,5,
        1,5,3,5,140,8,5,3,5,142,8,5,1,6,5,6,145,8,6,10,6,12,6,148,9,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,172,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,3,8,185,8,8,1,9,1,9,1,9,1,9,3,9,191,8,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,203,8,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,215,8,11,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,3,14,228,8,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,239,8,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,251,8,14,1,15,1,15,
        1,15,1,15,1,15,3,15,258,8,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,17,1,17,3,17,271,8,17,1,18,1,18,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,
        291,8,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,302,8,
        19,10,19,12,19,305,9,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,
        1,21,0,1,38,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,0,2,1,0,28,29,2,0,24,24,30,30,342,0,46,1,0,0,0,2,68,
        1,0,0,0,4,94,1,0,0,0,6,96,1,0,0,0,8,124,1,0,0,0,10,141,1,0,0,0,12,
        146,1,0,0,0,14,171,1,0,0,0,16,184,1,0,0,0,18,190,1,0,0,0,20,202,
        1,0,0,0,22,214,1,0,0,0,24,216,1,0,0,0,26,220,1,0,0,0,28,250,1,0,
        0,0,30,252,1,0,0,0,32,264,1,0,0,0,34,268,1,0,0,0,36,272,1,0,0,0,
        38,290,1,0,0,0,40,306,1,0,0,0,42,309,1,0,0,0,44,47,3,2,1,0,45,47,
        3,4,2,0,46,44,1,0,0,0,46,45,1,0,0,0,47,48,1,0,0,0,48,46,1,0,0,0,
        48,49,1,0,0,0,49,50,1,0,0,0,50,51,5,0,0,1,51,1,1,0,0,0,52,53,5,2,
        0,0,53,54,5,30,0,0,54,56,5,15,0,0,55,57,3,8,4,0,56,55,1,0,0,0,56,
        57,1,0,0,0,57,58,1,0,0,0,58,59,5,16,0,0,59,69,5,4,0,0,60,61,5,3,
        0,0,61,62,5,30,0,0,62,64,5,15,0,0,63,65,3,8,4,0,64,63,1,0,0,0,64,
        65,1,0,0,0,65,66,1,0,0,0,66,67,5,16,0,0,67,69,5,4,0,0,68,52,1,0,
        0,0,68,60,1,0,0,0,69,3,1,0,0,0,70,71,5,2,0,0,71,72,5,30,0,0,72,74,
        5,15,0,0,73,75,3,8,4,0,74,73,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,
        76,77,5,16,0,0,77,79,5,19,0,0,78,80,3,12,6,0,79,78,1,0,0,0,79,80,
        1,0,0,0,80,81,1,0,0,0,81,95,5,20,0,0,82,83,5,3,0,0,83,84,5,30,0,
        0,84,86,5,15,0,0,85,87,3,8,4,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,
        1,0,0,0,88,89,5,16,0,0,89,91,5,19,0,0,90,92,3,12,6,0,91,90,1,0,0,
        0,91,92,1,0,0,0,92,93,1,0,0,0,93,95,5,20,0,0,94,70,1,0,0,0,94,82,
        1,0,0,0,95,5,1,0,0,0,96,97,5,30,0,0,97,99,5,15,0,0,98,100,3,10,5,
        0,99,98,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,102,5,16,0,0,
        102,7,1,0,0,0,103,104,5,25,0,0,104,109,5,2,0,0,105,106,5,2,0,0,106,
        109,5,22,0,0,107,109,5,2,0,0,108,103,1,0,0,0,108,105,1,0,0,0,108,
        107,1,0,0,0,109,110,1,0,0,0,110,113,5,30,0,0,111,112,5,21,0,0,112,
        114,3,8,4,0,113,111,1,0,0,0,113,114,1,0,0,0,114,125,1,0,0,0,115,
        116,5,2,0,0,116,117,5,30,0,0,117,118,5,17,0,0,118,119,5,28,0,0,119,
        122,5,18,0,0,120,121,5,21,0,0,121,123,3,8,4,0,122,120,1,0,0,0,122,
        123,1,0,0,0,123,125,1,0,0,0,124,108,1,0,0,0,124,115,1,0,0,0,125,
        9,1,0,0,0,126,129,5,30,0,0,127,128,5,21,0,0,128,130,3,10,5,0,129,
        127,1,0,0,0,129,130,1,0,0,0,130,142,1,0,0,0,131,134,3,36,18,0,132,
        133,5,21,0,0,133,135,3,10,5,0,134,132,1,0,0,0,134,135,1,0,0,0,135,
        142,1,0,0,0,136,139,3,38,19,0,137,138,5,21,0,0,138,140,3,10,5,0,
        139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,126,1,0,0,0,
        141,131,1,0,0,0,141,136,1,0,0,0,142,11,1,0,0,0,143,145,3,14,7,0,
        144,143,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,
        147,13,1,0,0,0,148,146,1,0,0,0,149,150,3,38,19,0,150,151,5,4,0,0,
        151,172,1,0,0,0,152,153,3,16,8,0,153,154,5,4,0,0,154,172,1,0,0,0,
        155,156,3,18,9,0,156,157,5,4,0,0,157,172,1,0,0,0,158,172,3,28,14,
        0,159,160,3,30,15,0,160,161,5,4,0,0,161,172,1,0,0,0,162,163,3,34,
        17,0,163,164,5,4,0,0,164,172,1,0,0,0,165,166,3,42,21,0,166,167,5,
        4,0,0,167,172,1,0,0,0,168,169,3,40,20,0,169,170,5,4,0,0,170,172,
        1,0,0,0,171,149,1,0,0,0,171,152,1,0,0,0,171,155,1,0,0,0,171,158,
        1,0,0,0,171,159,1,0,0,0,171,162,1,0,0,0,171,165,1,0,0,0,171,168,
        1,0,0,0,172,15,1,0,0,0,173,174,5,2,0,0,174,185,5,30,0,0,175,176,
        5,2,0,0,176,177,5,30,0,0,177,178,5,1,0,0,178,185,3,38,19,0,179,180,
        5,2,0,0,180,181,5,30,0,0,181,182,5,17,0,0,182,183,5,28,0,0,183,185,
        5,18,0,0,184,173,1,0,0,0,184,175,1,0,0,0,184,179,1,0,0,0,185,17,
        1,0,0,0,186,191,3,22,11,0,187,191,3,20,10,0,188,191,3,26,13,0,189,
        191,3,24,12,0,190,186,1,0,0,0,190,187,1,0,0,0,190,188,1,0,0,0,190,
        189,1,0,0,0,191,19,1,0,0,0,192,193,5,30,0,0,193,194,5,1,0,0,194,
        203,3,38,19,0,195,196,5,30,0,0,196,197,5,17,0,0,197,198,3,38,19,
        0,198,199,5,18,0,0,199,200,5,1,0,0,200,201,3,38,19,0,201,203,1,0,
        0,0,202,192,1,0,0,0,202,195,1,0,0,0,203,21,1,0,0,0,204,205,5,30,
        0,0,205,206,5,8,0,0,206,215,3,38,19,0,207,208,5,30,0,0,208,209,5,
        17,0,0,209,210,3,38,19,0,210,211,5,18,0,0,211,212,5,8,0,0,212,213,
        3,38,19,0,213,215,1,0,0,0,214,204,1,0,0,0,214,207,1,0,0,0,215,23,
        1,0,0,0,216,217,5,24,0,0,217,218,5,1,0,0,218,219,3,38,19,0,219,25,
        1,0,0,0,220,221,5,24,0,0,221,222,5,8,0,0,222,223,3,38,19,0,223,27,
        1,0,0,0,224,225,5,10,0,0,225,227,5,15,0,0,226,228,5,25,0,0,227,226,
        1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,230,3,38,19,0,230,231,
        5,16,0,0,231,232,5,19,0,0,232,233,3,12,6,0,233,234,5,20,0,0,234,
        251,1,0,0,0,235,236,5,10,0,0,236,238,5,15,0,0,237,239,5,25,0,0,238,
        237,1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,241,3,38,19,0,241,
        242,5,16,0,0,242,243,5,19,0,0,243,244,3,12,6,0,244,245,5,20,0,0,
        245,246,5,11,0,0,246,247,5,19,0,0,247,248,3,12,6,0,248,249,5,20,
        0,0,249,251,1,0,0,0,250,224,1,0,0,0,250,235,1,0,0,0,251,29,1,0,0,
        0,252,253,5,12,0,0,253,254,5,19,0,0,254,255,3,12,6,0,255,257,5,20,
        0,0,256,258,3,32,16,0,257,256,1,0,0,0,257,258,1,0,0,0,258,259,1,
        0,0,0,259,260,5,13,0,0,260,261,5,15,0,0,261,262,3,38,19,0,262,263,
        5,16,0,0,263,31,1,0,0,0,264,265,5,19,0,0,265,266,3,12,6,0,266,267,
        5,20,0,0,267,33,1,0,0,0,268,270,5,14,0,0,269,271,3,38,19,0,270,269,
        1,0,0,0,270,271,1,0,0,0,271,35,1,0,0,0,272,273,7,0,0,0,273,37,1,
        0,0,0,274,275,6,19,-1,0,275,276,5,5,0,0,276,291,3,38,19,7,277,291,
        3,36,18,0,278,291,5,30,0,0,279,291,5,24,0,0,280,291,3,6,3,0,281,
        282,5,30,0,0,282,283,5,17,0,0,283,284,3,38,19,0,284,285,5,18,0,0,
        285,291,1,0,0,0,286,287,5,15,0,0,287,288,3,38,19,0,288,289,5,16,
        0,0,289,291,1,0,0,0,290,274,1,0,0,0,290,277,1,0,0,0,290,278,1,0,
        0,0,290,279,1,0,0,0,290,280,1,0,0,0,290,281,1,0,0,0,290,286,1,0,
        0,0,291,303,1,0,0,0,292,293,10,10,0,0,293,294,5,7,0,0,294,302,3,
        38,19,11,295,296,10,9,0,0,296,297,5,6,0,0,297,302,3,38,19,10,298,
        299,10,8,0,0,299,300,5,9,0,0,300,302,3,38,19,9,301,292,1,0,0,0,301,
        295,1,0,0,0,301,298,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,
        304,1,0,0,0,304,39,1,0,0,0,305,303,1,0,0,0,306,307,5,26,0,0,307,
        308,3,38,19,0,308,41,1,0,0,0,309,310,5,27,0,0,310,311,7,1,0,0,311,
        312,5,21,0,0,312,313,7,1,0,0,313,43,1,0,0,0,33,46,48,56,64,68,74,
        79,86,91,94,99,108,113,122,124,129,134,139,141,146,171,184,190,202,
        214,227,238,250,257,270,290,301,303
    ]

class GramParser ( Parser ):

    grammarFileName = "Gram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "'void'", "';'", "'~'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'if'", "'else'", "'do'", "'while'", "'return'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "','", "'&'", "'%'", 
                     "'_gp'", "'const'", "'print'", "'swap'" ]

    symbolicNames = [ "<INVALID>", "EQUAL_SIGN", "TYPE", "VOID", "SEMICOLON", 
                      "TILDE", "OP_ADDITIVE", "OP_MULTIPLICATIVE", "OP_INPLACE", 
                      "OP_COMPARATIVE", "IF", "ELSE", "DO", "WHILE", "RETURN", 
                      "OPENPAREN", "CLOSEPAREN", "OPENSQUARE", "CLOSESQUARE", 
                      "OPENCURLY", "CLOSECURLY", "COMMA", "ECOMMERCIAL", 
                      "PERCENTAGE", "GARBAGEPOINTER", "CONST", "PRINT_TOKEN", 
                      "SWPAP_TOKEN", "INT", "FLOAT", "ID", "WS" ]

    RULE_program = 0
    RULE_functionDecl = 1
    RULE_functionImpl = 2
    RULE_functionCall = 3
    RULE_fargs = 4
    RULE_aargs = 5
    RULE_body = 6
    RULE_stmt = 7
    RULE_varDecl = 8
    RULE_assignment = 9
    RULE_reAssign = 10
    RULE_ipAssign = 11
    RULE_reAssignS = 12
    RULE_ipAssignS = 13
    RULE_condStat = 14
    RULE_doWhile = 15
    RULE_reversingBody = 16
    RULE_returnStmt = 17
    RULE_num = 18
    RULE_expr = 19
    RULE_print = 20
    RULE_swap = 21

    ruleNames =  [ "program", "functionDecl", "functionImpl", "functionCall", 
                   "fargs", "aargs", "body", "stmt", "varDecl", "assignment", 
                   "reAssign", "ipAssign", "reAssignS", "ipAssignS", "condStat", 
                   "doWhile", "reversingBody", "returnStmt", "num", "expr", 
                   "print", "swap" ]

    EOF = Token.EOF
    EQUAL_SIGN=1
    TYPE=2
    VOID=3
    SEMICOLON=4
    TILDE=5
    OP_ADDITIVE=6
    OP_MULTIPLICATIVE=7
    OP_INPLACE=8
    OP_COMPARATIVE=9
    IF=10
    ELSE=11
    DO=12
    WHILE=13
    RETURN=14
    OPENPAREN=15
    CLOSEPAREN=16
    OPENSQUARE=17
    CLOSESQUARE=18
    OPENCURLY=19
    CLOSECURLY=20
    COMMA=21
    ECOMMERCIAL=22
    PERCENTAGE=23
    GARBAGEPOINTER=24
    CONST=25
    PRINT_TOKEN=26
    SWPAP_TOKEN=27
    INT=28
    FLOAT=29
    ID=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GramParser.EOF, 0)

        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(GramParser.FunctionDeclContext,i)


        def functionImpl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.FunctionImplContext)
            else:
                return self.getTypedRuleContext(GramParser.FunctionImplContext,i)


        def getRuleIndex(self):
            return GramParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 44
                    self.functionDecl()
                    pass

                elif la_ == 2:
                    self.state = 45
                    self.functionImpl()
                    pass


                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==3):
                    break

            self.state = 50
            self.match(GramParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(GramParser.TYPE, 0)

        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def OPENPAREN(self):
            return self.getToken(GramParser.OPENPAREN, 0)

        def CLOSEPAREN(self):
            return self.getToken(GramParser.CLOSEPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(GramParser.SEMICOLON, 0)

        def fargs(self):
            return self.getTypedRuleContext(GramParser.FargsContext,0)


        def VOID(self):
            return self.getToken(GramParser.VOID, 0)

        def getRuleIndex(self):
            return GramParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = GramParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(GramParser.TYPE)
                self.state = 53
                self.match(GramParser.ID)
                self.state = 54
                self.match(GramParser.OPENPAREN)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==25:
                    self.state = 55
                    self.fargs()


                self.state = 58
                self.match(GramParser.CLOSEPAREN)
                self.state = 59
                self.match(GramParser.SEMICOLON)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(GramParser.VOID)
                self.state = 61
                self.match(GramParser.ID)
                self.state = 62
                self.match(GramParser.OPENPAREN)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==25:
                    self.state = 63
                    self.fargs()


                self.state = 66
                self.match(GramParser.CLOSEPAREN)
                self.state = 67
                self.match(GramParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionImplContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(GramParser.TYPE, 0)

        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def OPENPAREN(self):
            return self.getToken(GramParser.OPENPAREN, 0)

        def CLOSEPAREN(self):
            return self.getToken(GramParser.CLOSEPAREN, 0)

        def OPENCURLY(self):
            return self.getToken(GramParser.OPENCURLY, 0)

        def CLOSECURLY(self):
            return self.getToken(GramParser.CLOSECURLY, 0)

        def fargs(self):
            return self.getTypedRuleContext(GramParser.FargsContext,0)


        def body(self):
            return self.getTypedRuleContext(GramParser.BodyContext,0)


        def VOID(self):
            return self.getToken(GramParser.VOID, 0)

        def getRuleIndex(self):
            return GramParser.RULE_functionImpl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionImpl" ):
                listener.enterFunctionImpl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionImpl" ):
                listener.exitFunctionImpl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionImpl" ):
                return visitor.visitFunctionImpl(self)
            else:
                return visitor.visitChildren(self)




    def functionImpl(self):

        localctx = GramParser.FunctionImplContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionImpl)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(GramParser.TYPE)
                self.state = 71
                self.match(GramParser.ID)
                self.state = 72
                self.match(GramParser.OPENPAREN)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==25:
                    self.state = 73
                    self.fargs()


                self.state = 76
                self.match(GramParser.CLOSEPAREN)
                self.state = 77
                self.match(GramParser.OPENCURLY)
                self.state = 79
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 78
                    self.body()


                self.state = 81
                self.match(GramParser.CLOSECURLY)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(GramParser.VOID)
                self.state = 83
                self.match(GramParser.ID)
                self.state = 84
                self.match(GramParser.OPENPAREN)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==25:
                    self.state = 85
                    self.fargs()


                self.state = 88
                self.match(GramParser.CLOSEPAREN)
                self.state = 89
                self.match(GramParser.OPENCURLY)
                self.state = 91
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 90
                    self.body()


                self.state = 93
                self.match(GramParser.CLOSECURLY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def OPENPAREN(self):
            return self.getToken(GramParser.OPENPAREN, 0)

        def CLOSEPAREN(self):
            return self.getToken(GramParser.CLOSEPAREN, 0)

        def aargs(self):
            return self.getTypedRuleContext(GramParser.AargsContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = GramParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(GramParser.ID)
            self.state = 97
            self.match(GramParser.OPENPAREN)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1895858208) != 0):
                self.state = 98
                self.aargs()


            self.state = 101
            self.match(GramParser.CLOSEPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FargsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def CONST(self):
            return self.getToken(GramParser.CONST, 0)

        def TYPE(self):
            return self.getToken(GramParser.TYPE, 0)

        def ECOMMERCIAL(self):
            return self.getToken(GramParser.ECOMMERCIAL, 0)

        def COMMA(self):
            return self.getToken(GramParser.COMMA, 0)

        def fargs(self):
            return self.getTypedRuleContext(GramParser.FargsContext,0)


        def OPENSQUARE(self):
            return self.getToken(GramParser.OPENSQUARE, 0)

        def INT(self):
            return self.getToken(GramParser.INT, 0)

        def CLOSESQUARE(self):
            return self.getToken(GramParser.CLOSESQUARE, 0)

        def getRuleIndex(self):
            return GramParser.RULE_fargs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFargs" ):
                listener.enterFargs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFargs" ):
                listener.exitFargs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFargs" ):
                return visitor.visitFargs(self)
            else:
                return visitor.visitChildren(self)




    def fargs(self):

        localctx = GramParser.FargsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fargs)
        self._la = 0 # Token type
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 103
                    self.match(GramParser.CONST)
                    self.state = 104
                    self.match(GramParser.TYPE)
                    pass

                elif la_ == 2:
                    self.state = 105
                    self.match(GramParser.TYPE)
                    self.state = 106
                    self.match(GramParser.ECOMMERCIAL)
                    pass

                elif la_ == 3:
                    self.state = 107
                    self.match(GramParser.TYPE)
                    pass


                self.state = 110
                self.match(GramParser.ID)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 111
                    self.match(GramParser.COMMA)
                    self.state = 112
                    self.fargs()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(GramParser.TYPE)
                self.state = 116
                self.match(GramParser.ID)
                self.state = 117
                self.match(GramParser.OPENSQUARE)
                self.state = 118
                self.match(GramParser.INT)
                self.state = 119
                self.match(GramParser.CLOSESQUARE)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 120
                    self.match(GramParser.COMMA)
                    self.state = 121
                    self.fargs()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AargsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def COMMA(self):
            return self.getToken(GramParser.COMMA, 0)

        def aargs(self):
            return self.getTypedRuleContext(GramParser.AargsContext,0)


        def num(self):
            return self.getTypedRuleContext(GramParser.NumContext,0)


        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_aargs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAargs" ):
                listener.enterAargs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAargs" ):
                listener.exitAargs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAargs" ):
                return visitor.visitAargs(self)
            else:
                return visitor.visitChildren(self)




    def aargs(self):

        localctx = GramParser.AargsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_aargs)
        self._la = 0 # Token type
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.match(GramParser.ID)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 127
                    self.match(GramParser.COMMA)
                    self.state = 128
                    self.aargs()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.num()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 132
                    self.match(GramParser.COMMA)
                    self.state = 133
                    self.aargs()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.expr(0)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 137
                    self.match(GramParser.COMMA)
                    self.state = 138
                    self.aargs()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.StmtContext)
            else:
                return self.getTypedRuleContext(GramParser.StmtContext,i)


        def getRuleIndex(self):
            return GramParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = GramParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097206308) != 0):
                self.state = 143
                self.stmt()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(GramParser.SEMICOLON, 0)

        def varDecl(self):
            return self.getTypedRuleContext(GramParser.VarDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(GramParser.AssignmentContext,0)


        def condStat(self):
            return self.getTypedRuleContext(GramParser.CondStatContext,0)


        def doWhile(self):
            return self.getTypedRuleContext(GramParser.DoWhileContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(GramParser.ReturnStmtContext,0)


        def swap(self):
            return self.getTypedRuleContext(GramParser.SwapContext,0)


        def print_(self):
            return self.getTypedRuleContext(GramParser.PrintContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = GramParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.expr(0)
                self.state = 150
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.varDecl()
                self.state = 153
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.assignment()
                self.state = 156
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.condStat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.doWhile()
                self.state = 160
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.returnStmt()
                self.state = 163
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 165
                self.swap()
                self.state = 166
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 168
                self.print_()
                self.state = 169
                self.match(GramParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(GramParser.TYPE, 0)

        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def EQUAL_SIGN(self):
            return self.getToken(GramParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def OPENSQUARE(self):
            return self.getToken(GramParser.OPENSQUARE, 0)

        def INT(self):
            return self.getToken(GramParser.INT, 0)

        def CLOSESQUARE(self):
            return self.getToken(GramParser.CLOSESQUARE, 0)

        def getRuleIndex(self):
            return GramParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = GramParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varDecl)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(GramParser.TYPE)
                self.state = 174
                self.match(GramParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(GramParser.TYPE)
                self.state = 176
                self.match(GramParser.ID)
                self.state = 177
                self.match(GramParser.EQUAL_SIGN)
                self.state = 178
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(GramParser.TYPE)
                self.state = 180
                self.match(GramParser.ID)
                self.state = 181
                self.match(GramParser.OPENSQUARE)
                self.state = 182
                self.match(GramParser.INT)
                self.state = 183
                self.match(GramParser.CLOSESQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ipAssign(self):
            return self.getTypedRuleContext(GramParser.IpAssignContext,0)


        def reAssign(self):
            return self.getTypedRuleContext(GramParser.ReAssignContext,0)


        def ipAssignS(self):
            return self.getTypedRuleContext(GramParser.IpAssignSContext,0)


        def reAssignS(self):
            return self.getTypedRuleContext(GramParser.ReAssignSContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = GramParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.ipAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.reAssign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.ipAssignS()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.reAssignS()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def EQUAL_SIGN(self):
            return self.getToken(GramParser.EQUAL_SIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)


        def OPENSQUARE(self):
            return self.getToken(GramParser.OPENSQUARE, 0)

        def CLOSESQUARE(self):
            return self.getToken(GramParser.CLOSESQUARE, 0)

        def getRuleIndex(self):
            return GramParser.RULE_reAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReAssign" ):
                listener.enterReAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReAssign" ):
                listener.exitReAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReAssign" ):
                return visitor.visitReAssign(self)
            else:
                return visitor.visitChildren(self)




    def reAssign(self):

        localctx = GramParser.ReAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_reAssign)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(GramParser.ID)
                self.state = 193
                self.match(GramParser.EQUAL_SIGN)
                self.state = 194
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(GramParser.ID)
                self.state = 196
                self.match(GramParser.OPENSQUARE)
                self.state = 197
                self.expr(0)
                self.state = 198
                self.match(GramParser.CLOSESQUARE)
                self.state = 199
                self.match(GramParser.EQUAL_SIGN)
                self.state = 200
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IpAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def OP_INPLACE(self):
            return self.getToken(GramParser.OP_INPLACE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)


        def OPENSQUARE(self):
            return self.getToken(GramParser.OPENSQUARE, 0)

        def CLOSESQUARE(self):
            return self.getToken(GramParser.CLOSESQUARE, 0)

        def getRuleIndex(self):
            return GramParser.RULE_ipAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIpAssign" ):
                listener.enterIpAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIpAssign" ):
                listener.exitIpAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIpAssign" ):
                return visitor.visitIpAssign(self)
            else:
                return visitor.visitChildren(self)




    def ipAssign(self):

        localctx = GramParser.IpAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ipAssign)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(GramParser.ID)
                self.state = 205
                self.match(GramParser.OP_INPLACE)
                self.state = 206
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(GramParser.ID)
                self.state = 208
                self.match(GramParser.OPENSQUARE)
                self.state = 209
                self.expr(0)
                self.state = 210
                self.match(GramParser.CLOSESQUARE)
                self.state = 211
                self.match(GramParser.OP_INPLACE)
                self.state = 212
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReAssignSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GARBAGEPOINTER(self):
            return self.getToken(GramParser.GARBAGEPOINTER, 0)

        def EQUAL_SIGN(self):
            return self.getToken(GramParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_reAssignS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReAssignS" ):
                listener.enterReAssignS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReAssignS" ):
                listener.exitReAssignS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReAssignS" ):
                return visitor.visitReAssignS(self)
            else:
                return visitor.visitChildren(self)




    def reAssignS(self):

        localctx = GramParser.ReAssignSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_reAssignS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(GramParser.GARBAGEPOINTER)
            self.state = 217
            self.match(GramParser.EQUAL_SIGN)
            self.state = 218
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IpAssignSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GARBAGEPOINTER(self):
            return self.getToken(GramParser.GARBAGEPOINTER, 0)

        def OP_INPLACE(self):
            return self.getToken(GramParser.OP_INPLACE, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_ipAssignS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIpAssignS" ):
                listener.enterIpAssignS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIpAssignS" ):
                listener.exitIpAssignS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIpAssignS" ):
                return visitor.visitIpAssignS(self)
            else:
                return visitor.visitChildren(self)




    def ipAssignS(self):

        localctx = GramParser.IpAssignSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ipAssignS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(GramParser.GARBAGEPOINTER)
            self.state = 221
            self.match(GramParser.OP_INPLACE)
            self.state = 222
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GramParser.IF, 0)

        def OPENPAREN(self):
            return self.getToken(GramParser.OPENPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def CLOSEPAREN(self):
            return self.getToken(GramParser.CLOSEPAREN, 0)

        def OPENCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.OPENCURLY)
            else:
                return self.getToken(GramParser.OPENCURLY, i)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.BodyContext)
            else:
                return self.getTypedRuleContext(GramParser.BodyContext,i)


        def CLOSECURLY(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.CLOSECURLY)
            else:
                return self.getToken(GramParser.CLOSECURLY, i)

        def CONST(self):
            return self.getToken(GramParser.CONST, 0)

        def ELSE(self):
            return self.getToken(GramParser.ELSE, 0)

        def getRuleIndex(self):
            return GramParser.RULE_condStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondStat" ):
                listener.enterCondStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondStat" ):
                listener.exitCondStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondStat" ):
                return visitor.visitCondStat(self)
            else:
                return visitor.visitChildren(self)




    def condStat(self):

        localctx = GramParser.CondStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condStat)
        self._la = 0 # Token type
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(GramParser.IF)
                self.state = 225
                self.match(GramParser.OPENPAREN)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 226
                    self.match(GramParser.CONST)


                self.state = 229
                self.expr(0)
                self.state = 230
                self.match(GramParser.CLOSEPAREN)
                self.state = 231
                self.match(GramParser.OPENCURLY)
                self.state = 232
                self.body()
                self.state = 233
                self.match(GramParser.CLOSECURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(GramParser.IF)
                self.state = 236
                self.match(GramParser.OPENPAREN)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==25:
                    self.state = 237
                    self.match(GramParser.CONST)


                self.state = 240
                self.expr(0)
                self.state = 241
                self.match(GramParser.CLOSEPAREN)
                self.state = 242
                self.match(GramParser.OPENCURLY)
                self.state = 243
                self.body()
                self.state = 244
                self.match(GramParser.CLOSECURLY)
                self.state = 245
                self.match(GramParser.ELSE)
                self.state = 246
                self.match(GramParser.OPENCURLY)
                self.state = 247
                self.body()
                self.state = 248
                self.match(GramParser.CLOSECURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(GramParser.DO, 0)

        def OPENCURLY(self):
            return self.getToken(GramParser.OPENCURLY, 0)

        def body(self):
            return self.getTypedRuleContext(GramParser.BodyContext,0)


        def CLOSECURLY(self):
            return self.getToken(GramParser.CLOSECURLY, 0)

        def WHILE(self):
            return self.getToken(GramParser.WHILE, 0)

        def OPENPAREN(self):
            return self.getToken(GramParser.OPENPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def CLOSEPAREN(self):
            return self.getToken(GramParser.CLOSEPAREN, 0)

        def reversingBody(self):
            return self.getTypedRuleContext(GramParser.ReversingBodyContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_doWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhile" ):
                listener.enterDoWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhile" ):
                listener.exitDoWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhile" ):
                return visitor.visitDoWhile(self)
            else:
                return visitor.visitChildren(self)




    def doWhile(self):

        localctx = GramParser.DoWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_doWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(GramParser.DO)
            self.state = 253
            self.match(GramParser.OPENCURLY)
            self.state = 254
            self.body()
            self.state = 255
            self.match(GramParser.CLOSECURLY)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 256
                self.reversingBody()


            self.state = 259
            self.match(GramParser.WHILE)
            self.state = 260
            self.match(GramParser.OPENPAREN)
            self.state = 261
            self.expr(0)
            self.state = 262
            self.match(GramParser.CLOSEPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReversingBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENCURLY(self):
            return self.getToken(GramParser.OPENCURLY, 0)

        def body(self):
            return self.getTypedRuleContext(GramParser.BodyContext,0)


        def CLOSECURLY(self):
            return self.getToken(GramParser.CLOSECURLY, 0)

        def getRuleIndex(self):
            return GramParser.RULE_reversingBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReversingBody" ):
                listener.enterReversingBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReversingBody" ):
                listener.exitReversingBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReversingBody" ):
                return visitor.visitReversingBody(self)
            else:
                return visitor.visitChildren(self)




    def reversingBody(self):

        localctx = GramParser.ReversingBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_reversingBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(GramParser.OPENCURLY)
            self.state = 265
            self.body()
            self.state = 266
            self.match(GramParser.CLOSECURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(GramParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = GramParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(GramParser.RETURN)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1895858208) != 0):
                self.state = 269
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GramParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GramParser.FLOAT, 0)

        def getRuleIndex(self):
            return GramParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = GramParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TILDE(self):
            return self.getToken(GramParser.TILDE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)


        def num(self):
            return self.getTypedRuleContext(GramParser.NumContext,0)


        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def GARBAGEPOINTER(self):
            return self.getToken(GramParser.GARBAGEPOINTER, 0)

        def functionCall(self):
            return self.getTypedRuleContext(GramParser.FunctionCallContext,0)


        def OPENSQUARE(self):
            return self.getToken(GramParser.OPENSQUARE, 0)

        def CLOSESQUARE(self):
            return self.getToken(GramParser.CLOSESQUARE, 0)

        def OPENPAREN(self):
            return self.getToken(GramParser.OPENPAREN, 0)

        def CLOSEPAREN(self):
            return self.getToken(GramParser.CLOSEPAREN, 0)

        def OP_MULTIPLICATIVE(self):
            return self.getToken(GramParser.OP_MULTIPLICATIVE, 0)

        def OP_ADDITIVE(self):
            return self.getToken(GramParser.OP_ADDITIVE, 0)

        def OP_COMPARATIVE(self):
            return self.getToken(GramParser.OP_COMPARATIVE, 0)

        def getRuleIndex(self):
            return GramParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GramParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 275
                self.match(GramParser.TILDE)
                self.state = 276
                self.expr(7)
                pass

            elif la_ == 2:
                self.state = 277
                self.num()
                pass

            elif la_ == 3:
                self.state = 278
                self.match(GramParser.ID)
                pass

            elif la_ == 4:
                self.state = 279
                self.match(GramParser.GARBAGEPOINTER)
                pass

            elif la_ == 5:
                self.state = 280
                self.functionCall()
                pass

            elif la_ == 6:
                self.state = 281
                self.match(GramParser.ID)
                self.state = 282
                self.match(GramParser.OPENSQUARE)
                self.state = 283
                self.expr(0)
                self.state = 284
                self.match(GramParser.CLOSESQUARE)
                pass

            elif la_ == 7:
                self.state = 286
                self.match(GramParser.OPENPAREN)
                self.state = 287
                self.expr(0)
                self.state = 288
                self.match(GramParser.CLOSEPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 301
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = GramParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 292
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 293
                        self.match(GramParser.OP_MULTIPLICATIVE)
                        self.state = 294
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = GramParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 295
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 296
                        self.match(GramParser.OP_ADDITIVE)
                        self.state = 297
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = GramParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 298
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 299
                        self.match(GramParser.OP_COMPARATIVE)
                        self.state = 300
                        self.expr(9)
                        pass

             
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_TOKEN(self):
            return self.getToken(GramParser.PRINT_TOKEN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = GramParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(GramParser.PRINT_TOKEN)
            self.state = 307
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwapContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWPAP_TOKEN(self):
            return self.getToken(GramParser.SWPAP_TOKEN, 0)

        def COMMA(self):
            return self.getToken(GramParser.COMMA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.ID)
            else:
                return self.getToken(GramParser.ID, i)

        def GARBAGEPOINTER(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.GARBAGEPOINTER)
            else:
                return self.getToken(GramParser.GARBAGEPOINTER, i)

        def getRuleIndex(self):
            return GramParser.RULE_swap

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwap" ):
                listener.enterSwap(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwap" ):
                listener.exitSwap(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwap" ):
                return visitor.visitSwap(self)
            else:
                return visitor.visitChildren(self)




    def swap(self):

        localctx = GramParser.SwapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_swap)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(GramParser.SWPAP_TOKEN)
            self.state = 310
            _la = self._input.LA(1)
            if not(_la==24 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 311
            self.match(GramParser.COMMA)
            self.state = 312
            _la = self._input.LA(1)
            if not(_la==24 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         




