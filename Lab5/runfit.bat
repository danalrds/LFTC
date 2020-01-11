bison -d Calc.y
flex MyScanner.l
gcc lex.yy.c Calc.tab.c -o calc 
calc
