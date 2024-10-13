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
        4,1,30,335,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,4,0,49,8,0,11,0,12,0,50,1,0,1,0,
        1,1,1,1,1,1,1,1,3,1,59,8,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,
        1,1,1,3,1,71,8,1,1,2,1,2,1,2,1,2,3,2,77,8,2,1,2,1,2,1,2,3,2,82,8,
        2,1,2,1,2,1,2,1,2,1,2,3,2,89,8,2,1,2,1,2,1,2,3,2,94,8,2,1,2,3,2,
        97,8,2,1,3,1,3,1,3,3,3,102,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,111,
        8,4,1,4,1,4,1,4,3,4,116,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,125,
        8,4,3,4,127,8,4,1,5,1,5,1,5,3,5,132,8,5,1,5,1,5,1,5,3,5,137,8,5,
        1,5,1,5,1,5,3,5,142,8,5,3,5,144,8,5,1,6,5,6,147,8,6,10,6,12,6,150,
        9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,174,8,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,3,8,187,8,8,1,9,1,9,1,9,1,9,3,9,193,8,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,205,8,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,217,8,11,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,3,14,230,8,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,241,8,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,253,8,14,1,15,
        1,15,1,15,1,15,1,15,3,15,260,8,15,1,15,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,17,1,17,3,17,273,8,17,1,18,1,18,1,19,1,19,1,19,
        1,19,1,19,1,19,3,19,283,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,299,8,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,5,20,310,8,20,10,20,12,20,313,9,20,
        1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,3,22,333,8,22,1,22,0,1,40,23,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,2,1,0,27,
        28,2,0,23,23,29,29,362,0,48,1,0,0,0,2,70,1,0,0,0,4,96,1,0,0,0,6,
        98,1,0,0,0,8,126,1,0,0,0,10,143,1,0,0,0,12,148,1,0,0,0,14,173,1,
        0,0,0,16,186,1,0,0,0,18,192,1,0,0,0,20,204,1,0,0,0,22,216,1,0,0,
        0,24,218,1,0,0,0,26,222,1,0,0,0,28,252,1,0,0,0,30,254,1,0,0,0,32,
        266,1,0,0,0,34,270,1,0,0,0,36,274,1,0,0,0,38,282,1,0,0,0,40,298,
        1,0,0,0,42,314,1,0,0,0,44,332,1,0,0,0,46,49,3,2,1,0,47,49,3,4,2,
        0,48,46,1,0,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,
        1,0,0,0,51,52,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,55,5,2,0,0,55,
        56,5,29,0,0,56,58,5,14,0,0,57,59,3,8,4,0,58,57,1,0,0,0,58,59,1,0,
        0,0,59,60,1,0,0,0,60,61,5,15,0,0,61,71,5,4,0,0,62,63,5,3,0,0,63,
        64,5,29,0,0,64,66,5,14,0,0,65,67,3,8,4,0,66,65,1,0,0,0,66,67,1,0,
        0,0,67,68,1,0,0,0,68,69,5,15,0,0,69,71,5,4,0,0,70,54,1,0,0,0,70,
        62,1,0,0,0,71,3,1,0,0,0,72,73,5,2,0,0,73,74,5,29,0,0,74,76,5,14,
        0,0,75,77,3,8,4,0,76,75,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,
        5,15,0,0,79,81,5,18,0,0,80,82,3,12,6,0,81,80,1,0,0,0,81,82,1,0,0,
        0,82,83,1,0,0,0,83,97,5,19,0,0,84,85,5,3,0,0,85,86,5,29,0,0,86,88,
        5,14,0,0,87,89,3,8,4,0,88,87,1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,
        90,91,5,15,0,0,91,93,5,18,0,0,92,94,3,12,6,0,93,92,1,0,0,0,93,94,
        1,0,0,0,94,95,1,0,0,0,95,97,5,19,0,0,96,72,1,0,0,0,96,84,1,0,0,0,
        97,5,1,0,0,0,98,99,5,29,0,0,99,101,5,14,0,0,100,102,3,10,5,0,101,
        100,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,15,0,0,104,
        7,1,0,0,0,105,106,5,24,0,0,106,111,5,2,0,0,107,108,5,2,0,0,108,111,
        5,21,0,0,109,111,5,2,0,0,110,105,1,0,0,0,110,107,1,0,0,0,110,109,
        1,0,0,0,111,112,1,0,0,0,112,115,5,29,0,0,113,114,5,20,0,0,114,116,
        3,8,4,0,115,113,1,0,0,0,115,116,1,0,0,0,116,127,1,0,0,0,117,118,
        5,2,0,0,118,119,5,29,0,0,119,120,5,16,0,0,120,121,5,27,0,0,121,124,
        5,17,0,0,122,123,5,20,0,0,123,125,3,8,4,0,124,122,1,0,0,0,124,125,
        1,0,0,0,125,127,1,0,0,0,126,110,1,0,0,0,126,117,1,0,0,0,127,9,1,
        0,0,0,128,131,5,29,0,0,129,130,5,20,0,0,130,132,3,10,5,0,131,129,
        1,0,0,0,131,132,1,0,0,0,132,144,1,0,0,0,133,136,3,36,18,0,134,135,
        5,20,0,0,135,137,3,10,5,0,136,134,1,0,0,0,136,137,1,0,0,0,137,144,
        1,0,0,0,138,141,3,40,20,0,139,140,5,20,0,0,140,142,3,10,5,0,141,
        139,1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,128,1,0,0,0,143,
        133,1,0,0,0,143,138,1,0,0,0,144,11,1,0,0,0,145,147,3,14,7,0,146,
        145,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,
        13,1,0,0,0,150,148,1,0,0,0,151,152,3,40,20,0,152,153,5,4,0,0,153,
        174,1,0,0,0,154,155,3,16,8,0,155,156,5,4,0,0,156,174,1,0,0,0,157,
        158,3,18,9,0,158,159,5,4,0,0,159,174,1,0,0,0,160,174,3,28,14,0,161,
        162,3,30,15,0,162,163,5,4,0,0,163,174,1,0,0,0,164,165,3,34,17,0,
        165,166,5,4,0,0,166,174,1,0,0,0,167,168,3,44,22,0,168,169,5,4,0,
        0,169,174,1,0,0,0,170,171,3,42,21,0,171,172,5,4,0,0,172,174,1,0,
        0,0,173,151,1,0,0,0,173,154,1,0,0,0,173,157,1,0,0,0,173,160,1,0,
        0,0,173,161,1,0,0,0,173,164,1,0,0,0,173,167,1,0,0,0,173,170,1,0,
        0,0,174,15,1,0,0,0,175,176,5,2,0,0,176,187,5,29,0,0,177,178,5,2,
        0,0,178,179,5,29,0,0,179,180,5,1,0,0,180,187,3,40,20,0,181,182,5,
        2,0,0,182,183,5,29,0,0,183,184,5,16,0,0,184,185,5,27,0,0,185,187,
        5,17,0,0,186,175,1,0,0,0,186,177,1,0,0,0,186,181,1,0,0,0,187,17,
        1,0,0,0,188,193,3,22,11,0,189,193,3,20,10,0,190,193,3,26,13,0,191,
        193,3,24,12,0,192,188,1,0,0,0,192,189,1,0,0,0,192,190,1,0,0,0,192,
        191,1,0,0,0,193,19,1,0,0,0,194,195,5,29,0,0,195,196,5,1,0,0,196,
        205,3,40,20,0,197,198,5,29,0,0,198,199,5,16,0,0,199,200,3,40,20,
        0,200,201,5,17,0,0,201,202,5,1,0,0,202,203,3,40,20,0,203,205,1,0,
        0,0,204,194,1,0,0,0,204,197,1,0,0,0,205,21,1,0,0,0,206,207,5,29,
        0,0,207,208,5,7,0,0,208,217,3,40,20,0,209,210,5,29,0,0,210,211,5,
        16,0,0,211,212,3,40,20,0,212,213,5,17,0,0,213,214,5,7,0,0,214,215,
        3,40,20,0,215,217,1,0,0,0,216,206,1,0,0,0,216,209,1,0,0,0,217,23,
        1,0,0,0,218,219,3,38,19,0,219,220,5,1,0,0,220,221,3,40,20,0,221,
        25,1,0,0,0,222,223,3,38,19,0,223,224,5,7,0,0,224,225,3,40,20,0,225,
        27,1,0,0,0,226,227,5,9,0,0,227,229,5,14,0,0,228,230,5,24,0,0,229,
        228,1,0,0,0,229,230,1,0,0,0,230,231,1,0,0,0,231,232,3,40,20,0,232,
        233,5,15,0,0,233,234,5,18,0,0,234,235,3,12,6,0,235,236,5,19,0,0,
        236,253,1,0,0,0,237,238,5,9,0,0,238,240,5,14,0,0,239,241,5,24,0,
        0,240,239,1,0,0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,243,3,40,20,
        0,243,244,5,15,0,0,244,245,5,18,0,0,245,246,3,12,6,0,246,247,5,19,
        0,0,247,248,5,10,0,0,248,249,5,18,0,0,249,250,3,12,6,0,250,251,5,
        19,0,0,251,253,1,0,0,0,252,226,1,0,0,0,252,237,1,0,0,0,253,29,1,
        0,0,0,254,255,5,11,0,0,255,256,5,18,0,0,256,257,3,12,6,0,257,259,
        5,19,0,0,258,260,3,32,16,0,259,258,1,0,0,0,259,260,1,0,0,0,260,261,
        1,0,0,0,261,262,5,12,0,0,262,263,5,14,0,0,263,264,3,40,20,0,264,
        265,5,15,0,0,265,31,1,0,0,0,266,267,5,18,0,0,267,268,3,12,6,0,268,
        269,5,19,0,0,269,33,1,0,0,0,270,272,5,13,0,0,271,273,3,40,20,0,272,
        271,1,0,0,0,272,273,1,0,0,0,273,35,1,0,0,0,274,275,7,0,0,0,275,37,
        1,0,0,0,276,277,5,22,0,0,277,278,5,16,0,0,278,279,3,40,20,0,279,
        280,5,17,0,0,280,283,1,0,0,0,281,283,5,23,0,0,282,276,1,0,0,0,282,
        281,1,0,0,0,283,39,1,0,0,0,284,285,6,20,-1,0,285,299,3,36,18,0,286,
        299,5,29,0,0,287,299,3,38,19,0,288,299,3,6,3,0,289,290,5,29,0,0,
        290,291,5,16,0,0,291,292,3,40,20,0,292,293,5,17,0,0,293,299,1,0,
        0,0,294,295,5,14,0,0,295,296,3,40,20,0,296,297,5,15,0,0,297,299,
        1,0,0,0,298,284,1,0,0,0,298,286,1,0,0,0,298,287,1,0,0,0,298,288,
        1,0,0,0,298,289,1,0,0,0,298,294,1,0,0,0,299,311,1,0,0,0,300,301,
        10,9,0,0,301,302,5,6,0,0,302,310,3,40,20,10,303,304,10,8,0,0,304,
        305,5,5,0,0,305,310,3,40,20,9,306,307,10,7,0,0,307,308,5,8,0,0,308,
        310,3,40,20,8,309,300,1,0,0,0,309,303,1,0,0,0,309,306,1,0,0,0,310,
        313,1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,41,1,0,0,0,313,311,
        1,0,0,0,314,315,5,25,0,0,315,316,3,40,20,0,316,43,1,0,0,0,317,318,
        5,26,0,0,318,319,7,1,0,0,319,320,5,20,0,0,320,333,7,1,0,0,321,322,
        5,26,0,0,322,323,5,22,0,0,323,324,5,16,0,0,324,325,3,40,20,0,325,
        326,5,17,0,0,326,327,5,20,0,0,327,328,5,22,0,0,328,329,5,16,0,0,
        329,330,3,40,20,0,330,331,5,17,0,0,331,333,1,0,0,0,332,317,1,0,0,
        0,332,321,1,0,0,0,333,45,1,0,0,0,35,48,50,58,66,70,76,81,88,93,96,
        101,110,115,124,126,131,136,141,143,148,173,186,192,204,216,229,
        240,252,259,272,282,298,309,311,332
    ]

