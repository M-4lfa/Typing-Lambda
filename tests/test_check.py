# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:07:42 2023

@author: Moisés
"""
from Typinglexer.lexer import Stream, Operator, Int, Variable
from Typinglexer.lexer import lexer_operator, lexer_variable, lexer_int


def test_regresa_Operador():
    
    assert prueba_operador("+") == Operator("+")
    
def prueba_operador(p):
    b = Stream(p)
    return lexer_operator(b)
#########################################################

def test_regresa_Int_negativo():
    
    assert prueba_int("-4") == Int(-4)
    
def prueba_int(p):
    b = Stream(p)
    return lexer_int(b)
#########################################################
def test_regresa_Varibale_acc():
    
    assert prueba_variable("acc") == Variable("acc")
    
def prueba_variable(p):
    b = Stream(p)
    return lexer_variable(b)
#########################################################
def prueba_regresa_None(lexer, cadena_prueba:str):
    stream_prueba = Stream(cadena_prueba)
    get_none = lexer(stream_prueba) 
    assert get_none is None
    

def test_get_None_Variable():
    prueba_regresa_None(lexer_variable, "2dfsg")
    
#########################################################