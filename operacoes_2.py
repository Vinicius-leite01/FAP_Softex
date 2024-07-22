def bem_vindo():
    numero1 = float(input("digite o primeiro número: "))
    numero2 = float(input("digite o segundo número: "))

def menu():
    print('menu de operadores: ')
    print("1 - adição")
    print("2 - subtração")
    opcao = int(input("digite a opção desejada: "))
    return opcao

def adicao(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtracao(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def main():
    bem_vindo()
    menu()
    opcao = menu()

    if opcao == 1:
        adicao()
        resultado = adicao
    elif opcao == 2:
        subtracao()
        resultado = subtracao
main()