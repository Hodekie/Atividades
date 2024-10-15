arraynumeros = [0]*10
tam = len(arraynumeros)

for x in range(tam):
    arraynumeros[x]= int(input(f"digite {x+1} numero: "))
arraynumeros2 = int(input("digite qualquer outro numero: "))
qtd = 0
for i in range(tam):
    if arraynumeros2 == arraynumeros[i]:
        qtd +=1
print(qtd)
