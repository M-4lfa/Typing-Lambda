# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:40:49 2023

@author: Moisés
"""

from typing import Union, Optional
from dataclasses import dataclass
import Typinglexer.lexer as LexerT

Expression_Literal = Union["LexerT.BoolExpresion","LexerT.Int"]
Expression_Function = Union["LexerT.BoolExpresion","LexerT.Int"]
Expression_Type = Union["LexerT.BoolExpresion","LexerT.Int", "TypeExpression"]

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



def parser_literal (tokens = list["LexerT.Token"])->Optional[(list["LexerT.Token"])]:
    print(tokens,"newtokens en parsr.py")
    if len(tokens)> 0:
        if isinstance(tokens[0], LexerT.BoolExpresion) or isinstance(tokens[0], LexerT.Int):
            Lit = Literal(tokens[0])
            new_tokens = tokens[1:]
            return new_tokens
        else:
            return None
    else:
        return None
    
def parser_aplication_expression (tokens = list["LexerT.Token"])->Optional[AplicationExpression]:
    print(tokens,"newtokens")
    if len(tokens)> 0:
        if tokens[0] is LexerT.LeftP():
            new_tokens = tokens[1:]
            b = parser_expression(new_tokens)
            if  b is not None: 
                new_tokens, left_expression = parser_expression(new_tokens)
            b = parser_expression(new_tokens)
            if  b is not None:
                new_tokens, right_expression = parser_expression(new_tokens)
            return new_tokens, AplicationExpression(left_expression, right_expression), 
        else:
            return None
        
def parser_if_expression (tokens = list["LexerT.Token"])->Optional[IfExpression]:
    print(tokens,"newtokens")
    if len(tokens)> 0:
        if tokens[0] is LexerT.If():
            new_tokens = tokens[1:]
            new_tokens, first_expression = parser_expression(new_tokens)
            if tokens[0] is LexerT.Then():
                new_tokens, second_expression = parser_expression(new_tokens)
                if tokens[0] is LexerT.Else():
                    new_tokens, second_expression = parser_expression(new_tokens)
        else:
            return tokens, None
            
def parser_expression (token_list = list["Lexer.Token"]):    
    parser_list = [
        parser_aplication_expression,
        parser_literal  
    ]
    pass            
        
    
    
def main(): 
    a = LexerT.lexer_token("ñaldfjvh")
    print(a)
    b = parser_literal(a)
    print(b)


if __name__ == "__main__":
    main()



























