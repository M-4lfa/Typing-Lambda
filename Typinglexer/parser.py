# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:40:49 2023

@author: Moisés
"""

from typing import Union, Optional
from dataclasses import dataclass
import Typinglexer.lexer as LexerT

Expression_Literal = Union["LexerT.Boole","LexerT.Int"]
Expression_Function = Union["LexerT.Boole","LexerT.Int"]
Expression_Type = Union["LexerT.Boole","LexerT.Int", "TypeExpression"]

Expression = Union[
    "Variable",
    "Literal",
    "AplicationExpression",
    "FunctionExpression",
    "OperadorExpression",
    "IfExpression",
    "TypeExpression",    
    ]


@dataclass
class Variable:
    name: str

@dataclass 
class Literal:
    name: Expression_Literal

@dataclass 
class AplicationExpression:
    leftname: Expression
    rightname: Expression
        
@dataclass 
class FunctionExpression:
    Firstname: Variable
    Secondname: Expression

@dataclass 
class OperadorExpression:
    Firstname: Expression
    Secondname: Expression

@dataclass 
class IfExpression:
    Firstname: Expression
    Secondname: Expression
    Thirdname: Expression
    
@dataclass 
class TypeExpression:
    Firstname: Expression
    Secondname: Expression_Type



def parser_literal (tokens = Optional[list["LexerT.Token"]])->Optional[Literal]:
    print(tokens,"newtokens")
    if tokens is not None:
        new_tokens = tokens
        if isinstance(new_tokens[0], LexerT.BoolExpresion):
            if new_tokens[0] == LexerT.BoolExpresion(True):
                return Literal(LexerT.Bool(True))
            else:
                return Literal(LexerT.Bool(False))
        elif isinstance(new_tokens[0], LexerT.Int):
            return Literal(new_tokens[0])
        else:
            return None
    else:
        return None
    
    
def main(): 
    a = LexerT.lexer_token("ñaldfjvh")
    print(a)
    b = parser_literal(a)
    print(b)


if __name__ == "__main__":
    main()



























