# Language-Parser

Language-Parser is a program used to catch and display invalid tokens and statements for a simple pre-defined programming language.

## Run

Run the program followed by some text file that the parser will check for errors in.
```bash
python3 ParserDriver.py sometestcase.txt
```
If there are no errors the output will be 
```
Code parsed successfully
```
otherwise it should print out the type of error on a specific line and suggest an expected token. Ex: 
```
SYNTAX ERROR: found  Prog_Name on line  2  but expected  Prog
```

## Grammar

```
<program> ::= prog <progname> <compound stmt>
<compound stmt> ::= begin <stmt> {; <stmt>} end
<stmt> ::= <simple stmt> | <structured stmt>
<simple stmt> ::= <assignment stmt> | <read stmt> | <write stmt>
<assignment stmt> ::= <variable> <- <expression>
<read stmt> ::= read ( <variable> { , <variable> } )
<write stmt> ::= write ( <expression> { , <expression> } )
<structured stmt> ::= <compound stmt> | <if stmt> | <while stmt>
<if stmt> ::= if <expression> then <stmt> |
 if <expression> then <stmt> else <stmt>
<while stmt> ::= while <expression> do <stmt>
<expression> ::= <simple expr> |
 <simple expr> <relational_operator> <simple expr>
<simple expr> ::= [ <sign> ] <term> { <adding_operator> <term> }
<term> ::= <factor> { <multiplying_operator> <factor> }
<factor> ::= <variable> | <int_literal> | ( <expression> )
<sign> ::= + | -
<adding_operator> ::= + | -
<multiplying_operator> ::= * | /
<relational_operator> ::= = | <> | < | <= | >= | >
<variable> ::= <letter> { <letter> | <digit> }
<int_literal> ::= <digit> { <digit> }
<progname> ::= <capital_letter> { <letter> | <digit> }
<capital_letter> ::= A | B | C | ... | Z
<letter> ::= a | b | c | ... | z | <capital_letter>
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<comment> ::= // all text to end of line ignored
```
