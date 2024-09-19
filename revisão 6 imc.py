peso = float(input("digite o seu peso: "))
altura = float(input("digite a sua altura: "))

imc = peso/(altura)**2
print(f"{imc:.2f}")
if imc<=18.5:
    print("você está abaixo do peso")
elif imc>=18.6 and imc<=24.9:
    print("você está no peso ideal, parabéns")
elif imc>=25.0 and imc<30.0:
    print("você está levemente acima do peso")
elif imc>=30.0 and imc<35.0:
    print("Obesidade grau I")
elif imc>=35.0 and imc<40.0:
    print("Obesidade grau II (severa)")
elif imc>=40.0:
    print("Obesidade grau III(mórbida)")



