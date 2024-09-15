grammar Gram;
import GrammaticaLessico;

program 
    : (functionDecl | functionImpl)+ EOF
    ;

functionDecl 
    : TYPE ID'(' fargs? ')' ';'
    | VOID ID'(' fargs? ')' ';'
    ;// fargs stand for formal args

functionImpl 
    : TYPE ID '(' fargs? ')'  '{'body?'}'
    | VOID ID '(' fargs? ')'  '{'body?'}'
    ;
functionCall : ID '('aargs?')'; // aargs stand for actual args
fargs 
    : (CONST TYPE | TYPE '&' | TYPE) ID (',' fargs)? 
    | TYPE ID '[' INT ']' (',' fargs)?
    ;

aargs
    : ID (',' aargs)?
    | num (',' aargs)?
    | expr (',' aargs)?
    ;

body : stmt*;
stmt
    : expr ';' // REMOVE ASAP 
    | varDecl  ';'
    | assignment ';'
    | condStat
    | doWhile ';'
    | returnStmt ';'
    | print ';'
    ;
    
varDecl     
    : TYPE ID
    | TYPE ID '=' expr
    | TYPE ID '['INT']'
    ;

assignment : ipAssign | reAssign;
reAssign:ID '=' expr
        |ID'['expr']' '=' expr;
ipAssign: ID OP_INPLACE expr
        | ID'['expr']' OP_INPLACE expr;
  
condStat
    : IF '(' expr ')' '{' body '}'
    | IF '(' expr ')' '{' body '}'
      ELSE '{' body '}'
    ;
doWhile
    : DO '{' body '}' WHILE '('expr')'
    ;


returnStmt : RETURN expr?;

num : INT | FLOAT;

expr: expr OP_MULTIPLICATIVE expr
    | expr OP_ADDITIVE expr
    | expr OP_COMPARATIVE expr
    | num
    | ID
    | functionCall
    | ID'['expr']' 
    | '(' expr ')'
    ;

print : PRINT_TOKEN expr;