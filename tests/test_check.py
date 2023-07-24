# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:07:42 2023

@author: Moisés
"""
from Typinglexer.lexer import Stream, Operator, Int, Variable
from Typinglexer.lexer import lexer_operator, lexer_variable, lexer_int, lexer_leftp, lexer_rightp
    

###############################################################################
#Funciones de prueba, se envia quetipo de fucnion, la cadena y si regresa un valor o None
###############################################################################


def prueba_regresa_None(lexer, cadena_prueba:str):
    stream_prueba = Stream(cadena_prueba)
    get_none = lexer(stream_prueba) 
    assert get_none is None

def prueba_regresa_some(lexer, cadena_prueba:str,expect):
    stream_prueba = Stream(cadena_prueba)
    get_some = lexer(stream_prueba) 
    assert get_some == expect
    
def prueba_regresa_posicion(lexer, cadena_prueba:str,expect):
    stream_prueba = Stream(cadena_prueba)
    lexer(stream_prueba)
    posicion = stream_prueba.get_posicion()
    assert posicion == expect
    
     
###############################################################################
#Tests de Lexer_variable    
###############################################################################

def test_get_None_Variable():
    prueba_regresa_None(lexer_variable, "-2dfsg") 

def test_get_None_Void_Variable():
    prueba_regresa_None(lexer_variable, "")  


def test_get_some_variable():
    prueba_regresa_some(lexer_variable,"hola-a",Variable("hola"))


def test_get_one_variable():
    prueba_regresa_some(lexer_variable,"q",Variable("q"))

def test_get_some1_variable():
    prueba_regresa_some(lexer_variable,"qwerwerqwerwerqwerwerqwerwerqwerwer",
                        Variable("qwerwerqwerwerqwerwerqwerwerqwerwer"))

def test_get_None_variable():
    prueba_regresa_None(lexer_variable,"98274*59872")


###############################################################################
#Test de Lexer_int   
###############################################################################
def prueba_int(p):
    b = Stream(p)
    return lexer_int(b)

def test_get_Int_negativo():    
    assert prueba_int("-4") == Int(-4)
#########################################################

def test_get_None_Int():
    prueba_regresa_None(lexer_int, "asd") 

def test_get_None_Void_Int():
    prueba_regresa_None(lexer_int, "") 

def test_get_one_int():
    
    prueba_regresa_some(lexer_int,"4",Int(4))

def test_get_some1_int():
    prueba_regresa_some(lexer_int,"1234567890",Int(1234567890))

def test_get_None_int():
    prueba_regresa_None(lexer_int,"MOises")

def test_get_some_int():
    prueba_regresa_some(lexer_int,"43-2",Int(43))

###############################################################################
#Test de Lexer_operator
###############################################################################

def test_get_None_Operator():
    prueba_regresa_None(lexer_operator, "dfsg")    

def test_get_None_Void_operator():
    prueba_regresa_None(lexer_operator, "")    

def test_get_some_operator():
    prueba_regresa_some(lexer_operator,"+a",Operator("+"))

def test_get_one_operator():
    prueba_regresa_some(lexer_operator,"&",Operator("&"))

def test_get_some1_operator():
    prueba_regresa_some(lexer_operator,"*+*+*+*+*+",Operator("*"))

def test_get_some2_operator():
    prueba_regresa_some(lexer_operator,"<=*+*+*+*+",Operator("<="))

def test_get_None_operator1():
    prueba_regresa_None(lexer_operator,"24fq3gouh")

def test_get_some3_operator():
    prueba_regresa_some(lexer_operator,"<*+*+*+*+",Operator("<"))
    
def test_get_some4_operator():
    prueba_regresa_some(lexer_operator,"==r4r",Operator("=="))

def test_get_some5_operator():
    prueba_regresa_some(lexer_operator,"=a=r4r",Operator("="))
    
def test_get_some6_operator():
    prueba_regresa_some(lexer_operator,"=>",Operator("="))


###############################################################################
#Test de posicion Variable
###############################################################################

def test_get_posisicon_variable_0_nulo():
    prueba_regresa_posicion(lexer_variable, "", 0)
    
def test_get_posisicon_variable_1_():
    prueba_regresa_posicion(lexer_variable, "a", 1)
    
def test_get_posisicon_variable_5():
    prueba_regresa_posicion(lexer_variable, "qwert", 5)

def test_get_posisicon_variable_5_cortado():
    prueba_regresa_posicion(lexer_variable, "qwert3", 5)
    
def test_get_posisicon_variable_0_no_nulo():
    prueba_regresa_posicion(lexer_variable, "1qwert", 0)
    
###############################################################################
#Test de posicion Int
###############################################################################

def test_get_posisicon_int_0_nulo():
    prueba_regresa_posicion(lexer_int, "", 0)
    
def test_get_posisicon_int_1_():
    prueba_regresa_posicion(lexer_int, "1", 1)
    
def test_get_posisicon_int_5():
    prueba_regresa_posicion(lexer_int, "12345", 5)

def test_get_posisicon_int_5_cortado():
    prueba_regresa_posicion(lexer_int, "12345poi", 5)
    
def test_get_posisicon_int_0_no_nulo():
    prueba_regresa_posicion(lexer_int, "q12345", 0)
    
def test_get_posisicon_int_negativo_2():
    prueba_regresa_posicion(lexer_int, "-1", 2)

def test_get_posisicon_int_0_menos_nulo():
    prueba_regresa_posicion(lexer_int, "-q12345", 0)

def test_get_posisicon_int_menos():
    prueba_regresa_posicion(lexer_int, "-", 0)

def test_get_posisicon_int_menos_enmedio():
    prueba_regresa_posicion(lexer_int, "123-e", 3)
    
###############################################################################
#Test de posicion Operator
###############################################################################

def test_get_posisicon_operator_0_nulo():
    prueba_regresa_posicion(lexer_operator, "", 0)
    
def test_get_posisicon_operator_1():
    prueba_regresa_posicion(lexer_operator, "+", 1)
    
def test_get_posisicon_operator_2():
    prueba_regresa_posicion(lexer_operator, "<=", 2)

def test_get_posisicon_operator_1_cortado():
    prueba_regresa_posicion(lexer_operator, "=1=", 1)
    
def test_get_posisicon_operator_2_coratdo():
    prueba_regresa_posicion(lexer_operator, "===", 2)
    
def test_get_posisicon_operator_menos_con_digito():
    prueba_regresa_posicion(lexer_operator, "-1", 1)

def test_get_posisicon_operator_0_no_nulo():
    prueba_regresa_posicion(lexer_operator, "a*++", 0)

###############################################################################
#Test de posicion Operator
###############################################################################

def test_get_posisicon_leftP_0_nulo():
    prueba_regresa_posicion(lexer_leftp, "", 0)
    
def test_get_posisicon_leftP_1():
    prueba_regresa_posicion(lexer_leftp, "()", 1)
    

def test_get_posisicon_leftP_0_no_nulo():
    prueba_regresa_posicion(lexer_leftp, "ñaowifh", 0)
    
    
def test_get_posisicon_righP_0_nulo():
    prueba_regresa_posicion(lexer_rightp, "", 0)
    
def test_get_posisicon_righP_1():
    prueba_regresa_posicion(lexer_rightp, ")(", 1)
    
def test_get_posisicon_leftP_0_no_nulo():
    prueba_regresa_posicion(lexer_rightp, "ñaowifh", 0)


###############################################################################
#Test de return_token
###############################################################################
    
#def test_get_None_token():
    #prueba_regresa_None(return_token, "!2dfsg") 






































