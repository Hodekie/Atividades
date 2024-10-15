arraynomes = [0]*5
arraysenha = [0]*5
tam1 =len(arraynomes)

for x in range(tam1):
    arraynomes[x]=input("digite o nome do usuario: ")
    arraysenha[x]=int(input("digite a senha do usuario: "))
for j in range(tam1):
    print(arraynomes[j], arraysenha[j],j)