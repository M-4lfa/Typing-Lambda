# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 18:32:10 2023

@author: Moisés
"""
SPACES : / |\n/+
%ignore SPACES

// Python re doesn't match "\n" by defect when using `.`
COMMENT_REST_OF_LINE: /#[^\n]*/

%ignore COMMENT_REST_OF_LINE

expression : variable
    | literal 
    | "(" expression expression ")"
    |"\" variable "->"  expression
    | "(" expression operator expression ")"
    | "if" expression "then" expression "else" expression

variable_character : "a" | ... | "z" | "A" | ... | "Z"
variable : "_" variable_character+ | variable_character+

literal : bool_literal | int_literal | "unit"

bool_literal : True | False

int_literal : 0 | 1 | -1 | 2 | -2 | ...

operator: "+" | "-" | "*" | "/" | "<" | ">" | "<=" | ">=" | "==" | "&" | "|" |"~"

type : "Bool" | "Int" | "Unit" | "(" type "->" type ")"

variable_definition : variable "=" expression
variable_declaration : variable ":" type