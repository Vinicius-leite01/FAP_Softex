numero1 = int(input('digite o primeiro numero:'))
numero2 = int(input('digite o segundo numero:'))

print("Menu de operadores")
print('1- Adição')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão')
opção = int(input('digite a opção desejada:'))

if opção == 1:
    resultado = numero1 + numero2

elif opção == 2:
    resultado = numero1 - numero2

elif opção == 3:
    resultado = numero1 * numero2
elif opção == 4: 
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print('número não pode ser dividido por 0')
        resultado = None
else:
    print('opcão invalida')
if resultado is not None:
    print(f"resultado: {resultado:}")    