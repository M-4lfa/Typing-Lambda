# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:07:42 2023

@author: Moisés
"""
from Typinglexer.lexer import (
    Stream,
    Operator,
    Int,
    Variable,
    LeftP,
    RightP,
    Token,
    TokenError,
    BoolType,
    BoolExpresion,
    LineLambda,
    If,
    Then,
    Equals,
    UnitExpresion,
    UnitType,
)
from Typinglexer.lexer import (
    lexer_operator,
    lexer_variable,
    lexer_int,
    lexer_leftp,
    lexer_rightp,
    lexer_string,
    lexer_booltype,
    lexer_equals,
    lexer_boolexpresion,
    lexer_if,
    lexer_lineLambda,
    lexer_then,
    lexer_unit_expresion,
    lexer_unit,
    lexer_tokens,
    lexer_space,
)

import pytest

from typing import TypeVar

T = TypeVar("T")

###############################################################################
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Pruebas Some y None!!!!!!!!!!!!!!!!!!!!!!!!!!"
# Funciones de prueba, se envia que tipo de fucnion, la cadena y si regresa un valor o None
###############################################################################


def prueba_regresa_None(lexer, cadena_prueba: str):
    stream_prueba = Stream(cadena_prueba)
    get_none = lexer(stream_prueba)
    assert get_none is None


def prueba_regresa_some(lexer, cadena_prueba: str, expect):
    stream_prueba = Stream(cadena_prueba)
    get_some = lexer(stream_prueba)
    assert get_some == expect


def prueba_regresa_posicion(lexer, cadena_prueba: str, expect):
    stream_prueba = Stream(cadena_prueba)
    lexer(stream_prueba)
    posicion = stream_prueba.get_posicion()
    assert posicion == expect


###############################################################################
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Prueba de Tokens!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
###############################################################################


def prueba_regresa_lexer_string(cadena_enviada: str, expect: T):
    b = lexer_string(cadena_enviada, expect)
    regreso = b(Stream(cadena_enviada))
    assert regreso == expect


def prueba_regresa_posicion_lexer_string(
    cadena_enviada: str, expect: T, posi: int
):
    b = lexer_string(cadena_enviada, expect)
    newstream = Stream(cadena_enviada)
    b(newstream)
    posicion = newstream.get_posicion()
    assert posicion == posi


def prueba_regresa_tokens(cadena_enviada: str, expect: T):
    lista_tokens = lexer_tokens(cadena_enviada)
    assert lista_tokens == expect


###############################################################################
"""Tests de None lexer variable"""
###############################################################################


@pytest.mark.parametrize(
    "cadena_prueba",
    [
        "",  # String vacio
        "-2dfsg",  # String con carecter no definido
        "1234314",  # string de otra clase
        "*+*",  # String de otra clase
        "_",  # solomante un guion
    ],
)
def test_get_none_variable(cadena_prueba: str):
    prueba_regresa_None(lexer_variable, cadena_prueba)


###############################################################################
"""Tests de some lexer Variable"""
###############################################################################
@pytest.mark.parametrize(
    "string, result",
    [
        ("_a", Variable("_a")),  # String comienza con _
        ("q", Variable("q")),  # String de un solo caracter
        (
            "qwerwerqwerwerqwerwerqwerwerqwerwer",
            Variable("qwerwerqwerwerqwerwerqwerwerqwerwer"),
        ),  # String Largo
        ("Hola1", Variable("Hola")),  # String cortado
        ("Hola_1", Variable("Hola")),  # String cortado con _
    ],
)
def test_get_some_variable(string: str, result: Variable):
    prueba_regresa_some(lexer_variable, string, result)


###############################################################################
"""Tests de None lexer Int"""
###############################################################################


@pytest.mark.parametrize(
    "cadena_prueba",
    [
        "",  # String vacio
        "#123",  # String con carecter no definido
        "KJB",  # String de otra clase
        "*++*",  # String de otra clase
        "-",  # solomante un menos
        "--2",  # solomante un menos
    ],
)
def test_get_none_int(cadena_prueba: str):
    prueba_regresa_None(lexer_int, cadena_prueba)


###############################################################################
"""Tests de some lexer Int"""


###############################################################################
@pytest.mark.parametrize(
    "string, result",
    [
        ("-1", Int(-1)),  # Numero negativo
        ("5", Int(5)),  # Numero normal
        ("2142345", Int(2142345)),  # Numero largo
        ("1324asdf", Int(1324)),  # Numero cortado
        ("1235-", Int(1235)),  # String cortado con
    ],
)
def test_get_some_int(string: str, result: Int):
    prueba_regresa_some(lexer_int, string, result)


###############################################################################
"""Tests de None lexer Operator"""
###############################################################################


@pytest.mark.parametrize(
    "cadena_prueba",
    [
        "",  # String vacio
        "#123",  # String con carecter no definido
        "KJB",  # String de otra clase
        "124",  # String de otra clase
        "=",  # solomante =
        "=>",  # Diferencia entre mayor igual
        "=<",  # Diferencia entre menor igual
        "=a=>",  # Igual cortado
    ],
)
def test_get_none_operator(cadena_prueba: str):
    prueba_regresa_None(lexer_operator, cadena_prueba)


###############################################################################
"""Tests de some lexer Operator"""


###############################################################################
@pytest.mark.parametrize(
    "string, result",
    [
        ("+", Operator("+")),  # Un solo operador
        ("*+*+*+*+*+", Operator("*")),  # Cadena de operadores
        ("<=*+*+*+*+", Operator("<=")),  # Detecta a menor o igual
        (">=*+*+*+*+", Operator(">=")),  # Detecta a mayor o igual
        ("<*+*+*+*+", Operator("<")),  # Detecta a memor que
        (">*+*+*+*+", Operator(">")),  # Detecta a memor que
        ("==*+*+*+*+", Operator("==")),  # Detecta al igual
    ],
)
def test_get_some_operator(string: str, result: Operator):
    prueba_regresa_some(lexer_operator, string, result)


###############################################################################
# Test de lexer_string
###############################################################################


@pytest.mark.parametrize(
    "stream,result",
    [
        ("", None),  # String vacio
        ("#123", None),  # String con carecter no definido
        ("a", Variable("a")),  # String con un solo carecter
        ("sfdgbasfg", Variable("sfdgbasfg")),
    ],
)
def test_get_some_string(stream: str, result: Variable):
    prueba_regresa_lexer_string(stream, result)


@pytest.mark.parametrize(
    "stream,vartype,result",
    [
        ("", None, 0),  # String vacio
        ("#123", None, 4),  # avanza aunque tenga un caracter no definido
        ("a", Variable("a"), 1),  # String con un solo carecter
        ("sfdgbasfg", Variable("sfdgbasfg"), 9),
    ],
)
def test_get_posicion_string(stream: str, vartype: Variable, result: int):
    prueba_regresa_posicion_lexer_string(stream, vartype, result)


"!!!!!!!!!!!!!!!!!!!!!!!!!!Test de posicion!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

###############################################################################
# Test de posicion Variable
###############################################################################


@pytest.mark.parametrize(
    "stream, result",
    [
        ("", 0),  # String nulo
        ("a", 1),  # Un solo caracter
        ("qwert", 5),  # cadena de caracteres
        ("qwert3", 5),  # cadena de caracteres cortado
        ("1qwert", 0),  # cadena de caracteres que no recorre
        ("_a", 2),  # detecta la cadana _a
        ("_", 0),  # No avanza cuando se envia _
    ],
)
def test_get_posisicon_variable(stream: str, result: int):
    prueba_regresa_posicion(lexer_variable, stream, result)


###############################################################################
# Test de posicion Int
###############################################################################


@pytest.mark.parametrize(
    "stream, result",
    [
        ("", 0),  # String nulo
        ("1", 1),  # Un solo caracter
        ("12345", 5),  # cadena de caracteres
        ("12345Qp", 5),  # cadena de caracteres cortado
        ("A12345", 0),  # cadena de caracteres que no recorre
        ("-334", 4),  # detecta numeros negativos
        ("-", 0),  # No avanza cuando se envia -
        ("-qweqr", 0),  # No avanza cuando se envia - y otros caracteres
        ("123-e", 3),  # Se corta en el menos -
    ],
)
def test_get_posisicon_int(stream: str, result: int):
    prueba_regresa_posicion(lexer_int, stream, result)


###############################################################################
# Test de posicion Operator
###############################################################################


@pytest.mark.parametrize(
    "stream, result",
    [
        ("", 0),  # String nulo
        ("+", 1),  # Un solo caracter
        (">=", 2),  # cadena de caracteres
        ("<=", 2),  # cadena de caracteres cortado
        ("==", 2),  # cadena de caracteres que no recorre
        ("=1=", 0),  # detecta la cadana _a
        ("-", 1),  # No avanza cuando se envia _
        ("-4", 1),  # No avanza cuando se envia un numero negativo
        ("===", 2),  # Solo detecta un igual
        ("a*++", 0),  # Cadena que nos avanza
    ],
)
def test_get_posisicon_operator(stream: str, result: int):
    prueba_regresa_posicion(lexer_operator, stream, result)


###############################################################################
# Test de posicion Parenteisis Left y Right
###############################################################################


@pytest.mark.parametrize(
    "stream, result",
    [
        ("", 0),  # String nulo
        ("(", 1),  # Un solo caracter
        ("(((", 1),  # Solo detecta 3 parentesis
        ("()", 1),  # Solo detecta un parentesis
        (")(", 0),  # Solo detecta un parentesis
        (")", 0),  # No avanza
        ("1", 0),  # No avanza
        ("-", 0),  # No avanza cuando se envia _
        ("a", 0),  # No avanza cuando se envia un numero negativo
    ],
)
def test_get_posisicon_leftp(stream: str, result: int):
    prueba_regresa_posicion(lexer_leftp, stream, result)


@pytest.mark.parametrize(
    "stream, result",
    [
        ("", 0),  # String nulo
        (")", 1),  # Un solo caracter
        ("))))", 1),  # Solo detecta 3 parentesis
        (")(", 1),  # Solo detecta un parentesis
        ("()", 0),  # No avanza
        ("1", 0),  # No avanza
        (
            "-",
            0,
        ),  # No avanza cuando se envia -, aunque creo que esto se podria evitar si hacemos priero un lexer de Int
        ("a", 0),  # No avanza cuando se envia un numero negativo
    ],
)
def test_get_posisicon_rightp(stream: str, result: int):
    prueba_regresa_posicion(lexer_rightp, stream, result)


###############################################################################
# Test de lexer_booltype
###############################################################################
@pytest.mark.parametrize(
    "stream, result",
    [
        ("", 0),  # String nulo
        ("bool", 4),
        ("Boole", 0),
        ("Bbool", 0),
        ("bo-ol", 0),
        ("booL", 0),
    ],
)
def test_get_posicion_boolextype(stream: str, result: int):
    prueba_regresa_posicion(lexer_booltype, stream, result)
    
    
    
@pytest.mark.parametrize(
    "cadena_prueba",
    [
        "flase",  # String vacio
        "Trrue",  # String con carecter no definido
        "true",  # string de otra clase
        "false",  # String de otra clase
        "    ",  # solomante un guion
    ],
)

def test_get_boolexpresion_none(cadena_prueba: str):
    prueba_regresa_None(lexer_boolexpresion, cadena_prueba)
    

@pytest.mark.parametrize(
    "stream, result",
    [
        ("True", BoolExpresion(True)),
        ("False", BoolExpresion(False)),
    ],
)

def test_get_boolexpresion(stream: str, result: int):
    prueba_regresa_some(lexer_boolexpresion, stream, result)


###############################################################################
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!TBorrar Espacios!!!!!!!!!!!!!!!!!!!!!!!!!!"
###############################################################################
@pytest.mark.parametrize(
    "string, result",
    [(" ", 1), (" a ", 1)],  # String nulo
)
def test_get_posicion_spaces(string: str, result: int):
    prueba_regresa_posicion(lexer_space, string, result)


###############################################################################
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Test de return_token!!!!!!!!!!!!!!!!!!!!!!!!!!"
###############################################################################
@pytest.mark.parametrize(
    "stream, result",
    [  ('', None)
       ("!", [TokenError("!")]),
        ("a", [Variable("a")]),
        ("12", [Int(12)]),
        ("==", [Operator("==")]),
        ("(", [LeftP()]),
        ("a1", [Variable("a"), Int(1)]),
        ("a*1", [Variable("a"), Operator("*"), Int(1)]),
        ("Manzana1", [Variable("Manzana"), Int(1)]),
        ("==1", [Operator("=="), Int(1)]),
        ("(a1)", [LeftP(), Variable("a"), Int(1), RightP()]),
        ("bool", [BoolType()]),
        ("False", [BoolExpresion(False)]),
        ("True", [BoolExpresion(True)]),
        ("True or False", [BoolExpresion(True),Variable("or"),BoolExpresion(False)]),
        ("->", [LineLambda()]),
        (
            "Teorema if1+1==2then1+2=3",
            [
                Variable("Teorema"),
                If(),
                Int(1),
                Operator("+"),
                Int(1),
                Operator("=="),
                Int(2),
                Then(),
                Int(1),
                Operator("+"),
                Int(2),
                Equals(),
                Int(3),
            ],
        ),
        (
            "Teorema  if 1+1==2 then 1+2=3",
            [
                Variable("Teorema"),
                If(),
                Int(1),
                Operator("+"),
                Int(1),
                Operator("=="),
                Int(2),
                Then(),
                Int(1),
                Operator("+"),
                Int(2),
                Equals(),
                Int(3),
            ],
        ),
        (
            "Teorema                              if 1+1==2 then 1+2=3",
            [
                Variable("Teorema"),
                If(),
                Int(1),
                Operator("+"),
                Int(1),
                Operator("=="),
                Int(2),
                Then(),
                Int(1),
                Operator("+"),
                Int(2),
                Equals(),
                Int(3),
            ],
        ),
    ],
)
def test_get_tokens(stream: str, result: list[Token]):
    prueba_regresa_tokens(stream, result)
