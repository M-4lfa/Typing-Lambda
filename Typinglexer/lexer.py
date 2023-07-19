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
#Clase para recibir cadena de caracteres y la posiicon del carecter que se esta leyendo 
class Stream:
    value:str
    pos: int
    
    def __init__(self,value:str):
        self.pos = 0
        self.value=value
    
        #Funcion que obtiene el caracter en la posicion "pos" de la cadena original
    def get_char(self)->Optional[str]:
        if len(self.value)>self.pos:
            return self.value[self.pos]
        else:
            #Esta parte podria saltarse y dejar que solo retorne None
            return None 
    #Funcion que aumenta la posicion del carecter a leer
    def consume(self):
        self.pos+=1   
    #FUncion que retorna el string de la clase
    def get_string(self):
        return str(self.value)
    #Funcion que regresa la posicion del caracter a leer
    def get_posicion(self):
        return self.pos
    #Funcion que reescribe la poscion del caracter a leer
    
    def colcar_posicion(self, new_pos):
        self.pos = new_pos
        
        
 #Funcion que verifica que el caraceter ingresado es un digito       
def is_digit(string:str)->bool:
    """ Esta funcion verifica el primer caracter de un string sea un dígito"""
    if len(string)>0:
        digit = string[0]
        if digit >= "0" and digit <= "9":
            return True
        else: 
            return False
    else:
        return False
    
def is_operator(string:str)->bool:
    """ Esta funcion verifica el primer caracter de un string sea un dígito"""
    if len(string)>0:
        ope = string[0]
        if ope == "*" or ope == "+" or ope == "-" or ope == "=" or ope == "<" or ope == "^" or ope == "/":
            return True
        else: 
            return False
    else:
        return False





#Funcion que verifica que el caracter leido sea de la clase Variable 
# y regresa el segemnto de l string que sea del Variable
def lexer_variable (stream:Stream)->Optional[Variable]:
    acc:list[str]=[]
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


#Funcion que verifica que el caracter leido sea de la clase Int
# y regresa el segemnto del string que sea del tipo Int
def lexer_int(stream:Stream)->Optional[Int]:
    acc:list[str]=[]
    orig_post=stream.get_posicion()
    num = stream.get_char()
    if num is None:
        return None
    else: 
        if num == "-":
            acc.append(num)
            stream.consume()
            num = stream.get_char()
            if num is not None:
                if is_digit(num) :
                    while is_digit(num):
                        acc.append(num)
                        stream.consume()
                        num = stream.get_char()
                        if num is None:
                            break
                else:
                    return None
            else: 
                stream.colcar_posicion(orig_post)
                return None
        elif is_digit(num):
            while is_digit(num):
                acc.append(num)
                stream.consume()
                num = stream.get_char()
                if num is None:
                    break
        else:
            stream.colcar_posicion(orig_post)
            return None
    return Int(int("".join(acc)))  


#Funcion que verifica que el caracter leido sea de la clase Operator
# y regresa el segemnto del string que sea del tipo Operator
def lexer_operator(stream:Stream)->Optional[Operator]:

    acc:list[str]=[]
    orig_post=stream.get_posicion()
    oper = stream.get_char()
    print(oper)
    if oper is None:
        return None
    else: 
        if oper == "=":
            acc.append(oper)
            stream.consume()
            oper = stream.get_char()
            print(oper)
            if oper is not None:
                if is_operator(oper) :
                    while is_operator(oper):
                        
                        acc.append(oper)
                        
                        stream.consume()
                        oper = stream.get_char()
                        if oper is None:
                            break
                else:
                    return None
            else: 
                stream.colcar_posicion(orig_post)
                return None
        elif is_operator(oper):
            while is_operator(oper):
                acc.append(oper)
                stream.consume()
                oper = stream.get_char()
                if oper is None:
                    break
        else:
            stream.colcar_posicion(orig_post)
            return None
    return Operator(str("".join(acc)))  


            
#print(lexer_int(Stream("-121+3-4"))) 
def main():   
    b = Stream("2a^++q29=+a83*gf-9+r-38tf68+98-7fffg")
    print(b.get_string(),len(b.get_string()))
    index=[lexer_variable(b),lexer_int(b),lexer_operator(b)]
    index_token=["Variable","Int","Operator"]
    tokens = {'string':[],'Typetoken':[]}
    tokens_list = []
    stop = 0
    ind = 0
    finish = 0
    catch_token :[str]=[]
    while stop == 0:
        #print(index,b.get_posicion())
        #print("")
        catch_token = index[ind]
        #print(catch_token,"cath", ind,"##############")
        #print(finish)
        #print("")
        
        #time.sleep(.1)
        if catch_token is None:
            finish = finish + 1
            #print(finish,"finish")
            if finish == len(index):
                ind = 0
                stop =1
            #time.sleep(1)
        else:
            tokens['string'].append(catch_token)
            tokens_list.append(catch_token)
            tokens['Typetoken'].append(index_token[ind])
            #print(ind,"else222222")
            #print(tokens)
        if ind >= len(index)-1:
            ind = -1
            finish = 0
            index=[lexer_variable(b),lexer_int(b),lexer_operator(b)]
            #print(ind,"00000000")
            #print("")
            #print(tokens)
        #print(stop,"stop")
        
            #time.sleep(1)
        ind = ind + 1
        #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",ind)
    print(tokens['string'])
    print(tokens['Typetoken'])       


if __name__ =="__main__":
 main()






























