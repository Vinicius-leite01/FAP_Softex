print('Sistema de calculo IMC')

peso = float(input("Insira seu peso em quilogramas (kg): "))
altura = float(input("Insira sua altura em metros(m): "))


imc = peso/(altura*altura)

print("IMC:", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc > 18.6 and imc < 24.9:
    print("Peso normal")
elif imc > 25 and imc < 29.9:
    print("Acima do peso")
elif imc > 30 and imc < 34.9:
    print(" Obesidade grau I")
elif imc > 35 and imc < 40:
    print(" Obesiade grau II")
elif imc > 40:
    print("Obesiade grau III")