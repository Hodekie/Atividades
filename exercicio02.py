print("digite a nota")
nota1 = int(input("digite aqui:"))
print("digite a nota")
nota2 = int(input("digite aqui:"))


if nota1 == nota2:
    print("iguais")
else:
    if nota1 > nota2:
        print(f"{nota2},\n"
              f"{nota1}")
    else:
        print(f"{nota1},\n"
              f"{nota2}")
