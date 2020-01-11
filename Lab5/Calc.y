%{
void yyerror (char *s);
int yylex();
#include <stdio.h>  
#include <stdlib.h>
#include <string.h>
#include <ctype.h>


char* identifiers[100];
int values[100];
int currentLen=0;
int findIdentifier(char *id);
void assignIdentifier(char* id,int val);
int readIdentifier(char *id);
%}

%union {int num; char* id;}       
%start programS
%token print
%token program
%token read
%token write
%token open_curly
%token closed_curly
%token dot
%token exit_command
%token <num> number
%token <id> identifier
%type <num> program exp term stmt
%type <id> assignment

%%

/* descriptions of expected inputs     corresponding actions (in C) */

programS : program stmtList '.'

stmtList: stmt					{;}
		| stmt ';' stmtList		{;}
		

stmt    : assignment ';'		{;}
		| exit_command ';'		{exit(EXIT_SUCCESS);}
		| print exp ';'			{printf("Printing %d\n", $2);}
		| stmt assignment ';'	{;}
		| stmt print exp ';'	{printf("Printing %d\n", $3);}
		| stmt exit_command  	{exit(EXIT_SUCCESS);}
        ;

assignment : identifier '=' exp  { assignIdentifier($1,$3); }
			;
exp    	: term                  {$$ = $1;}
       	| exp '+' term          {$$ = $1 + $3;}
       	| exp '-' term          {$$ = $1 - $3;}
		| exp '*' term          {$$ = $1 * $3;} 
       	;
term   	: number                {$$ = $1;}
		| identifier			{$$ = readIdentifier($1);} 
        ;

%%                    
int findIdentifier(char* id){
	int i;
	for(i=0;i<currentLen;i++){
		if (strcmp(id, identifiers[i]))
			return i;
	}
	return -1;
}
void assignIdentifier(char* id, int val){
	int pos=(findIdentifier(id));
	if (pos != -1){
		values[pos]=val;
	}else{
		identifiers[currentLen]=id;
		values[currentLen]=val;
		currentLen+=1;
	}	
}
int readIdentifier(char *id){
	int pos=(findIdentifier(id));
	if(pos == -1){
		return -1;
		printf("undefined variable %s\n", id);
		exit(1);
	}
	return values[pos];
}

int main (void) {
	/* init symbol table */
	int i;
	for(i=0; i<100; i++) {
		values[i] = 0;
		identifiers[i]=NULL;
	}
	return yyparse ( );
}

void yyerror (char *s) {fprintf (stderr, "%s\n", s);} 