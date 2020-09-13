segment = int(input("Digite 1 para um segmento ou 0 para múltiplos: "))
#Um segmento
if(segment == 1):
    h = float(input("Insira o h: "))
    f0 = float(input("Insira o f0: "))
    f1 = float(input("Insira o f1: "))
    trap = h * (f0 + f1) / 2
    print("Resultado: " + str(trap))
#Multiplos Segmentos
else:
    f = []
    h = float(input("Insira o h: "))
    n = int(input("Insira o número de segmentos: "))
    for i in range(n):
        f.append(float(input("Insira o segmento: " + str(i+1) + ".\n")))
    soma = f[0]
    for i in range(n):
        soma = soma + 2 * f[i]
    soma = soma + f[0]
    trapm = h * soma / 2
    print("Resultado: " + str(trapm))