#https://docs.python.org/3/library/doctest.html
#https://docs.python.org/3/library/unittest.html
#https://docs.python.org/pt-br/3/library/unittest.html

from backend.Doctest.calculadora import *

try:
    print(soma(11,20))
except AssertionError as e:
    print("Conta invalida")
    print(e)

print("hello world")