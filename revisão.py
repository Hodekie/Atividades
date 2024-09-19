numa = int(input("digite um numero"))
numb = int(input("digite um numero"))
numc = int(input("digite um numero"))
soma = numa+numb
if soma==numc:
    print(f"{soma} é igual a {numc}")
elif soma<numc:
    print(f"{soma} vai ser menor do que {numc}")
else:
    print(f"se {soma} for maior do que {numc}")