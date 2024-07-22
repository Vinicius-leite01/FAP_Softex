#def main():
#    for i in range(101, -1, -1):
#        print(i)


#main()

def main():
    contador = 1 
    numero_maior = float(input('digite o 1° numero: '))

    while contador < 5:
        numero = float(input(f" digite {contador + 1}° numero:"))
        if numero > numero_maior:
            numero_maior = numero
        contador += 1
    print(f"o maior numero digitado é {numero_maior}")




main()