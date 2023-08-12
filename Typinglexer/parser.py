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



def parser_literal (tokens = list["LexerT.Token"])->Optional[Literal]:
    new_tokens = tokens
    if new_tokens is not None:
        if isinstance(new_tokens[0], LexerT.BoolExpresion()):
            literal = new_tokens[0]
            return "a"
        else:
            return "a"
    else:
        return "a"
    
    




























