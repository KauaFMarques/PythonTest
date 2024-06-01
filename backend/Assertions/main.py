#https://docs.python.org/3/library/doctest.html
#https://docs.python.org/3/library/unittest.html
#https://docs.python.org/pt-br/3/library/unittest.html

from calculadora import *

try:
    print(soma(10,20))
except AssertionError as e:
    print("Conta invalida")
    print(e)

print("hello world")