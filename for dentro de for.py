nomes=[0]*5
tam = len(nomes)
for x in range(tam):
    nomes[x]=input(" Digite um nome de Usuario: ")
for i in range(tam):
    print(i,nomes[i], end=" ")
for j in range(tam-1,-1,-1):
    print(j,nomes[j], end=" ")