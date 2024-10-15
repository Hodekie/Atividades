arraynumeros = [0]*5
tam = len(arraynumeros)
for x in range(tam):
    arraynumeros[x]=int(input("digite um numero: "))
for i in range(tam-1,-1,-1):
    print(arraynumeros[i], end=" ")