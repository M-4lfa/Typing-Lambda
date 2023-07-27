# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:07:42 2023

@author: Moisés
"""
from Typinglexer.lexer import (
        Stream, 
        Operator,
        Int,
        Variable
    )
from Typinglexer.lexer import (
        lexer_operator, 
        lexer_variable, 
        lexer_int, 
        lexer_leftp, 
        lexer_rightp, 
        lexer_string, 
        lexer_booltype
        )

import pytest

###############################################################################
#Funciones de prueba, se envia que tipo de fucnion, la cadena y si regresa un valor o None
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
    
    
def prueba_regresa_lexer_string(cadena_enviada:str):
    b = lexer_string(cadena_enviada)
    regreso = b(Stream(cadena_enviada))
    assert regreso == cadena_enviada
    
def prueba_regresa_posicion_lexer_string(cadena_enviada:str,expect):
    b = lexer_string(cadena_enviada)
    newstream = Stream(cadena_enviada)
    b(newstream)
    posicion = newstream.get_posicion()
    assert posicion == expect
     
###############################################################################
"""Tests de None lexer variable"""
###############################################################################

@pytest.mark.parametrize('cadena_prueba',
                         ["", #String vacio
                          '-2dfsg', #String con carecter no definido
                          "1234314", #string de otra clase
                          "*+*", #String de otra clase
                          "_", #solomante un guion
                          ],
                         )
def test_get_none_variable(cadena_prueba:str):
    prueba_regresa_None(lexer_variable,cadena_prueba) 

###############################################################################
"""Tests de some lexer Variable""" 
###############################################################################  
@pytest.mark.parametrize('string, result',
                         [("_a", Variable("_a")),#String comienza con _
                          ('q',Variable("q")), #String de un solo caracter
                          ("qwerwerqwerwerqwerwerqwerwerqwerwer",
                           Variable("qwerwerqwerwerqwerwerqwerwerqwerwer")), #String Largo
                          ("Hola1",Variable("Hola")), #String cortado
                          ("Hola_1",Variable("Hola"))#String cortado con _
                          ],
                         )

def test_get_some_variable(string: str, result: Variable):
    prueba_regresa_some(lexer_variable,string,result)

###############################################################################
"""Tests de None lexer Int"""
###############################################################################

@pytest.mark.parametrize('cadena_prueba',
                         ["", #String vacio
                          '#123', #String con carecter no definido
                          "KJB", #String de otra clase
                          "*++*", #String de otra clase
                          "-", #solomante un menos
                          ],
                         )
def test_get_none_int(cadena_prueba:str):
    prueba_regresa_None(lexer_int,cadena_prueba)


###############################################################################
"""Tests de some lexer Int""" 
###############################################################################  
@pytest.mark.parametrize('string, result',
                         [("-1", Int(-1)),#Numero negativo
                          ('5',Int(5)), #Numero normal
                          ("2142345", Int(2142345)), #Numero largo
                          ("1324asdf",Int(1324)), #Numero cortado
                          ("1235-",Int(1235))#String cortado con 
                          ],
                         )

def test_get_some_int(string: str, result: Int):
    prueba_regresa_some(lexer_int,string,result)


###############################################################################
"""Tests de None lexer Operator"""
###############################################################################

@pytest.mark.parametrize('cadena_prueba',
                         ["", #String vacio
                          '#123', #String con carecter no definido
                          "KJB", #String de otra clase
                          "124", #String de otra clase
                          "=", #solomante =
                          "=>" ,#Diferencia entre mayor igual
                          "=<", #Diferencia entre menor igual
                          "=a=>" #Igual cortado
                          ],
                         )
def test_get_none_operator(cadena_prueba:str):
    prueba_regresa_None(lexer_operator,cadena_prueba)


###############################################################################
"""Tests de some lexer Operator""" 
###############################################################################  
@pytest.mark.parametrize('string, result',
                         [("+", Operator("+")),#Un solo operador
                          ('*+*+*+*+*+',Operator("*")), #Cadena de operadores
                          ("<=*+*+*+*+", Operator("<=")), #Detecta a menor o igual
                          (">=*+*+*+*+",Operator(">=")), #Detecta a mayor o igual
                          ("<*+*+*+*+",Operator("<")),#Detecta a memor que
                          (">*+*+*+*+",Operator(">")),#Detecta a memor que
                          ("==*+*+*+*+",Operator("=="))#Detecta al igual
                          ],
                         )

def test_get_some_operator(string: str, result: Operator):
    prueba_regresa_some(lexer_operator,string,result)
    
    



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
    prueba_regresa_posicion(lexer_operator, "=1=", 0)
    
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
    prueba_regresa_posicion(lexer_rightp, ")", 1)
    
def test_get_posisicon_rightP_0_no_nulo():
    prueba_regresa_posicion(lexer_rightp, "ñaowifh", 0)
    
###############################################################################
#Test de lexer_string
###############################################################################
def test_get_lexer_string_1():
    prueba_regresa_lexer_string("a")

def test_get_lexer_string_0_nulo():
    prueba_regresa_lexer_string("")
    
def test_get_lexer_string_some_nulo():
    prueba_regresa_lexer_string("ñapiwfgañoksfnaoefnrloKFG")

def test_get_posisicon_lexer_string_1():
    prueba_regresa_posicion_lexer_string("a",1)
    
def test_get_posisicon_lexer_string_10():
    prueba_regresa_posicion_lexer_string("awedrftgyh",10)
    
def test_get_posisicon_lexer_string_0():
    prueba_regresa_posicion_lexer_string("",0)

###############################################################################
#Test de lexer_booltype
###############################################################################

def test_get_posisicon_booltype_4():
    prueba_regresa_posicion(lexer_booltype, "bool", 4)

def test_get_posisicon_booltype_():
    prueba_regresa_posicion(lexer_booltype, "Bbool", 0)


###############################################################################
#Test de return_token
###############################################################################
    
#def test_get_None_token():
    #prueba_regresa_None(return_token, "!2dfsg") 






































