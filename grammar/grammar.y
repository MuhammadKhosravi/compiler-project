%token NUM
%token ID
%start program
%%
program: declaration_list
;
declaration_list: declaration_list declaration
| declaration
;
declaration: var_declaration 
| fun_declaration 
;
var_declaration: type_specifier ID ';' 
| type_specifier ID '[' NUM ']' ';'
;
type_specifier: "int" 
| "void"
;
fun_declaration: type_specifier ID '(' params ')' compound_stmt # TODO
;
params: param_list
| "void"
;
param_list: param_list ',' param
| param
;
param: type_specifier ID
| type_specifier ID '[' ']'
;
compound_stmt: '{' local_declarations statement_list '}'
;
local_declarations: local_declarations var_declaration
| /* epsilon */
;
statement_list: statement_list statement
| /* epsilon */
;
statement: expression_stmt
| compound_stmt
| selection_stmt
| iteration_stmt
| return_stmt
| switch_stmt
;
expression_stmt: expression ';'
| "break" ';'
| ';'
;
selection_stmt: "if" '(' expression ')' #save statement "endif" #jpf
| "if" '(' expression ')' #save statement "else" #jpf_save statement "endif" #jp
;
iteration_stmt: "while" #label '(' expression ')' #save statement #while
;
return_stmt: "return" ';'
| "return" expression ';'
;
switch_stmt: #switch "switch" '(' #pid expression ')' '{' case_stmts default_stmt '}'#finish
;
case_stmts: case_stmts case_stmt
| /* epsilon */
;
case_stmt: #jpf_save "case" NUM #save':' statement_list #out
;
default_stmt: #jpf_save "default" ':' statement_list #out
| /* epsilon */
;
expression: var '=' expression #assign
| simple_expression
;
var: ID
| ID '[' expression ']'
;
simple_expression: additive_expression relop additive_expression
| additive_expression
;
relop: '<'
| "=="
;
additive_expression: additive_expression addop term #add
| term
;
addop: '+'
| '-'
;
term: term mulop factor #mult
| factor
;
mulop: '*'
| '/'
;
factor: '(' expression ')'
| var
| call
| NUM
| output
;
call: ID '(' args ')'
;
args: arg_list
| /* epsilon */
;
arg_list: arg_list ',' expression
| expression
;
output: "output " #pid factor #print
%%
