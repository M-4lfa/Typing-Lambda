# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:53:32 2023

@author: Moisés
"""

import pytest

from Typinglexer.parser import (
    Expression_Literal,
    Expression_Function,
    Expression_Type,
    Variable,
    Expression,
    Literal,
    AplicationExpression,
    FunctionExpression,
    OperadorExpression,
    IfExpression,
    TypeExpression
    )

from Typinglexer.parser import (
    parser_literal
    )

import Typinglexer.lexer as LexerT


###############################################################################
"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Pruebas Some y None!!!!!!!!!!!!!!!!!!!!!!!!!!"
###############################################################################


def prueba_regresa_None(lexer, cadena_prueba: str):
    token_prueba = LexerT.lexer_tokens(cadena_prueba)
    print(token_prueba)
    get_none = lexer(token_prueba)
    print(get_none,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
    assert get_none is None


def prueba_regresa_some(lexer, cadena_prueba: str, expect):
    token_prueba = LexerT.lexer_tokens(cadena_prueba)
    get_some = lexer(token_prueba)
    assert get_some == expect


###############################################################################
"""Tests de None lexer variable"""
###############################################################################


@pytest.mark.parametrize(
    "cadena_prueba",
    [
        "",  # String vacio
        #"-2dfsg",  # String con carecter no definido
        # "1234314",  # string de otra clase
        # "*+*",  # String de otra clase
        # "_",  # solomante un guion
    ],
)
def test_get_none_variable(cadena_prueba: str):
    prueba_regresa_None(parser_literal, cadena_prueba)


###############################################################################
"""Tests de some lexer Variable"""
###############################################################################
# @pytest.mark.parametrize(
#     "string, result",
#     [
#         ("_a", Variable("_a"))
#     ],
# )
# def test_get_some_variable(string: str, result: Variable):
#     prueba_regresa_some(parser_literal, string, result)





























