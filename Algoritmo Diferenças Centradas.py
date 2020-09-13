from sympy import *

x = Symbol('x')

function = cos(x)

def funcao(x):
  return cos(x)

X = float(input("Entre com o valor de X: "))
f = funcao(X)
print("f = " + str(f) )

#1º Derivada

d1 = diff(function, x)
print("d1: " + str(d1))

h = 0.26179938779

#O(h²)
o = ( funcao(X+h) - funcao(X-h) ) / (2 * h)

#O(h^4) 
o2 = ( (-1 * funcao(X+h+h)) + (8 * funcao(X+h)) - (8 * funcao(X-h)) + funcao(X-h-h) ) / (12 * h)

print("O(h²): " + str(o))
print("O(h^4): " + str(o2))