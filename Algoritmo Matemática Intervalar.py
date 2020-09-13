a = []
b = []
c = []

# define the function blocks

def intersec_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    b.append(float(input("\nInsira o x do conjunto B: ")))
    b.append(float(input("\nInsira o y do conjunto B: ")))
    if( a[0] > b[1] or a[1] < b[0]):
        return None
    else:
        c.append(max(a[0],b[0]))
        c.append(min(a[1],b[1]))
    print("\nA Intersecção é: [" + str(c[0]) + "," + str(c[1]) + "]")

def uni_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    b.append(float(input("\nInsira o x do conjunto B: ")))
    b.append(float(input("\nInsira o y do conjunto B: ")))
    c.append(min(a[0],b[0]))
    c.append(max(a[1],b[1]))
    print("\nA União é: [" + str(c[0]) + "," + str(c[1]) + "]")

def convexUni_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    b.append(float(input("\nInsira o x do conjunto B: ")))
    b.append(float(input("\nInsira o y do conjunto B: ")))
    c.append(min(a[0],b[0]))
    c.append(max(a[1],b[1]))
    print("\nA União Convexa é: [" + str(c[0]) + "," + str(c[1]) + "]")

def w_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    w = a[1] - a[0]
    print("\nO diâmetro de A é: " + str(w) )

def r_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    r = 0.5 * (a[1] - a[0])
    print("\nO raio de A é: " + str(r) )

def m_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    m = 0.5 * (a[0] + a[1])
    print("\nO Ponto médio de A é: " + str(m) )

def mod_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    m = max(abs(a[0]),abs(a[1])) #módulo
    print("\nO módulo de A é: " + str(m) )   
    
def dist_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    b.append(float(input("\nInsira o x do conjunto B: ")))
    b.append(float(input("\nInsira o y do conjunto B: ")))
    d = max(abs(a[0]-b[0]),abs(a[1]-b[1]))
    print("\nA Distância entre A e B é: " + str(d))

def add_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    b.append(float(input("\nInsira o x do conjunto B: ")))
    b.append(float(input("\nInsira o y do conjunto B: ")))
    c.append(a[0] + b[0])
    c.append(a[1] + b[1])
    print("\nA Adição é: [" + str(c[0]) + "," + str(c[1]) + "]")

def sub_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    b.append(float(input("\nInsira o x do conjunto B: ")))
    b.append(float(input("\nInsira o y do conjunto B: ")))
    c.append(a[0] - b[1])
    c.append(a[1] - b[0])
    print("\nA Subtração é: [" + str(c[0]) + "," + str(c[1]) + "]")

def mult_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    b.append(float(input("\nInsira o x do conjunto B: ")))
    b.append(float(input("\nInsira o y do conjunto B: ")))
    c.append( min(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]) )
    c.append( max(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]) )
    print("\nA Multiplicação é: [" + str(c[0]) + "," + str(c[1]) + "]")

def div_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    b.append(float(input("\nInsira o x do conjunto B: ")))
    b.append(float(input("\nInsira o y do conjunto B: ")))
    c.append( min(a[0]/b[0],a[0]/b[1],a[1]/b[0],a[1]/b[1]) )
    c.append( max(a[0]/b[0],a[0]/b[1],a[1]/b[0],a[1]/b[1]) )
    print("\nA Divisão é: [" + str(c[0]) + "," + str(c[1]) + "]")

def neg_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    c.append( -1*a[1] )
    c.append( -1*a[0] )
    print("\nO Negativo é: [" + str(c[0]) + "," + str(c[1]) + "]")

def recip_():
    a.append(float(input("\nInsira o x do conjunto A: ")))
    a.append(float(input("\nInsira o y do conjunto A: ")))
    c.append( 1/a[1] )
    c.append( 1/a[0] )
    print("\nA Recíproca é: [" + str(c[0]) + "," + str(c[1]) + "]")


# map the inputs to the function blocks
options = {1 : intersec_,
           2 : uni_,
           3 : convexUni_,
           4 : w_,
           5 : r_,
           6 : m_,
           7 : mod_,
           8 : dist_,
           9 : add_,
           10 : sub_,
           11 : mult_,
           12 : div_,
           13 : neg_,
           14 : recip_,
}

op = int(input("Digite 1 Intersecção\nDigite 2 para União\nDigite 3 para União Convexa\nDigite 4 para w(A) - Diâmetro de A\nDigite 5 para r(A) - Raio de A\nDigite 6 para m(A) - Ponto Médio de A\nDigite 7 para |A| - Módulo de A\nDigite 8 para d(A,B) - Distância entre A e B\nDigite 9 para A + B - Adição entre A e B\nDigite 10 para A - B - Subtração entre A e B\nDigite 11 para A * B - Multiplicação entre A e B\nDigite 12 para A / B - Divisão entre A e B\nDigite 13 para -A - Negativo de A\nDigite 14 para 1/A - Recíproca de A\nOpção: "))
if op == 1:
    options[1]() 
elif op ==2:
    options[2]() 
elif op == 3:
    options[3]() 
elif op == 4:
    options[4]()
elif op == 5:
    options[5]()
elif op == 6:
    options[6]()
elif op == 7:
    options[7]()
elif op == 8:
    options[8]()
elif op == 9:
    options[9]()
elif op == 10:
    options[10]()
elif op == 11:
    options[11]()
elif op == 12:
    options[12]()
elif op == 13:
    options[13]()
elif op == 14:
    options[14]()
else:
    print("\nErro, não há esta opção.\n")