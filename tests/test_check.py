# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:07:42 2023

@author: Moisés
"""
from Typinglexer.lexer import Stream, Operator, Int, Variable
from Typinglexer.lexer import lexer_operator, lexer_variable, lexer_int


def test_get_None_Operator():
    prueba_regresa_None(lexer_operator, "2dfsg")    

#########################################################
def test_get_None_Variable():
    prueba_regresa_None(lexer_variable, "-2dfsg")  
    
#########################################################
def test_get_None_Int():
    prueba_regresa_None(lexer_int, "asd")  

#########################################################
def test_get_None_Void_operator():
    prueba_regresa_None(lexer_operator, "")    

#########################################################
def test_get_None_Void_Variable():
    prueba_regresa_None(lexer_variable, "")  
    
#########################################################
def test_get_None_Void_Int():
    prueba_regresa_None(lexer_int, "")  

#########################################################
 
def test_regresa_Int_negativo():
    
    assert prueba_int("-4") == Int(-4)
    
def prueba_int(p):
    b = Stream(p)
    return lexer_int(b)

#########################################################
 
def test_regresa_some_variable():
    
    prueba_regresa_some(lexer_variable,"hola-a",Variable("hola"))

#########################################################
def test_regresa_some_int():
    
    prueba_regresa_some(lexer_int,"43-2",Int(43))
    
#########################################################
def test_regresa_some_operator():
    
    prueba_regresa_some(lexer_operator,"+ad",Operator("+"))


#########################################################
def prueba_regresa_None(lexer, cadena_prueba:str):
    stream_prueba = Stream(cadena_prueba)
    get_none = lexer(stream_prueba) 
    assert get_none is None

    
#########################################################

def prueba_regresa_some(lexer, cadena_prueba:str,expect):
    stream_prueba = Stream(cadena_prueba)
    get_some = lexer(stream_prueba) 
    
    assert get_some == expect

    
#########################################################













































