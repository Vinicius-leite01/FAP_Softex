


def main():

    quantidade = 10
    soma = 0
    for i in range(quantidade):
        numero = int(input(f'digite o {i+1} numero: '))
        soma = soma + numero
    media = soma/quantidade

    print("soma: ", soma)
    print("media: ", media)

main()