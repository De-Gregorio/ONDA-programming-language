grammar GrammaticaLessico;

EQUAL_SIGN : '=';
TYPE : 'int' | 'float';
VOID : 'void';
SEMICOLON : ';';
OP_ADDITIVE : '+' | '-';
OP_MULTIPLICATIVE : '*' | '/';
OP_INPLACE : '+='
     | '-='
     | '*='
     | '/='
     | '%='
     ;
OP_COMPARATIVE : '==' 
     | '!=' 
     | '<' 
     | '>'
     | '<='
     | '>='    
     ; 
IF : 'if';
ELSE : 'else';
DO :'do';
WHILE : 'while';
RETURN : 'return';
OPENPAREN : '(';
CLOSEPAREN : ')'; 
OPENSQUARE : '[';
CLOSESQUARE : ']';
OPENCURLY : '{';
CLOSECURLY : '}';
COMMA : ',';
ECOMMERCIAL : '&';
PERCENTAGE : '%';
GARBAGEPOINTER : '_gp';
CONST : 'const' ;
PRINT_TOKEN : 'print' ;
INT : ('+'|'-')?[0-9]+ ;
FLOAT : [0-9]+'.'[0-9]* | [0-9]*'.'[0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;