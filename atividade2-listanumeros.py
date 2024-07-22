def somar_valores(lista):
    soma = 0 
    for numero in lista:
        soma = soma + numero
    return soma

def media_valores(lista):
    soma = somar_valores
    media = soma/(len(lista))
    return media
def main():
    lista_numero = []
    numero = 0

    while numero != -1:
        numero = float(input('digite uma nota (-1 encerra): '))
        if numero != -1:
            if numero < 0 or numero > 10:
                print('número invalido')
            else:
                lista_numero.append(numero)
    
    # questão A
    print('quantidade de notas', len(lista_numero))
#questão b
    print("Seguem notas digitadas na ordem: ")
    for numero in lista_numero:
        print(numero, end=" ")
    print()

#questão c
    for i in range(len(lista_numero)-1, -1, -1):
        print(lista_numero[i], end=" ")
#questão d
    soma = somar_valores(lista_numero)
    print(f"a soma de todas as notas é: {soma}")        
#questao e
    media = media_valores(lista_numero)
    print(f"a media foi de: {media}")
    

main()