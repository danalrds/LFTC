%{
#include "Calc.tab.h"
void yyerror (char *s);
int yylex();
%}
%%
"print"				   {return print;}
"program"			   {return program;}
"read"					{return read;}
"write"					{return write;}
"exit"				   {return exit_command;}
[\{\}\.]				{return yytext[0];}
[a-zA-Z]*			   {yylval.id = yytext; return identifier;}
[0-9]+                 {yylval.num = atoi(yytext); return number;}
[ \t\n]                ;
[-+*=;]           	   {return yytext[0];}
.                      {ECHO; yyerror ("unexpected character");}

%%
int yywrap (void) {return 1;}	