class GramParser ( Parser ):

    grammarFileName = "Gram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "'void'", "';'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'if'", "'else'", 
                     "'do'", "'while'", "'return'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "','", "'&'", "'%'", "'_gp'", 
                     "'const'", "'print'", "'swap'" ]

    symbolicNames = [ "<INVALID>", "EQUAL_SIGN", "TYPE", "VOID", "SEMICOLON", 
                      "OP_ADDITIVE", "OP_MULTIPLICATIVE", "OP_INPLACE", 
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
    RULE_special_ID = 19
    RULE_expr = 20
    RULE_print = 21
    RULE_swap = 22

    ruleNames =  [ "program", "functionDecl", "functionImpl", "functionCall", 
                   "fargs", "aargs", "body", "stmt", "varDecl", "assignment", 
                   "reAssign", "ipAssign", "reAssignS", "ipAssignS", "condStat", 
                   "doWhile", "reversingBody", "returnStmt", "num", "special_ID", 
                   "expr", "print", "swap" ]

    EOF = Token.EOF
    EQUAL_SIGN=1
    TYPE=2
    VOID=3
    SEMICOLON=4
    OP_ADDITIVE=5
    OP_MULTIPLICATIVE=6
    OP_INPLACE=7
    OP_COMPARATIVE=8
    IF=9
    ELSE=10
    DO=11
    WHILE=12
    RETURN=13
    OPENPAREN=14
    CLOSEPAREN=15
    OPENSQUARE=16
    CLOSESQUARE=17
    OPENCURLY=18
    CLOSECURLY=19
    COMMA=20
    ECOMMERCIAL=21
    PERCENTAGE=22
    GARBAGEPOINTER=23
    CONST=24
    PRINT_TOKEN=25
    SWPAP_TOKEN=26
    INT=27
    FLOAT=28
    ID=29
    WS=30

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
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.functionDecl()
                    pass

                elif la_ == 2:
                    self.state = 47
                    self.functionImpl()
                    pass


                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==3):
                    break

            self.state = 52
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
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(GramParser.TYPE)
                self.state = 55
                self.match(GramParser.ID)
                self.state = 56
                self.match(GramParser.OPENPAREN)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==24:
                    self.state = 57
                    self.fargs()


                self.state = 60
                self.match(GramParser.CLOSEPAREN)
                self.state = 61
                self.match(GramParser.SEMICOLON)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(GramParser.VOID)
                self.state = 63
                self.match(GramParser.ID)
                self.state = 64
                self.match(GramParser.OPENPAREN)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==24:
                    self.state = 65
                    self.fargs()


                self.state = 68
                self.match(GramParser.CLOSEPAREN)
                self.state = 69
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
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(GramParser.TYPE)
                self.state = 73
                self.match(GramParser.ID)
                self.state = 74
                self.match(GramParser.OPENPAREN)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==24:
                    self.state = 75
                    self.fargs()


                self.state = 78
                self.match(GramParser.CLOSEPAREN)
                self.state = 79
                self.match(GramParser.OPENCURLY)
                self.state = 81
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 80
                    self.body()


                self.state = 83
                self.match(GramParser.CLOSECURLY)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(GramParser.VOID)
                self.state = 85
                self.match(GramParser.ID)
                self.state = 86
                self.match(GramParser.OPENPAREN)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==24:
                    self.state = 87
                    self.fargs()


                self.state = 90
                self.match(GramParser.CLOSEPAREN)
                self.state = 91
                self.match(GramParser.OPENCURLY)
                self.state = 93
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 92
                    self.body()


                self.state = 95
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
            self.state = 98
            self.match(GramParser.ID)
            self.state = 99
            self.match(GramParser.OPENPAREN)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 952123392) != 0):
                self.state = 100
                self.aargs()


            self.state = 103
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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 105
                    self.match(GramParser.CONST)
                    self.state = 106
                    self.match(GramParser.TYPE)
                    pass

                elif la_ == 2:
                    self.state = 107
                    self.match(GramParser.TYPE)
                    self.state = 108
                    self.match(GramParser.ECOMMERCIAL)
                    pass

                elif la_ == 3:
                    self.state = 109
                    self.match(GramParser.TYPE)
                    pass


                self.state = 112
                self.match(GramParser.ID)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 113
                    self.match(GramParser.COMMA)
                    self.state = 114
                    self.fargs()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(GramParser.TYPE)
                self.state = 118
                self.match(GramParser.ID)
                self.state = 119
                self.match(GramParser.OPENSQUARE)
                self.state = 120
                self.match(GramParser.INT)
                self.state = 121
                self.match(GramParser.CLOSESQUARE)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 122
                    self.match(GramParser.COMMA)
                    self.state = 123
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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(GramParser.ID)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 129
                    self.match(GramParser.COMMA)
                    self.state = 130
                    self.aargs()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.num()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 134
                    self.match(GramParser.COMMA)
                    self.state = 135
                    self.aargs()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.expr(0)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 139
                    self.match(GramParser.COMMA)
                    self.state = 140
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
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1052797444) != 0):
                self.state = 145
                self.stmt()
                self.state = 150
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
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.expr(0)
                self.state = 152
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.varDecl()
                self.state = 155
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.assignment()
                self.state = 158
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.condStat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.doWhile()
                self.state = 162
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 164
                self.returnStmt()
                self.state = 165
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 167
                self.swap()
                self.state = 168
                self.match(GramParser.SEMICOLON)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 170
                self.print_()
                self.state = 171
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(GramParser.TYPE)
                self.state = 176
                self.match(GramParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(GramParser.TYPE)
                self.state = 178
                self.match(GramParser.ID)
                self.state = 179
                self.match(GramParser.EQUAL_SIGN)
                self.state = 180
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.match(GramParser.TYPE)
                self.state = 182
                self.match(GramParser.ID)
                self.state = 183
                self.match(GramParser.OPENSQUARE)
                self.state = 184
                self.match(GramParser.INT)
                self.state = 185
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
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.ipAssign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.reAssign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.ipAssignS()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
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
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(GramParser.ID)
                self.state = 195
                self.match(GramParser.EQUAL_SIGN)
                self.state = 196
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(GramParser.ID)
                self.state = 198
                self.match(GramParser.OPENSQUARE)
                self.state = 199
                self.expr(0)
                self.state = 200
                self.match(GramParser.CLOSESQUARE)
                self.state = 201
                self.match(GramParser.EQUAL_SIGN)
                self.state = 202
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
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(GramParser.ID)
                self.state = 207
                self.match(GramParser.OP_INPLACE)
                self.state = 208
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.match(GramParser.ID)
                self.state = 210
                self.match(GramParser.OPENSQUARE)
                self.state = 211
                self.expr(0)
                self.state = 212
                self.match(GramParser.CLOSESQUARE)
                self.state = 213
                self.match(GramParser.OP_INPLACE)
                self.state = 214
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

        def special_ID(self):
            return self.getTypedRuleContext(GramParser.Special_IDContext,0)


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
            self.state = 218
            self.special_ID()
            self.state = 219
            self.match(GramParser.EQUAL_SIGN)
            self.state = 220
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

        def special_ID(self):
            return self.getTypedRuleContext(GramParser.Special_IDContext,0)


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
            self.state = 222
            self.special_ID()
            self.state = 223
            self.match(GramParser.OP_INPLACE)
            self.state = 224
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
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(GramParser.IF)
                self.state = 227
                self.match(GramParser.OPENPAREN)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 228
                    self.match(GramParser.CONST)


                self.state = 231
                self.expr(0)
                self.state = 232
                self.match(GramParser.CLOSEPAREN)
                self.state = 233
                self.match(GramParser.OPENCURLY)
                self.state = 234
                self.body()
                self.state = 235
                self.match(GramParser.CLOSECURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(GramParser.IF)
                self.state = 238
                self.match(GramParser.OPENPAREN)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 239
                    self.match(GramParser.CONST)


                self.state = 242
                self.expr(0)
                self.state = 243
                self.match(GramParser.CLOSEPAREN)
                self.state = 244
                self.match(GramParser.OPENCURLY)
                self.state = 245
                self.body()
                self.state = 246
                self.match(GramParser.CLOSECURLY)
                self.state = 247
                self.match(GramParser.ELSE)
                self.state = 248
                self.match(GramParser.OPENCURLY)
                self.state = 249
                self.body()
                self.state = 250
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
            self.state = 254
            self.match(GramParser.DO)
            self.state = 255
            self.match(GramParser.OPENCURLY)
            self.state = 256
            self.body()
            self.state = 257
            self.match(GramParser.CLOSECURLY)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 258
                self.reversingBody()


            self.state = 261
            self.match(GramParser.WHILE)
            self.state = 262
            self.match(GramParser.OPENPAREN)
            self.state = 263
            self.expr(0)
            self.state = 264
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
            self.state = 266
            self.match(GramParser.OPENCURLY)
            self.state = 267
            self.body()
            self.state = 268
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
            self.state = 270
            self.match(GramParser.RETURN)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 952123392) != 0):
                self.state = 271
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
            self.state = 274
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
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


    class Special_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERCENTAGE(self):
            return self.getToken(GramParser.PERCENTAGE, 0)

        def OPENSQUARE(self):
            return self.getToken(GramParser.OPENSQUARE, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def CLOSESQUARE(self):
            return self.getToken(GramParser.CLOSESQUARE, 0)

        def GARBAGEPOINTER(self):
            return self.getToken(GramParser.GARBAGEPOINTER, 0)

        def getRuleIndex(self):
            return GramParser.RULE_special_ID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial_ID" ):
                listener.enterSpecial_ID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial_ID" ):
                listener.exitSpecial_ID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecial_ID" ):
                return visitor.visitSpecial_ID(self)
            else:
                return visitor.visitChildren(self)




    def special_ID(self):

        localctx = GramParser.Special_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_special_ID)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(GramParser.PERCENTAGE)
                self.state = 277
                self.match(GramParser.OPENSQUARE)
                self.state = 278
                self.expr(0)
                self.state = 279
                self.match(GramParser.CLOSESQUARE)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(GramParser.GARBAGEPOINTER)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(GramParser.NumContext,0)


        def ID(self):
            return self.getToken(GramParser.ID, 0)

        def special_ID(self):
            return self.getTypedRuleContext(GramParser.Special_IDContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(GramParser.FunctionCallContext,0)


        def OPENSQUARE(self):
            return self.getToken(GramParser.OPENSQUARE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)


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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 285
                self.num()
                pass

            elif la_ == 2:
                self.state = 286
                self.match(GramParser.ID)
                pass

            elif la_ == 3:
                self.state = 287
                self.special_ID()
                pass

            elif la_ == 4:
                self.state = 288
                self.functionCall()
                pass

            elif la_ == 5:
                self.state = 289
                self.match(GramParser.ID)
                self.state = 290
                self.match(GramParser.OPENSQUARE)
                self.state = 291
                self.expr(0)
                self.state = 292
                self.match(GramParser.CLOSESQUARE)
                pass

            elif la_ == 6:
                self.state = 294
                self.match(GramParser.OPENPAREN)
                self.state = 295
                self.expr(0)
                self.state = 296
                self.match(GramParser.CLOSEPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 309
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = GramParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 300
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 301
                        self.match(GramParser.OP_MULTIPLICATIVE)
                        self.state = 302
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = GramParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 303
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 304
                        self.match(GramParser.OP_ADDITIVE)
                        self.state = 305
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = GramParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 306
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 307
                        self.match(GramParser.OP_COMPARATIVE)
                        self.state = 308
                        self.expr(8)
                        pass

             
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(GramParser.PRINT_TOKEN)
            self.state = 315
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

        def PERCENTAGE(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.PERCENTAGE)
            else:
                return self.getToken(GramParser.PERCENTAGE, i)

        def OPENSQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.OPENSQUARE)
            else:
                return self.getToken(GramParser.OPENSQUARE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)


        def CLOSESQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.CLOSESQUARE)
            else:
                return self.getToken(GramParser.CLOSESQUARE, i)

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
        self.enterRule(localctx, 44, self.RULE_swap)
        self._la = 0 # Token type
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(GramParser.SWPAP_TOKEN)
                self.state = 318
                _la = self._input.LA(1)
                if not(_la==23 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 319
                self.match(GramParser.COMMA)
                self.state = 320
                _la = self._input.LA(1)
                if not(_la==23 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(GramParser.SWPAP_TOKEN)
                self.state = 322
                self.match(GramParser.PERCENTAGE)
                self.state = 323
                self.match(GramParser.OPENSQUARE)
                self.state = 324
                self.expr(0)
                self.state = 325
                self.match(GramParser.CLOSESQUARE)
                self.state = 326
                self.match(GramParser.COMMA)
                self.state = 327
                self.match(GramParser.PERCENTAGE)
                self.state = 328
                self.match(GramParser.OPENSQUARE)
                self.state = 329
                self.expr(0)
                self.state = 330
                self.match(GramParser.CLOSESQUARE)
                pass


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
        self._predicates[20] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




