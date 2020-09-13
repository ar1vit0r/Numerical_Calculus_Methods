  # define the function blocks
def simp13_():
    #Um segmento
    h = float(input("Insira o h: "))
    f0 = float(input("Insira o f0: "))
    f1 = float(input("Insira o f1: "))
    f2 = float(input("Insira o f2: "))
    simp13 = 2 * h * (f0 + 4 * f1 + f2) / 6
    print("Resultado: " + str(simp13))

def simp13_mult():
    #Multiplos Segmentos
    f = []
    h = float(input("Insira o h: "))
    n = int(input("Insira o número de segmentos: "))
    for i in range(n):
        f.append(float(input("Insira o segmento: " + str(i+1) + ".\n")))
    soma = f[0]
    for i in range(n-1):
        soma = soma + 4 * f[i] + 2 * f[i+1]
    soma = soma + 4 * f[n-2] + f[n-1]
    simp13 = h * soma / 3
    print("Resultado: " + str(simp13))

def simp38_():
    #Um segmento
    h = float(input("Insira o h: "))
    f0 = float(input("Insira o f0: "))
    f1 = float(input("Insira o f1: "))
    f2 = float(input("Insira o f2: "))
    f3 = float(input("Insira o f3: "))
    simp38 = 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8
    print("Resultado: " + str(simp38))

    # simpInt Functions
def simp13_mult2(f,h,n):
    soma = f[0]
    for i in range(n-1):
        soma = soma + 4 * f[i] + 2 * f[i+1]
    soma = soma + 4 * f[n-2] + f[n-1]
    return h * soma / 3

def simp38_2(h,f0,f1,f2,f3):
    return 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8

def trap_(h,f0,f1):
    return h * (f0 + f1) / 2

def simpInt_():
    f = []
    a = float(input("Insira o a: "))
    b = float(input("Insira o b: "))
    n = int(input("Insira o número de segmentos: "))
    for i in range(n):
        f.append(float(input("Insira o segmento: " + str(i+1) + ".\n")))
    soma = 0
    h = (b - a) / n
    if n == 1:
        soma = trap_(h,f[n-2],f[n-1])
    else:
        m = n
        odd = n / 2 - int(n / 2)
        if odd > 0 and n > 1:
            soma = soma + simp38_2(h,f[n-4],f[n-3],f[n-2],f[n-1])
            m = n - 3
        if m > 1:
            soma = soma + simp13_mult2(f,h,m)
    print("Resultado: " + str(soma))

# map the inputs to the function blocks
options = {1 : simp13_,
           2 : simp13_mult,
           3 : simp38_,
           4 : simpInt_,
}

op = int(input("Digite 1 para 1/3 de simpson uma aplicação\nDigite 2 para 1/3 de simpson múltiplas aplicações\nDigite 3 para 3/8 de simpson uma aplicação\nDigite 4 para regra de simpson para número de segmentos pares ou ímpares.\nOpção: "))
if op == 1:
    options[1]() 
elif op ==2:
    options[2]() 
elif op == 3:
    options[3]() 
elif op == 4:
    options[4]()
else:
    print("\nErro, não há esta opção.\n")