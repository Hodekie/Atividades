
arrayalunos = [""]*5
tam = len(arrayalunos)
soma = 0
cont = 0
for x in range(tam):
    arrayalunos[x]=float(input("digite uma nota: "))
for i in range(tam):
    soma = soma + arrayalunos[i]
media = soma/tam
for y in range(tam):
    if arrayalunos[y]>media:
        cont=cont+1
print(f"A média da turma é {media} e {cont} alunos ficaram com nota acima da média")