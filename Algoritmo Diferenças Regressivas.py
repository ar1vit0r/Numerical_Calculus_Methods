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
X = X-h

#O(h)
o = ( funcao(X) - funcao(X-h) ) / h

#O(h²) 
o2 = ( (3 * funcao(X)) - (4 * funcao(X-h)) + funcao(X-h-h) ) / (2 * h)

print("O(h): " + str(o))
print("O(h²): " + str(o2))