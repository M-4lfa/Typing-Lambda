# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:10:34 2023

@author: Moisés
Definición de clases
"""
from dataclasses import dataclass
from typing import Union, Optional, Callable, TypeVar

Token = Union[
    "Variable",
    "Int",
    "Operator",
    "BoolExpresion",
    "BoolType",
    "LeftP",
    "RightP",
    "TokenError",
    "LineLambda",
    "UnitType",
    "UnitExpresion",
    "If",
    "Then",
    "Equals"
]


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
class BoolExpresion:
    name: bool


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
class LineLambda:
    pass


@dataclass
class UnitExpresion:
    pass


@dataclass
class UnitType:
    pass


@dataclass
class If:
    pass


@dataclass
class Then:
    pass


@dataclass
class Equals:
    pass


@dataclass
# Clase para recibir cadena de caracteres y la posiicon del carecter que se esta leyendo
class Stream:
    value: str
    pos: int

    def __init__(self, value: str):
        self.pos = 0
        self.value = value

        # Funcion que obtiene el caracter en la posicion "pos" de la cadena original

    def get_char(self) -> Optional[str]:
        if len(self.value) > self.pos:
            return self.value[self.pos]
        else:
            # Esta parte podria saltarse y dejar que solo retorne None
            return None

    # Funcion que aumenta la posicion del carecter a leer
    def consume(self):
        self.pos += 1

    # Funcion que retorna el string de la clase
    def get_string(self):
        return str(self.value)

    # Funcion que regresa la posicion del caracter a leer
    def get_posicion(self):
        return self.pos

    # Funcion que reescribe la poscion del caracter a leer
    def colcar_posicion(self, new_pos):
        self.pos = new_pos

    # Funcion que reescribe la poscion debido a una cadena
    def salto_posicion(self, jump_pos):
        print(jump_pos)
        self.pos = self.pos + jump_pos


T = TypeVar("T")


###############################################################################
# Funciones de is_some
###############################################################################


# Funcion que verifica que el caraceter ingresado es un digito
def is_digit(string: str) -> bool:
    """Esta funcion verifica el primer caracter de un string sea un dígito"""
    if len(string) > 0:
        digit = string[0]
        if digit >= "0" and digit <= "9":
            return True
        else:
            return False
    else:
        return False


def lexer_space(stream: Stream)->Optional[str]:
    f = lexer_string(" ", "a")
    return f(stream)

def lexer_spaces(stream:Stream)->None:
    result = lexer_space(stream)
    while result is not None:
        #print(stream)
        result = lexer_space(stream)
    return None
    


###############################################################################
"""!!!!!!!!!!!!!!!!!!!!!!!Funciones de Lexer_some!!!!!!!!!!!!!!!!!!!!!!!!!!!"""


###############################################################################
# Funcion  que verifica si una cadena de string esta dentro del stream
def lexer_string(string: str, varType: T) -> Callable[[Stream], Optional[T]]:
    def lexer_interno(stream: Stream) -> Optional[T]:
        orig_post = stream.get_posicion()  # print(string,orig_post)
        cadena_r = stream.get_string()  # print(cadena_r,"cadenaa",stream)
        new_cadena = cadena_r[
            orig_post:
        ]  
        if new_cadena is None:
            return None
        else:
            if new_cadena.startswith(string):
                salto = int(len(string))
                #       print(salto,"salto")
                stream.salto_posicion(salto)
                #      print(stream.get_posicion())
                return varType
            else:
                stream.colcar_posicion(orig_post)
                return None

    return lexer_interno


# Funcion que verifica que el caracter leido sea de la clase Variable
# y regresa el segemento del string que sea del Variable
###############################################################################
"""!!!!!!!!!!!!!!!!!!!!!!!Funciones de Lexer_variable!!!!!!!!!!!!!!!!!!!!!!!!!!!"""


###############################################################################
def lexer_variable(stream: Stream) -> Optional[Variable]:
    acc: list[str] = []
    orig_post = stream.get_posicion()
    char = stream.get_char()
    if char is None:
        return None
    else:
        if (
            (char == "_")
            or (char >= "a" and char <= "z")
            or (char >= "A" and char <= "Z")
        ):
            acc.append(char)
            stream.consume()
            char = stream.get_char()
            if char is None:
                if (acc[0] >= "a" and acc[0] <= "z") or (
                    acc[0] >= "A" and acc[0] <= "Z"
                ):
                    return Variable(acc[0])
                else:
                    stream.colcar_posicion(orig_post)
                    return None
            while (char >= "a" and char <= "z") or (
                char >= "A" and char <= "Z"
            ):
                acc.append(char)
                stream.consume()
                char = stream.get_char()
                if char is None:
                    break

            return Variable("".join(acc))
        else:
            return None


# -------------------------------------------------------------------


# Funcion que verifica que el caracter leido sea de la clase Int
# y regresa el segemnto del string que sea del tipo Int
def lexer_int(stream: Stream) -> Optional[Int]:
    acc: list[str] = []
    orig_post = stream.get_posicion()
    num = stream.get_char()
    if num is None:
        return None
    else:
        if num == "-":
            acc.append(num)
            stream.consume()
            num = stream.get_char()
            if num is not None:
                if is_digit(num):
                    while is_digit(num):
                        acc.append(num)
                        stream.consume()
                        num = stream.get_char()
                        if num is None:
                            break
                    else:
                        stream.colcar_posicion(orig_post)
                else:
                    stream.colcar_posicion(orig_post)
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


# -------------------------------------------------------------------
# Funcion que verifica que el caracter leido sea de la clase Operator
# y regresa el segemnto del string que sea del tipo Operator


def lexer_operator(stream: Stream) -> Optional[Operator]:
    index_oper = ["+", "*", "/", "<=", "<", ">=", ">", "&", "|", "==", "-"]
    for i in index_oper:
        """if i == "-":
        orig_post = stream.get_posicion()
         stream.consume()
         num = stream.get_char()
         if num is not None:
             if is_digit(num):
                 stream.colcar_posicion(orig_post)
                 return None
             else:
                 stream.colcar_posicion(orig_post)
         else:
             stream.colcar_posicion(orig_post)"""

        new_function = lexer_string(i, Operator(i))
        regreso = new_function(stream)
        if regreso is not None:
            return regreso
    return None


# -------------------------------------------------------------------


def lexer_leftp(stream: Stream) -> Optional[LeftP]:
    new_function = lexer_string("(", LeftP())
    regreso = new_function(stream)
    if regreso is not None:
        return regreso
    else:
        return None


"""f stream = 
 char '(' stream >>=  (\ x -> pure LeftP())"""

# -------------------------------------------------------------------


def lexer_rightp(stream: Stream) -> Optional[RightP]:
    new_function = lexer_string(")", RightP())
    regreso = new_function(stream)
    return regreso


# -------------------------------------------------------------------


def lexer_booltype(stream: Stream) -> Optional[BoolExpresion]:
    new_function = lexer_string("bool", BoolType())
    regreso = new_function(stream)
    return regreso


# -------------------------------------------------------------------
def lexer_boolexpresion(stream: Stream) -> Optional[BoolType]:
    new_function = lexer_string("True", BoolExpresion(True))
    regreso = new_function(stream)
    if regreso is None:
        new_function = lexer_string("False", BoolExpresion(False))
        regreso = new_function(stream)
    return regreso


# -------------------------------------------------------------------
def lexer_lineLambda(stream: Stream) -> Optional[LineLambda]:
    new_function = lexer_string("->", LineLambda())
    regreso = new_function(stream)
    return regreso


# -------------------------------------------------------------------
def lexer_if(stream: Stream) -> Optional[If]:
    new_function = lexer_string("if", If())
    regreso = new_function(stream)
    return regreso


# -------------------------------------------------------------------
def lexer_then(stream: Stream) -> Optional[Then]:
    new_function = lexer_string("then", Then())
    regreso = new_function(stream)
    return regreso


# -------------------------------------------------------------------
def lexer_equals(stream: Stream) -> Optional[Equals]:
    new_function = lexer_string("=", Equals())
    regreso = new_function(stream)
    return regreso


# -------------------------------------------------------------------
def lexer_unit_expresion(stream: Stream) -> Optional[UnitExpresion]:
    new_function = lexer_string("unit", UnitExpresion())
    regreso = new_function(stream)
    return regreso


# -------------------------------------------------------------------
def lexer_unit(stream: Stream) -> Optional[UnitType]:
    new_function = lexer_string("Unit", UnitType())
    regreso = new_function(stream)
    return regreso


###############################################################################
# Funcion Return_Token
###############################################################################
def lexer_tokens(input_string: str):
    char:Optional[Token]
    stream = Stream(input_string)
    lexer_list = [
        lexer_leftp,
        lexer_boolexpresion,
        lexer_booltype,
        lexer_if,
        lexer_lineLambda,
        lexer_rightp,
        lexer_then,
        lexer_unit,
        lexer_unit_expresion,
        lexer_variable,
        lexer_int,
        lexer_operator,
        lexer_equals
    ]
    tokens :list[Token] = []
    while stream.get_char() is not None:
        lexer_spaces(stream)
        for i in lexer_list:
            char = i(stream)
            if char is not None:
                tokens.append(char)
                break
        if char is None:
            char2 = stream.get_char()
            if  char2 is not None:
                tokens.append(TokenError(char2))
            break
    if len(tokens)>0:
        return tokens
    else:
        return None


"""def id(x:T)->T:
    return x"""


def main():
    b = ""
    print(lexer_tokens(b))


if __name__ == "__main__":
    main()
