# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:10:34 2023

@author: Moisés
Definición de clases
"""
from dataclasses import dataclass
from typing import Union, Optional


Token = Union["Variable", "Int", "IntType", "Operator", "Bool", "BoolType", "LeftP", "RightP", "TokenError", "ArrowR", "LineLambda", "Twop", "UnitType", "UnitExp"]



@dataclass
class Int:
    value: int

@dataclass
class IntType:
    pass

@dataclass    
class Operator:
    name: str

@dataclass    
class Bool:
    value: bool
    
@dataclass   
class Variable:
    name: str
    
@dataclass    
class BoolType:
    pass
 
@dataclass
class TokenError:
    error: str 

@dataclass
class LeftP:
    pass

@dataclass
class RightP:
    pass

@dataclass
class ArrowR:
    pass

@dataclass
class LineLambda:
    pass

@dataclass
class Twop:
    pass

@dataclass
class UnitExp:
    pass

@dataclass
class UnitType:
    pass

@dataclass
class Stream:
    value:str
    pos: int
    def __init__(self,value:str):
        self.pos = 0
        self.value=value
        
    def get_char(self)->Optional[str]:
        if len(self.value)>self.pos:
            return self.value[self.pos]
        else:
            #Esta parte podria saltarse y dejar que solo retorne None
            return None 
    def consume(self):
        self.pos+=1   
        
    def get_posicion(self):
        return self.pos
    
    def colcar_posicion(self, new_pos):
        self.pos = new_pos
    

def lexer_variable (stream:Stream)->Optional[Variable]:
    acc:[str]=[]
    orig_post=stream.get_posicion()
    char=stream.get_char()
    if char is None:
        return None
    else: 
        if (char=="_")or(char>="a" and char<="z")or(char>="A" and char<="Z"):
            acc.append(char)
            stream.consume()
            char=stream.get_char()
            if char is None:
                if  (acc[0]>="a" and acc[0]<="z")or(acc[0]>="A" and acc[0]<="Z"):
                    return Variable(acc[0])
                stream.colcar_posicion(orig_post)
                return None
            while((char>="a" and char<="z")or(char>="A" and char<="Z")):
                acc.append(char)
                stream.consume()
                char=stream.get_char()
                if char is None:
                    break
            
            final_str= "".join(acc)
            if final_str =="_":
                return None
            return Variable("".join(acc))
        else:
            return None

print(lexer_variable(Stream("_augiugk$b")))    