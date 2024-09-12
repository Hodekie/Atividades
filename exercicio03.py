n1 = float(input("nota 1 aqui:"))
n2 = float(input("nota 2 aqui:"))
n3 = float(input("nota 3 aqui:"))

media = (n1 + n2 + n3) /3
if media >= 7:
    print(f"aluno aprovado media:{media:,.2f}")
else:
    if media >=4:
        print(f"aluno em recuperação:{media:,.2f}")

    else:
        print(f"aluno reprovado media:{media:,.2f}")







