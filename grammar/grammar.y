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
var_declaration: type_specifier declare_id pid ID ';'
| type_specifier declare_id pid ID '[' size NUM ']' ';'
;
type_specifier: "int" 
| "void"
;
fun_declaration: type_specifier declare_id pid ID '(' params ')' end_declare compound_stmt
;
params: param_list
| "void"
;
param_list: param_list ',' param
| param
;
param: type_specifier declare_id pid ID
| type_specifier declare_id pid ID '[' ']'
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
expression_stmt: expression finish_exp';'
| "break" ';'
| ';'
;
selection_stmt: "if" '(' expression condition ')' save statement "endif"
| "if" '(' expression condition ')' save statement "else" jpf_save statement "endif"
;

iteration_stmt: "while" label '(' expression condition')' save statement
;
return_stmt: "return" ';'
| "return" expression ';'
;
switch_stmt: start_switch "switch" '('expression ')' fake_save '{' case_stmts default_stmt '}'
;
case_stmts: case_stmts case_stmt
| /* epsilon */
;
case_stmt: jp_case "case" case_condition NUM save':' statement_list
;
default_stmt: jp_case "default" ':' statement_list
| /* epsilon */
;
expression: var '=' expression
| simple_expression
;
var: declare_id pid ID
| declare_id pid ID '[' expression ']'
;
simple_expression: additive_expression relop additive_expression
| additive_expression
;
relop: op '<'
| op "=="
;
additive_expression: additive_expression addop term
| term
;
addop: op '+'
| op '-'
;
term: term mulop factor
| factor
;
mulop: op '*'
| op '/'
;
factor: '(' expression ')'
| var
| call
| num NUM
;
call: declare_id pid  ID '(' args add_args ')'
;
add_args: /* epsilon */
;
args: arg_list
| /* epsilon */
;
arg_list: arg_list ',' expression
| expression
;
save: /* epsilon */
;
jpf_save: /* epsilon */
;
label: /* epsilon */
;
start_switch: /* epsilon */
;
pid: /* epsilon */
;
declare_id: /* epsilon */
;
end_declare: /* epsilon */
;
op: /* epsilon */
;
num: /* epsilon */
;
condition: /* epsilon */
;
size:  /* epsilon */
;
finish_exp: /* epsilon */
;
case_condition: /* epsilon */
;
fake_save: /* epsilon */
;
jp_case: /* epsilon */
;
%%
