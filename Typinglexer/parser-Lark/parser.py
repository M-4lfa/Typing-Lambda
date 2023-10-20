# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:53:35 2023

@author: Moisés
"""

import logging
from lark import Lark, logger

logger.setLevel(logging.DEBUG)

collision_grammar = '''
SPACES : / |\n/x+
%ignore SPACES



VARIABLE_CHARACTER : /[a-zA-Z_]+/
VARIABLE :  VARIABLE_CHARACTER+

LITERAL : BOOL_LITERAL | INT_LITERAL | "UNIT"

BOOL_LITERAL : "True" | "False"

INT_LITERAL : /-?[1-9][0-9]*/ | /0+/

OPE_SUM: "+" | "-" 
OPE_MULT:  "*" | "/" 
OPE_COMPUESTO.2 : "<=" | ">=" |  "==" 
OPE_COMP: | "<" | ">" | "&" | "|" |"~"


operator: OPE_SUM|OPE_MULT|OPE_COMPUESTO|OPE_COMP



type : "Bool" | "Int" | "Unit" | "(" type "->" type ")"

variable_definition : VARIABLE "=" expression
variable_declaration : VARIABLE ":" type

expression : VARIABLE
            |LITERAL
            | "(" expression expression ")" 
            | "\\" VARIABLE "->" expression
            | "(" expression operator expression ")"
            | "if" expression "then" expression "else" expression



start: expression

'''
p = Lark(collision_grammar, parser='lalr', debug=True, strict = True)
print(p.parse("segt").pretty())
# Shift/Reduce conflict for terminal A: (resolving as shift)
#  * <as : >
# Shift/Reduce conflict for terminal A: (resolving as shift)
#  * <as : __as_star_0>